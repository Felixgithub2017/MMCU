import argparse
import os
import numpy as np
import pandas as pd
import time
import requests
import json
import re

choices = ["A", "B", "C", "D"]

def find_valid_substrings(s):
    # 匹配长度为1到4的、不包含重复字符的子串
    pattern = r'[ABCD]{1,4}'
    substrings = re.findall(pattern, s)
    # 过滤出不包含重复字符的子串
    valid_substrings = [substring for substring in substrings if len(substring) == len(set(substring))]
    return valid_substrings

def format_subject(subject):
    l = subject.split("_")
    s = ""
    for entry in l:
        s += " " + entry
    return s

def format_example(df, idx, include_answer=True):
    prompt = df.iloc[idx, 0]
    k = df.shape[1] - 2
    for j in range(k):
        #prompt += "\n{}. {}".format(choices[j], df.iloc[idx, j+1])
        try:
            prompt += "\n{}. {}".format(choices[j], df.iloc[idx, j+1].replace(" ．", "").replace("A、", "").replace("B、", "").replace("C、", "").replace("D、", "").replace("A.", "").replace("B.", "").replace("C.", "").replace("D.", "").replace("A", "").replace("B", "").replace("C", "").replace("D", "").replace("Ａ、", "").replace("Ｂ、", "").replace("Ｃ、", "").replace("Ｄ、", "").strip())
        except Exception as e:
            prompt += "\n{}. {}".format(choices[j], df.iloc[idx, j+1])
    #prompt += "\nAnswer:"
    prompt += "\n正确答案的序号是："
    if include_answer:
        prompt += " {}\n\n".format(df.iloc[idx, k + 1])
    return prompt

# 生成 prompt
# 不提示专业科目，让模型直接理解题目
def gen_prompt(train_df, k=-1):
    prompt = "请阅读以下选择题并给出正确选项，不要解释原因。\n"
    if k == -1:
        k = train_df.shape[0]
    for i in range(k):
        prompt += format_example(train_df, i)
    
    return prompt

# chatgpt api
# 将此函数替换为付费api
def plain_chat(prompt):
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    url= 'your_paid_chatgpt_api'
    # 构造 post 数据
    postdata = {"content": prompt}
    postdata = json.dumps(postdata)
    r = requests.post(url, data=postdata, headers=headers)
    #print(r)
    json_content = json.loads(r.text)
    answer = json_content["texts"]
    return answer

def read_file_lines(file):
    with open(file, 'r', errors='ignore', encoding='utf8') as f:
        lines = f.readlines()
    return lines
    
def writelines_to_file(file, lines):
    with open(file, 'w', encoding='utf8') as f:
        f.writelines(lines)

def writetext_to_file(file, contents):
    with open(file, 'w', encoding='utf8') as f:
        f.write(contents)

def eval(args, subject, dev_df, test_df):
    logfile = "chatgptestlogfile0512"
    cors = []
    #labels = []
    preds = []
    for i in range(test_df.shape[0]):
        # get prompt and make sure it fits
        k = args.ntrain
        prompt_end = format_example(test_df, i, include_answer=False)
        train_prompt = gen_prompt(dev_df, k)
        prompt = train_prompt + prompt_end

        #print("train_prompt:", train_prompt)
        print("题目：", prompt)
        with open(logfile, 'a', encoding='utf8') as f:
            f.write(prompt+"\n")

        try:        
            label = test_df.iloc[i, test_df.shape[1]-1]
            # A B C D 特殊处理
            label = label.replace(" ", "").replace("Ａ", "A").replace("Ｂ", "B").replace("Ｃ", "C").replace("Ｄ", "D")
            print("正确答案:", label)
            with open(logfile, 'a', encoding='utf8') as f:
                f.write("正确答案:"+label+"\n")
        except Exception as e:
            print(e)
            break

        while True:
            try:
                time.sleep(1)
                pred = plain_chat(prompt)
                pred = pred.replace("、", "").replace(".", "").replace(",", "").replace(";", "").replace("，", "")
                # 识别答案pattern
                pred = find_valid_substrings(pred)[0]
                print("模型预测答案:", pred)
                with open(logfile, 'a', encoding='utf8') as f:
                    f.write("模型预测答案:"+pred+"\n")
                break
            except Exception as e:
                print(e)
                print("pausing")
                time.sleep(2)
                continue

        try:
            cor = pred == label
            print("是否答对：", cor)
            with open(logfile, 'a', encoding='utf8') as f:
                f.write("是否答对："+str(cor)+"\n")
            cors.append(cor)
            preds.append(pred+"|||"+label+"|||"+str(cor))

            #labels.append(label)
        except Exception as e:
            print(e)

    acc = np.mean(cors)

    acc_info = "Average accuracy {:.3f} - {}".format(acc, subject)
    print(acc_info)

    preds.append(acc_info)

    preds = [x+"\n" for x in preds]

    return preds

def main(args):
    subjects = sorted([f.split(".xlsx")[0] for f in os.listdir(os.path.join(args.data_dir, "test")) if ".xlsx" in f])
    if not os.path.exists(args.save_dir):
        os.mkdir(args.save_dir)

    print("subjects:", subjects)
    print("args", args)

    for subject in subjects:
        if subject != "医疗":
            dev_df = pd.read_excel(os.path.join(args.data_dir, "dev", subject + ".xlsx"), header=0)[:args.ntrain]
            test_df = pd.read_excel(os.path.join(args.data_dir, "test", subject + ".xlsx"), header=0)
            preds = eval(args, subject, dev_df, test_df)
            writelines_to_file(os.path.join(args.save_dir, subject), preds)

        else:
            dev_df = pd.read_excel(os.path.join(args.data_dir, "dev", subject + ".xlsx"), header=0)[:args.ntrain]
            f = pd.ExcelFile(os.path.join(args.data_dir, "test", subject + ".xlsx"))
            sheet_list = f.sheet_names
            for sheet in sheet_list:
                test_df = pd.read_excel(os.path.join(args.data_dir, "test", subject + ".xlsx"), header=0, sheet_name=sheet)
                preds = eval(args, sheet, dev_df, test_df)
                writelines_to_file(os.path.join(args.save_dir, sheet), preds)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ntrain", "-k", type=int, default=5)
    parser.add_argument("--data_dir", "-d", type=str, default="data")
    parser.add_argument("--save_dir", "-s", type=str, default="results")

    args = parser.parse_args()
    main(args)
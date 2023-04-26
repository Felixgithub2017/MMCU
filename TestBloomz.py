import argparse
import os
import numpy as np
import pandas as pd
import time

import torch
from transformers import  AutoTokenizer, BloomForCausalLM, GenerationConfig

tokenizer = AutoTokenizer.from_pretrained('bigscience/bloom')

BASE_MODEL = "/media/user/80EADB63EADB53CE/bloom_lora_model/bloomz_560m"
#BASE_MODEL = "/media/user/80EADB63EADB53CE/bloom_lora_model/bloomz_1b1"
#BASE_MODEL = "/media/user/80EADB63EADB53CE/bloom_lora_model/bloomz_3b"
#BASE_MODEL = "/media/user/80EADB63EADB53CE/bloom_lora_model/bloomz_7b1_mt"

device = "cuda"

model = BloomForCausalLM.from_pretrained(
        BASE_MODEL,
        #load_in_8bit=True,
        torch_dtype=torch.float16,
        device_map={'': 1}, # original  device_map="auto"
    )

model.eval()

choices = ["A", "B", "C", "D"]

def softmax(x):
    z = x - max(x)
    numerator = np.exp(z)
    denominator = np.sum(numerator)
    softmax = numerator/denominator
    return softmax

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
            prompt += "\n{}. {}".format(choices[j], df.iloc[idx, j+1].replace("A、", "").replace("B、", "").replace("C、", "").replace("D、", "").replace("A.", "").replace("B.", "").replace("C.", "").replace("D.", "").replace("A", "").replace("B", "").replace("C", "").replace("D", "").replace("Ａ、", "").replace("Ｂ、", "").replace("Ｃ、", "").replace("Ｄ、", "").strip())
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
    prompt = "请阅读以下选择题并给出正确选项，不要解释原因。请只给出答案的序号。\n"
    if k == -1:
        k = train_df.shape[0]
    for i in range(k):
        prompt += format_example(train_df, i)
    
    return prompt

# bloomz
def plain_chat(
    prompt,
    input=None,
    temperature=0.7,
    top_p=0.75,
    top_k=40,
    num_beams=4,
    max_new_tokens=512,
    **kwargs,
):
    #print("prompt:", prompt)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=max_new_tokens,
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.replace(prompt, "").replace("</s>", "").strip()

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
    logfile = "bloomztestlogfile"
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
                print("模型预测答案:", pred)
                preds.append(pred)
                with open(logfile, 'a', encoding='utf8') as f:
                    f.write("模型预测答案:"+pred+"\n")
                break
            except Exception as e:
                print(e)
                print("pausing")
                time.sleep(10)
                continue

        try:
            #cor = pred == label
            if label in pred:
                cor = True
            else:
                cor = False
            print("是否答对：", cor)
            with open(logfile, 'a', encoding='utf8') as f:
                f.write("是否答对："+str(cor)+"\n")
            cors.append(cor)

            #labels.append(label)
        except Exception as e:
            print(e)

        '''if i>=5:
            break # test'''

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

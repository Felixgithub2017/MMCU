# MMCU

This is the code repository for paper Measuring Massive Multitask Chinese Understanding https://arxiv.org/abs/2304.12986

Please send us an email to apply for free dataset download: order@besteasy.com
You may need to clarify your identity (Professor, College Students, NLP researcher/engineer, etc.)<br>
For academic exchanges, please contact me at felix.zeng@besteasy.com

## 重要声明

本评测只是对大模型语义理解能力的测试，并不能代表模型的全面能力评测，评测结果仅供参考。整个评测方式、评测数据集、评测记录都公开，确保可以复现。


## 评测结果
### 四大领域平均分数<br>
|       | zero-shot | bloomz_560m | bloomz_1b1 | bloomz_3b | bloomz_7b1_mt | ChatGLM 6B | MOSS 16B | GPT-3.5-turbo |
|-------|-----------|-------------|------------|-----------|---------------|------------|----------|---------------|
| 医疗  | 0.298     | 0.213       | 0.374      | 0.364     | 0.338         | 0.234      | 0.512    | 
| 法律  | 0.163     | 0.14        | 0.18       | 0.174     | 0.169         | 0.133      | 0.239    |
| 心理学| 0.201     | 0.187       | 0.319      | 0.346     | 0.288         | 0.211      | 0.447    |
| 教育  | 0.247     | 0.275       | 0.315      | 0.316     | 0.333         | 0.253      | 0.455    |
| 平均  | 0.22725   | 0.20375     | 0.297      | 0.3       | 0.282         | 0.20775    | 0.41325  |

![image](https://github.com/Felixgithub2017/MMCU/assets/26135691/c1a798ab-3102-4c3b-83e4-c0df3e517ea4)

### 医疗领域分数<br>
![image](https://github.com/Felixgithub2017/MMCU/assets/26135691/547a7901-c403-4406-8361-d04b189437d1)

### 教育领域分数<br>
![image](https://github.com/Felixgithub2017/MMCU/assets/26135691/93b608ac-e5fe-42d1-9b3c-97f8b21c0feb)


## Updates
### 2023.5.13<br>
2023.5.13至2023.5.15之间对所有模型进行了重新评测，结果均上传至 test_results 文件夹，公开可见。<br>

### 2023.5.13<br>
2023.5.13之前拿到数据集的研究者需要手动添加以下问题的答案<br>
心理学 306 题  缺失答案 答案应为  B<br>
随年龄增长，个体的快速眼动睡眠量怎么变化？	A.越来越多	B.越来越少	C.呈 U 型变化	D.呈倒 U 型变化<br>

传染病学 126 题  缺失答案  答案应为A<br> 
新生儿预防乙型肝炎的最好措施是：	A.出生24小时内立即接种基因重组乙型肝炎疫苗	B.出生立即注射乙肝免疫球蛋白	C.尽早注射丙种球蛋白	D.注射人血清和胎盘球蛋白<br>    

传染病学 155 题 缺失答案 答案应为C<br>
孕妇于妊娠早期患重型病毒性肝炎，正确的处理应是：	A.积极治疗重型肝炎，病情不见好转行人工流产术	B.立即行人工流产术	C.治疗肝炎，待病情好转行人工流产术	D.治疗肝炎同时行人工流产术<br> 

### 2023.5.12<br>
1.修正模型预测答案匹配方法，更好地抽取多选题预测答案<br>
2.将某些题目正确答案中的特殊字符 ＡＢＣＤ 修正为正常字符 A B C D<br>
3.评测结果文件更加直观，采用以下形式记录，第一列为模型预测答案，第二列为标准答案，第三列记录是否答对<br>
ABD|||ABCD|||False<br>
C|||BD|||False<br>
ACD|||ABD|||False<br>
BCD|||BCD|||True<br>


## Usage

--ntrain 0: do not provide examples<br>
--ntrain 5: provide five examples<br>

zero-shot test for chatgpt
```python
python TestChatGPT.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
```

few-shot test for chatgpt
```python
python TestChatGPT.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
```

zero-shot test for bloomz
```python
python TestBloomz.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```
 
few-shot test for bloomz
```python
python TestBloomz.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```

zero-shot test for chatglm
```python
python TestChatGLM.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```

few-shot test for chatglm
```python
python TestChatGLM.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```

zero-shot test for MOSS
```python
python TestMOSS.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```
 
few-shot test for MOSS
```python
python TestMOSS.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 ```

## Cite
If you find the code and testset are useful in your research, please consider citing

@misc{zeng2023measuring,
      title={Measuring Massive Multitask Chinese Understanding}, 
      author={Hui Zeng},
      year={2023},
      eprint={2304.12986},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

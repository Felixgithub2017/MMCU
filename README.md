# MMCU

This is the code repository for paper Measuring Massive Multitask Chinese Understanding https://arxiv.org/abs/2304.12986

Please send us an email to apply for free dataset download: order@besteasy.com
You may need to clarify your identity (Professor, College Students, NLP researcher/engineer, etc.)<br>
For academic exchanges, please contact me at felix.zeng@besteasy.com

## 重要声明

本评测只是对大模型语义理解能力的测试，并不能代表模型的全面能力评测，评测结果仅供参考。整个评测方式、评测数据集、评测记录都公开，确保可以复现。


## 评测结果
### 四大领域平均分数<br>
| zero-shot | bloomz_560m | bloomz_1b1 | bloomz_3b | bloomz_7b1_mt | ChatGLM 6B | MOSS 16B | GPT-3.5-turbo |
|-----------|-------------|------------|-----------|---------------|------------|----------|---------------|
| 医疗  | 0.298     | 0.213       | 0.374      | 0.364     | 0.338         | 0.234      | 0.512    | 
| 法律  | 0.163     | 0.14        | 0.18       | 0.174     | 0.169         | 0.133      | 0.239    |
| 心理学| 0.201     | 0.187       | 0.319      | 0.346     | 0.288         | 0.211      | 0.447    |
| 教育  | 0.247     | 0.275       | 0.315      | 0.316     | 0.333         | 0.253      | 0.455    |
| 平均  | 0.22725   | 0.20375     | 0.297      | 0.3       | 0.282         | 0.20775    | 0.41325  |

### 医疗领域分数<br>
| zero-shot | bloomz_560m | bloomz_1b1 | bloomz_3b | bloomz_7b1_mt | ChatGLM6B | MOSS 16B | GPT-3.5-turbo |
|-----------|-------------|------------|-----------|---------------|-----------|----------|---------------|
| 医学三基  | 0.311     | 0.274       | 0.375      | 0.415     | 0.371         | 0.231     | 0.552    |
| 药理学   | 0.265     | 0.235       | 0.38       | 0.36      | 0.255         | 0.285     | 0.52     |
| 护理学   | 0.33      | 0.278       | 0.372      | 0.368     | 0.339         | 0.238     | 0.516    |
| 病理学   | 0.312     | 0.267       | 0.392      | 0.341     | 0.358         | 0.278     | 0.506    |
| 临床医学  | 0.347     | 0.198       | 0.426      | 0.554     | 0.455         | 0.317     | 0.693    |
| 传染病学  | 0.295     | 0.242       | 0.398      | 0.46      | 0.401         | 0.254     | 0.587    |
| 外科学    | 0.365     | 0.251       | 0.397      | 0.374     | 0.361         | 0.279     | 0.525    |
| 解剖学   | 0.182     | 0.136       | 0.227      | 0.227     | 0.273         | 0.136     | 0.5      |
| 医学影像学 | 0.45      | 0.05        | 0.6        | 0.45      | 0.35          | 0.25      | 0.55     |
| 寄生虫学  | 0.33      | 0.24        | 0.39       | 0.25      | 0.33          | 0.18      | 0.43     |
| 免疫学   | 0.282     | 0.147       | 0.331      | 0.344     | 0.319         | 0.178     | 0.515    |
| 儿科学   | 0.39      | 0.258       | 0.385      | 0.38      | 0.399         | 0.263     | 0.54     |
| 皮肤性病学 | 0.255     | 0.255       | 0.392      | 0.51      | 0.471         | 0.275     | 0.627    |
| 组织胚胎学 | 0.058     | 0.13      | 0.208       | 0.188      | 0.149         | 0.143     | 0.364    |
| 药物分析学 | 0.292     | 0.236      | 0.333       | 0.236      | 0.236         | 0.208     | 0.25    |
| 医疗平均分 | 0.2976     | 0.213133333      | 0.373733333       | 0.3638      | 0.3378         | 0.234333333     | 0.511666667    |

### 教育领域分数<br>
| zero-shot | bloomz_560m | bloomz_1b1 | bloomz_3b | bloomz_7b1_mt | ChatGLM6B | MOSS 16B | GPT-3.5-turbo |
|-----------|-------------|------------|-----------|---------------|-----------|----------|---------------|
| 语文  | 0.233     | 0.283       | 0.248      | 0.205     | 0.256         | 0.233     | 0.31     |
| 数学  | 0.251     | 0.257       | 0.281      | 0.325     | 0.307         | 0.257     | 0.427    |
| 物理  | 0.173     | 0.208       | 0.185      | 0.202     | 0.256         | 0.208     | 0.327    |
| 化学  | 0.28      | 0.34        | 0.28       | 0.14      | 0.3           | 0.28      | 0.44     |
| 政治  | 0.239     | 0.255       | 0.329      | 0.401     | 0.329         | 0.268     | 0.545    |
| 历史  | 0.279     | 0.296       | 0.421      | 0.432     | 0.448         | 0.245     | 0.513    |
| 地理  | 0.255     | 0.271       | 0.336      | 0.411     | 0.346         | 0.284     | 0.478    |
| 生物  | 0.262     | 0.287       | 0.443      | 0.414     | 0.422         | 0.245     | 0.599    |
| 平均  | 0.2465    | 0.274625    | 0.315375   | 0.31625   | 0.333         | 0.2525    | 0.454875 |

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

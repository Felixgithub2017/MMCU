# MMCU

This is the code repository for paper Measuring Massive Multitask Chinese Understanding https://arxiv.org/abs/2304.12986

Please send us an email to apply for free dataset download: order@besteasy.com
You may need to clarify your identity (Professor, College Students, NLP researcher/engineer, etc.)<br>
For academic exchanges, please contact me at felix.zeng@besteasy.com

# 重要声明

本评测只是对大模型语义理解能力的测试，并不能代表模型的全面能力评测，评测结果仅供参考。整个评测方式、评测数据集、评测记录都公开，确保可以复现。

# Updates
2023.5.12<br>
1.修正模型预测答案匹配方法，更好地抽取多选题预测答案<br>
2.将某些题目正确答案中的 ＡＢＣＤ 修正为 A B C D<br>
3.评测结果文件更加直观，采用以下形式记录，第一列为模型预测答案，第二列为标准答案，第三列记录是否答对<br>

ABD|||ABCD|||False<br>
C|||BD|||False<br>
ACD|||ABD|||False<br>
BCD|||BCD|||True<br>


# Usage

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

# Cite
If you find the code and testset are useful in your research, please consider citing

@misc{zeng2023measuring,
      title={Measuring Massive Multitask Chinese Understanding}, 
      author={Hui Zeng},
      year={2023},
      eprint={2304.12986},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

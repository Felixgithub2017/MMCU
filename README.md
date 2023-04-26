# MMCU

This is the code repository for paper Measuring Massive Multitask Chinese Understanding https://arxiv.org/abs/2304.12986

Please send us an email to apply for free dataset download: order@besteasy.com
You may need to clarify your identity (Professor, College Students, NLP researcher/engineer, etc.)

# Usage

--ntrain 0: do not provide examples
--ntrain 5: provide five examples

## zero-shot test for chatgpt
python FelixTestChatGPT.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

## few-shot test for chatgpt
python FelixTestChatGPT.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

## zero-shot test for bloomz
python FelixTestBloomz.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 
## few-shot test for bloomz
python FelixTestBloomz.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

## zero-shot test for chatglm
python FelixTestChatGLM.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

## few-shot test for chatglm
python FelixTestChatGLM.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

## zero-shot test for MOSS
python FelixTestMOSS.py \
 --ntrain 0  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results
 
## few-shot test for MOSS
python FelixTestMOSS.py \
 --ntrain 5  \
 --data_dir MMCU_dataset_path  \
 --save_dir path_for_test_results

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

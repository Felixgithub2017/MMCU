# MMCU
MEASURING MASSIVE MULTITASK CHINESE UNDERSTANDING

Please send us an email to apply for free dataset download: order@besteasy.com
You may need to clarify your identity (Professor, College Students, NLP researcher/engineer, etc.)

# Usage

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

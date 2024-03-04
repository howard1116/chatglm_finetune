# chatglm_finetune

此为项目[https://github.com/HarderThenHarder/transformers_tasks/tree/main/LLM/chatglm_finetune](https://github.com/HarderThenHarder/transformers_tasks/tree/main/LLM/chatglm_finetune)的复制（手动复制，不是fork），原readme见[readme_official.md](readme_official.md)

This is a copy from [https://github.com/HarderThenHarder/transformers_tasks/tree/main/LLM/chatglm_finetune](https://github.com/HarderThenHarder/transformers_tasks/tree/main/LLM/chatglm_finetune) (I copy it manually, not from 'fork'), and official readme is [here](readme_official.md)

## 建立环境

```sh
conda create -n llm_env python=3.8
conda activate llm_env
pip install -r requirements.txt
cd peft-chatglm
python setup.py install
cd ..
```

## 下载数据

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/THUDM/chatglm-6b
cd chatglm-6b
# https://cloud.tsinghua.edu.cn/d/fb9f16d6dc8f482596c2/
```

## LoRA Finetune（占显存，不用）

```sh
python train.py `
    --train_path data/mixed_train_dataset.jsonl `
    --dev_path data/mixed_dev_dataset.jsonl `
    --use_lora True `
    --lora_rank 8 `
    --batch_size 1 `
    --num_train_epochs 2 `
    --save_freq 1000 `
    --learning_rate 3e-5 `
    --logging_steps 100 `
    --max_source_seq_len 400 `
    --max_target_seq_len 100 `
    --save_dir checkpoints/finetune `
    --img_log_dir "log" `
    --img_log_name "ChatGLM Fine-Tune" `
    --device cuda:0
```

## P-Tuning

```sh
python train.py `
    --train_path data/mixed_train_dataset.jsonl `
    --dev_path data/mixed_dev_dataset.jsonl `
    --use_ptuning True `
    --pre_seq_len 128 `
    --batch_size 1 `
    --num_train_epochs 1 `
    --save_freq 900 `
    --learning_rate 2e-4 `
    --logging_steps 100 `
    --max_source_seq_len 400 `
    --max_target_seq_len 100 `
    --save_dir checkpoints/ptuning `
    --img_log_dir "log" `
    --img_log_name "ChatGLM P-Tuning" `
    --device cuda:0
```

## streamlit网页打开

```sh
streamlit run playground_local.py --server.port 8001
```
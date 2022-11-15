
#--model_name_or_path /data/nlp/pre_models/torch/bert/bert-base-chinese \
#--max_epochs 5 \
#--max_steps 100000 \
python ../train.py \
--device '0' \
--data_backend 'leveldb' \
--model_type gpt2 \
--tokenizer_name /data/nlp/pre_models/torch/bert/bert-base-chinese \
--config_name ../config/config.json \
--train_file /data/nlp/nlp_train_data/thucnews/train.json \
--do_train \
--max_steps 100000 \
--train_batch_size 8 \
--test_batch_size 2 \
--adam_epsilon 1e-8 \
--gradient_accumulation_steps 1 \
--max_grad_norm 1.0 \
--weight_decay 0 \
--warmup_steps 0 \
--output_dir './output' \
--max_seq_length 512 \
--title_max_len 50


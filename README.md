
## transformer is all you need.
- 基于pytorch-lightning 和 transformers实现的上下游训练框架

## 例子
  -  [deep_training-examples](https://github.com/ssbuild/deep_training-example)

## 更新
- <strong>2023年01月09</strong>
  - 增加infonce对比学习,SPN4RE关系模型抽取
- <strong>2023年01月06</strong>
  - 增加onerel关系模型抽取，prgc关系模型抽取，pure实体模型提取
- <strong>2022年12月24</strong>
  - 增加unilm模型蒸馏和事件抽取模型
- <strong>2022年12月16</strong>
  - crf_cascad crf级联抽取实体
  - span ner 可重叠多标签，非重叠多标签两种实现方式抽取实体
  - mhs_ner 多头选择实体抽取模型
  - w2ner 实体抽取模型
  - tplinkerplus 实体抽取
  - tpliner 关系抽取模型
  - tplinkerplus 关系抽取模型
  - mhslinker 多头选择关系抽取模型

- <strong>2022年11月17</strong>: 
  - simcse-unilm 系列
  - simcse-bert-wwm 系列 
  - tnews circle loss
  - afqmc siamese net similar
- <strong>2022年11月15</strong>: 
  - unilm autotitle seq2seq autotitle
  - 普通分类,指针提取命名实体,crf提取命名实体
  - prefixtuning 分类 , prefixtuning 分类 , prefixtuning 指针提取命名实体 , prefixtuning crf 提取命名实体
- <strong>2022年11月12</strong>: 
  - gplinker (全局指针提取)
  - casrel (A Novel Cascade Binary Tagging Framework for Relational Triple Extraction 参考 https://github.com/weizhepei/CasRel)
  - spliner (指针提取关系 sigmoid pointer or simple pointer)
- <strong>2022年11月11</strong>: 
  - cluener_pointer 中文命名实体提取 和 cluener crf 中文命名实体提取
  - tnews 中文分类
- <strong>2022年11月06</strong>: 
  - mlm,gpt2,t5等模型预训练任务



## 支持任务
- <strong>预训练</strong>:
  - <strong> 数据参考 </strong> [THUCNews新闻文本分类数据集的子集](https://pan.baidu.com/s/1eS-QZpWbWfKtdQE4uvzBrA?pwd=1234)
  - <strong>mlm预训练</strong>例子 bert roberta等一些列中文预训练 
  - <strong>lm预训练</strong>例子 gpt2等一些列中文预训练 
  - <strong>seq2seq 预训练</strong>例子 t5 small等一些列中文预训练 &nbsp;&nbsp;
  - <strong>unilm 预训练</strong>例子 unilm bert roberta 等一些列中文预训练 &nbsp;&nbsp
- <strong>中文分类</strong>:
  - 例子 <strong>tnews 中文分类</strong>
- <strong>命名实体提取</strong>: 
  -  <strong>参考数据</strong>  cluner
  -  <strong>cluener 全局指针提取</strong>
  -  <strong>cluener crf提取</strong>
  -  <strong>cluener crf prompt提取</strong>
  -  <strong>cluener mhs ner多头选择提取</strong>
  -  <strong>cluener span指针提取</strong>
  -  <strong>cluener crf 级联提取</strong>
  -  <strong>cluener tplinkerplus 提取</strong>
  -  <strong>cluener w2ner 提取</strong>
- <strong>关系提取</strong>
  - <strong>参考数据</strong>  [duie和法研杯第一阶段数据](https://github.com/ssbuild/cail2022-info-extract)
  - <strong>gplinker 关系提取</strong>
  - <strong>casrel 关系提取</strong>
  - <strong>spliner 关系提取</strong>
  - <strong>mhslinker 关系提取</strong>
  - <strong>tplinker 关系提取</strong>
  - <strong>tplinkerplus 关系提取</strong>
- <strong>事件提取</strong>
  - <strong>参考数据</strong> duee事件抽取 [DuEE v1.0数据集](https://aistudio.baidu.com/aistudio/competition/detail/46/0/datasets)
  - <strong>gplinker 事件提取</strong>
- <strong> prompt 系列</strong>: 
  - 例子 <strong>prefixprompt tnews中文分类</strong>
  - 例子 <strong>prefixtuning tnews 中文分类</strong>
  - 例子 <strong>prefixtuning cluener 命名实体全局指针提取</strong>
  - 例子 <strong>prefixtuning cluener 命名实体crf提取</strong>
  - 例子 <strong>prompt mlm 自行构建数据模板集，训练参考 pretrain/mlm_pretrain</strong>
  - 例子 <strong>prompt lm  自行构建数据模板集，训练参考 pretrain/seq2seq_pretrain ,  pretrain/lm_pretrain</strong>
- <strong> simcse 系列</strong>: 
  - <strong>simcse-unilm 系列</strong>  例子 unilm+simce  &nbsp;&nbsp; 
  参考数据&nbsp;&nbsp; [THUCNews新闻文本分类数据集的子集](https://pan.baidu.com/s/1eS-QZpWbWfKtdQE4uvzBrA?pwd=1234)
  - <strong>simcse-bert-wwm 系列</strong> 例子 mlm+simcse &nbsp;&nbsp;
  参考数据&nbsp;&nbsp; [THUCNews新闻文本分类数据集的子集](https://pan.baidu.com/s/1eS-QZpWbWfKtdQE4uvzBrA?pwd=1234)
- <strong> sentense embeding</strong>: 
  - <strong>circle loss </strong> 例子 tnews circle loss
  - <strong>siamese net </strong> 例子 afqmc siamese net similar

  
## 愿景
创建一个模型工厂, 轻量且高效的训练程序，让训练模型更容易,更轻松上手。

## 交流
QQ交流群：185144988

# -*- coding: utf-8 -*-
# @Time    : 2022/11/15 13:33
import random
import typing

from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup


def configure_optimizers(model_attrs: typing.Union[typing.List,typing.Tuple],
                         hparams: typing.Dict,
                         estimated_stepping_batches: int):

    no_decay = ["bias", "LayerNorm.weight"]
    opt = []
    for a, lr in model_attrs:
        opt += [
            {
                "params": [p for n, p in a.named_parameters() if not any(nd in n for nd in no_decay)],
                "weight_decay": hparams.training_args.weight_decay, "lr": lr,
            },
            {
                "params": [p for n, p in a.named_parameters() if any(nd in n for nd in no_decay)],
                "weight_decay": 0.0, "lr": lr,
            },
        ]

    optimizer = AdamW(opt, lr=hparams.training_args.learning_rate, eps=hparams.training_args.adam_epsilon)
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=hparams.training_args.warmup_steps,
        num_training_steps=estimated_stepping_batches
        # num_training_steps=self.trainer.estimated_stepping_batches,
    )
    scheduler = {"scheduler": scheduler, "interval": "step", "frequency": 1}
    return [optimizer], [scheduler]



def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str =''
    base_str ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length =len(base_str) -1
    for i in range(randomlength):
        random_str +=base_str[random.randint(0, length)]
    return random_str



class InheritBlockMeta(type):
    def __new__(cls, name,bases, attr,*args,**kwargs):
        if kwargs.get('__inherit',False):
            return super(InheritBlockMeta, cls).__new__(cls, name, bases, attr)
        if any(tuple(True for b in bases if issubclass(b,ClassUnBlock))):
            return super(InheritBlockMeta, cls).__new__(cls, name, bases, attr)
        return super(InheritBlockMeta, cls).__new__(cls, name,() if any(tuple(True for b in bases if str(b).endswith('__.ClassBlock\'>'))) else bases, attr)

class ClassUnBlock(metaclass=InheritBlockMeta,__inherit=True):...
class ClassBlock(metaclass=InheritBlockMeta,__inherit=False):...


def block_class(className):
    return type('BC' + generate_random_str(12), (className, ClassBlock,), dict(__MODEL_CLASS__ = className))




class ExceptClassMeta(type):
    def __new__(cls, name,bases,attr,*args,**kwargs):
        excepts = kwargs.pop('excepts',None)
        return super(ExceptClassMeta, cls).__new__(cls, name,tuple(_ for _ in bases if not str(_).endswith('__.{}\'>'.format(excepts))) if excepts is not None else bases,attr)

class ExceptCLASS(metaclass=ExceptClassMeta):...

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 09:24:16 2018

@author: DataAnt
"""
import pandas as pd
import os
from pypinyin import lazy_pinyin, Style

rpath = os.getcwd()
idioms = pd.read_excel(os.path.join(rpath, 'idioms_pinyin.xlsx'))
idioms['pinyin'] = idioms['pinyin'].map(eval)
idioms['pinyin_tone'] = idioms['pinyin_tone'].map(eval)


def get_pinyin(word, tone=False):
    if tone:
        py = lazy_pinyin(word, style=Style.TONE3)
        col = 'pinyin_tone'
    else:
        py = lazy_pinyin(word)
        col = 'pinyin'
    return py, col


def judge(py, col):
    # 返回两个set的交集长度
    func = lambda x:len(set(py).intersection(set(x)))
    # copy数据框idioms
    df = idioms.copy()
    # 交集长度
    df['inter_length'] = df[col].map(func)
    # 筛选交集长度大于0的记录
    df = df[df['inter_length'] > 0]
    #df = df.sort_values('inter_length', ascending=False)
    return df


def _replace(ser, py, col, word):
    ser['new_idiom'] = ser['idiom']
    for w, c in zip(word, py):
        if c in ser[col]:
            # 拼音相同的字的位置
            i = ser[col].index(c)
            # 要替换的汉字
            rw = ser['idiom'][i]
            # 替换
            ser['new_idiom'] = ser['new_idiom'].replace(rw, w)
    return ser
            

def diff_num(word1, word2):
    '''比较相同长度的两个字符串中不同的字符数'''
    num = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                num += 1
        return num
    else:
        raise ValueError('两个字符串长度不一致！')
        

def new_idiom(word):
    '''
    返回返回一个DataFrame，包含两个字段,idiom为成语原词，new_idiom为关键字谐音替换后的新成语
    :word: str类型，关键词
    '''
    py, col = get_pinyin(word, tone=True)
    df = judge(py, col)
    func = lambda x:_replace(x, py, col, word)
    df = df.apply(func, axis=1)
    # 生成的广告标题改动的字数
    df['diff_num'] = df.apply(lambda x:diff_num(x['idiom'], x['new_idiom']), axis=1)
    # 排序
    df = df.sort_values(by=['inter_length', 'diff_num'], ascending=[False, False])
    df = df[['idiom', 'new_idiom']]
    return df

if __name__ == '__main__':
    df = new_idiom('割韭菜')
    





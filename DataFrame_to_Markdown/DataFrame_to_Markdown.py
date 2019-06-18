# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:50:43 2018

@author: DataAnt
"""
import pandas as pd


def switch(df: pd.DataFrame) -> str:
    # 把所有的数据转为字符类型
    df = df.astype(str)
    # 把表头和短横线插入到df中
    cols = df.columns.tolist()
    lines = ['---'] * len(cols)
    head = pd.DataFrame([cols, lines], columns=df.columns)
    df = pd.concat([head, df], ignore_index=True)
    
    # 表中所有单元格的字符长度
    df_len = df.applymap(len)
    # 表格每列的字符长度
    lens = df_len.max().astype(int).tolist()
    # 创建一个DataFrame，存储df中每个单元格字符应该调整到的长度
    df_len_max = pd.DataFrame([lens] * len(df), index=df.index, columns=df.columns)
    # 根据df_len_max中的长度调整df中的长度
    center = lambda x1, x2: x1.center(x2)
    temp = df.combine(df_len_max, lambda s1, s2: s1.combine(s2, center))
    
    
    def concat(ser:pd.Series) -> str:
        '''
        用‘|’连接Series中的元素
        '''
        string = '|'.join(ser)
        string = '|' + string + '|'
        return string
    
    
    # 调用concat函数连接所有字符，得到字符串table
    ser_table = temp.apply(concat, axis=1)
    table = '\n'.join(ser_table)
    return table


if __name__ == '__main__':   
    df = pd.DataFrame({'A': range(10), 'B': [chr(i) for i in range(97, 107)]})
    table = switch(df)
    print(table)



作用
---
将一个指定的DataFrame转换成用Markdown语法描述的表格

例子
---
```py
import pandas as pd
df = pd.DataFrame({'A': range(10), 'B': [chr(i) for i in range(97, 107)]})
table = switch(df)
print(table)

| A | B |
|---|---|
| 0 | a |
| 1 | b |
| 2 | c |
| 3 | d |
| 4 | e |
| 5 | f |
| 6 | g |
| 7 | h |
| 8 | i |
| 9 | j |
```
将上述代码中的table字符串内容粘贴到Markdown文件中，可得到如下表格

| A | B |
|---|---|
| 0 | a |
| 1 | b |
| 2 | c |
| 3 | d |
| 4 | e |
| 5 | f |
| 6 | g |
| 7 | h |
| 8 | i |
| 9 | j |

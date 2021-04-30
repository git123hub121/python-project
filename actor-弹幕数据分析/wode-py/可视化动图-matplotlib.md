

```python
import pandas as pd
df = pd.read_csv('D:/Python/Mypython/python项目集锦/actor-弹幕数据分析/df_resuluts.csv',engine='python',encoding='utf-8')
df.head(5)
```


```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
#显示中文（可能还会显示不了，请自行百度解决中文问题）
plt.rcParams['font.sans-serif']=['SimHei']

df2 = df[['name', '2020-09-28']].sort_values(by='2020-09-28', ascending=False).head(10)#内嵌一个列表实现取两列，温习
df2.sort_values(by='2020-09-28', ascending=True, inplace=True)
df2#为了条形图做准备
```


```python
fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(df2['name'], df2['2020-09-28'])
```


```python
colors = ['#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', 
         '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50',
         '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50',
         '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50',
         '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50',
          '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50',
          '#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff']

#给每个国家随机分配颜色
namecolors = dict()
names = set(df['name'])
for color, name in zip(colors, names):#多个序列(列表，元组，集合)同时遍历，使用zip()方法，这里很高级哦！
    namecolors[name] = color
    
namecolors
```


```python
fig, ax = plt.subplots(figsize=(15, 8))
#排名前10的国家
ax.barh(df2['name'], df2['2020-09-28'], color=[namecolors[c] for c in df2['name']])
for i, (value, name) in enumerate(zip(df2['2020-09-28'], df2['name'])):
        ax.text(value, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
ax.text(1, 0.45, '2020-09-28', transform=ax.transAxes, size=46, ha='right')
```


```python
list(df)
```


```python
#data = [i for i in df[1:]][1:]#瞎猫碰上死耗子了
#取出列名的几种方法之一
data = list(df)[1:] 
@datadata
```


```python
fig, ax = plt.subplots(figsize=(15, 8))

def draw_barchart(date):
    #整理数据
    date = str(date)
    df2 = df[['name', date]].sort_values(by=date, ascending=False).head(10)
    df2.sort_values(by=date, ascending=True, inplace=True)
    
    #横向条形图
    ax.clear()
    ax.barh(df2['name'], df2[date], color=[namecolors[name] for name in df2['name']])
    dx = df[date].max()/200
    
    for i, (value, name) in enumerate(zip(df2[date], df2['name'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
        
        
    #细节修饰
    ax.text(1, 0.45, date, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'y轴标题', transform=ax.transAxes, size=12, color='#777777')
    
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)

    
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0.3, 1.05, '总标题',
           transform=ax.transAxes, size=24, weight=600, ha='left')
    
    plt.box(False)
    
#  for i in range(39):
draw_barchart(data[0])
```


```python
import matplotlib.animation as animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=[data[i] for i in range(39)])
HTML(animator.to_jshtml())
```


```python
#保存为gif
#animator.save('resetvalue.gif', writer='imagemagick')
#animator.save('crap.gif', writer='imagemagick',  savefig_kwargs={'facecolor':'white'}, fps=1)
```


```python
# 如何保存为视频
animator.to_html5_video()
#animator.save('countryflys1.mp4')
```

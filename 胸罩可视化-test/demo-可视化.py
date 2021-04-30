import pandas as pd
#读取数据
df = pd.read_excel('D:\\Python\\数据可视化演示\\taobao_goods.xlsx')
# print(df)
#数据清洗
df.drop_duplicates(inplace=True)#去除完全重复的行数据
# print(df)
location_list = []
for location in df['location']:
    location_list.append(location.split(' ')[0])
df['location'] = location_list
# print(df)
sales_list = []
for sale in df['sales']:
    sale = sale[:-3].replace('+','')
    if '万' in sale:
        sale = int(float(sale[:-1])*10000)
    else:
        sale = int(sale)
    sales_list.append(sale)
df['sales'] = sales_list
# print(df)
#重新保存新的数据
df.to_excel('new_taobao.xlsx',index=None)#去掉索引
#提取数据
locations = [location for location in df['location'].value_counts().items()]#pandas 的 value_counts() 函数可以对Series里面的每个值进行计数并且排序(默认降序)
#item()以列表返回可遍历的(键, 值) 元组数组
# print(locations)

import jieba #分词
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar, Map, WordCloud, Page

#地图map
map = (
    Map()
    .add("店铺数量",
        [list(location) for location in locations],"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="地址分布图"),
        visualmap_opts=opts.VisualMapOpts(max_=3000),
    )
    #.render("map.html")
)
#词云--这一部分可以改一下,改成自己的pyecharts
dfc = pd.read_excel(r'D:\Python\数据可视化演示\standard_excel\standard_goods_comments.xlsx')
# print(dfc['comment'])
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
#这里用的是workcloud
#分词
text = ' '.join(jieba.cut(str([comment for comment in dfc['comment']])))
#str函数的功能 str() 函数将对象转化为适于人阅读的形式#这句话还要在思考一下下
mask = np.array(Image.open(r"D:\Python\数据可视化演示\bra.jpg"))
wc = WordCloud(mask=mask,font_path='C:\Windows\Fonts\SimHei.ttf',mode='RGBA').generate(text)
# 显示词云
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()
wc.to_file('big_cup.png')

#统计胸罩大小
sizes = [size for size in dfc['bra_size'].value_counts().items()]
total_cup = sum(count[1] for count in sizes)
print(total_cup)

#下面一脸懵逼，可以去官网找对应的图
from pyecharts.commons.utils import JsCode
fn = """
    function(params) {
        if(params.name == 'other')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """
#这个函数应该是模块里面的
def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), 
    position="center")

pie = (
    Pie()
    .add(
        "",
        [['A_cup', round(696/total_cup, 2)*100],['other',round(1 - 696/total_cup, 2)*100]],
        center=["20%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [['B_cup', round(1909/total_cup, 2)*100],['other',round(1 - 1909/total_cup, 2)*100]],
        center=["55%", "30%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [['C_cup', round(810/total_cup, 2)*100],['other',round(1 - 810/total_cup, 2)*100]],
        center=["20%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .add(
        "",
        [['D_cup', round(259/total_cup * 100, 1)],['other',round(1 - 259/total_cup, 2)*100]],
        center=["55%", "70%"],
        radius=[60, 80],
        label_opts=new_label_opts(),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Cup-多饼图"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
        ),
    )
)
pie.render_notebook()

#自动生成柱状图
from pyecharts.faker import Faker
bar = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
        datazoom_opts=[opts.DataZoomOpts()]
    )
#     .render("bar_datazoom_both.html")
)
bar.render_notebook()

#自动生成饼图
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


v = Faker.choose()
pie1 = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(v, list(range(10,80,10)))],
        radius=["30%", "75%"],
        center=["25%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add(
        "",
        [list(z) for z in zip(v,list(range(10,80,10))[::-1])],
        radius=["30%", "75%"],
        center=["75%", "50%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
)
pie1.render_notebook()

#自动读取今天的天气
from pyecharts import options as opts
from pyecharts.charts import Liquid

liquid = (
    Liquid()
    .add("lq", [0.65,0.5])	
    .set_global_opts(title_opts=opts.TitleOpts(title="今日湿度"))
)
liquid.render_notebook()

# Page.save_resize_html('page_draggable_layout.html',cfg_file= 'chart_config (1).json')
page = Page(layout=Page.DraggablePageLayout)
page.add(
bar,
liquid,
pie,
map,
pie1
)
page.render_notebook()
page.render()
Page.save_resize_html('render.html',cfg_file='D:\Python\数据可视化演示\chart_config2.json')




# a = df['location'].value_counts()
# print(a)#从数据看出，实际上是一个字典数组  Name: location, dtype: int64
# a = a.items()
# for value in a:
#     print(value)
    #一个参数，返回元组 ('广东', 2398)
    #两个参数，返回列表的输出格式 山西       1
# print(type(a))#series---数组
# for i in a:
#     print(i)#只得到了值，没有键

# for i in dfc['comment']:
#     print(i)
#i = [i for i in dfc['comment']]
#前者是将列表遍历输出  后者是将整体添加到一个列表中
#也算作一个项目了，可以学习学习
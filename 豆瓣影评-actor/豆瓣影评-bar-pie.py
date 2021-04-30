# # #柱状图————豆瓣评论层次分布
# # place_message = dfs.groupby(['评价'])
# # place_com = place_message['评价'].agg(['count'])
# # place_com.reset_index(inplace=True)
# # place_com_last = place_com.sort_index()
# # dom1 = place_com_last.sort_values('评价', ascending=True)
# # # 生成柱状图
# # v1 = list(dom1['评价'])
# # # print(v1)
# # attr = list(dom1['count'])
# # #这里只是展示出来，但是并没有添加到csv里面

# # bar = (
# #     Bar(
# #         init_opts=opts.InitOpts(theme=ThemeType.MACARONS)  # 设置主题 不知道如何添加宽高
# #     )
# #     .add_xaxis(["差评","一般","好评"])
# #     .add_yaxis("影评评价",attr)
# #         #.set_colors(["orange"])  # 柱子的颜色
# #     .set_global_opts(
# #         title_opts=opts.TitleOpts(title="影评评价",
# #                                   subtitle="",
# #                                 #   title_textstyle_opts=opts.TextStyleOpts(color='red',
# #                                 #                                               font_size=12,
# #                                 #                                               font_family='Times New Roman',
# #                                 #                                               font_weight='bold',),
# #                                   ),
# #         #图例设置
# #         legend_opts=opts.LegendOpts(
# #             pos_left='center',    # 图例放置的位置，分上下左右，可用左右中表示，也可用百分比表示
# #             pos_top='top',
# #             orient='vertical',   # horizontal、vertical #图例放置的方式 横着放or竖着放
# #             textstyle_opts=opts.TextStyleOpts(
# #                 font_size=16,
# #                 color='skyblue',
# #                 font_family='Times New Roman',
# #             ),
# #         ),
# #         yaxis_opts=opts.AxisOpts(
# #             axislabel_opts=opts.LabelOpts(
# #                 font_size=20,
# #                 font_family='Times New Roman',
# #                 color='skyblue',
# #             ),
# #         ),
# #         #显示工具栏
# #         toolbox_opts=opts.ToolboxOpts(is_show=True),
# #     )
# # )


# # bar.render('豆瓣影评评价.html')

# #pie图————豆瓣影评层次分布
# (
#     Pie(init_opts=opts.InitOpts(width="600px", height="400px", bg_color="white"))
# .add (
#         series_name="评价",
#         data_pair=data_pair,
#         radius=["40%", "55%"],
#         label_opts=opts.LabelOpts(
#             position="outside",
#             formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
#             background_color="#eee",
#             border_color="#aaa",
#             border_width=1,
#             border_radius=4,
#             rich={
#                 "a": {"color": "#999", "lineHeight": 22, "align": "center"},
#                 "abg": {
#                     "backgroundColor": "#e3e3e3",
#                     "width": "100%",
#                     "align": "right",
#                     "height": 22,
#                     "borderRadius": [4, 4, 0, 0],
#                 },
#                 "hr": {
#                     "borderColor": "#aaa",
#                     "width": "100%",
#                     "borderWidth": 0.5,
#                     "height": 0,
#                 },
#                 "b": {"fontSize": 16, "lineHeight": 33},
#                 "per": {
#                     "color": "#eee",
#                     "backgroundColor": "#334455",
#                     "padding": [2, 4],
#                     "borderRadius": 2,
#                 },
#             },
#         ),
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣评价"))
#     .render("pie_rich_label.html")
# )

#词云图————评论词分析
# #数据处理库
# import numpy as np
# import pandas as pd
# import glob
# import re
# import jieba 

# #可视化库
# import stylecloud
# import matplotlib.pyplot as plt 
# import seaborn as sns
# from pyecharts.charts import *
# from pyecharts import options as opts 
# from pyecharts.globals import ThemeType  
# from IPython.display import Image 
# # df['comment'] = df['comment'].astype('str')
# # 定义分词函数
# def get_cut_words(content_series):
#     # 读入停用词表
#     stop_words = [] 
    
#     with open("D:\Python\Mypython\python项目集锦\Python-豆瓣电影TOP250\douban_HTML\data\停用词大全.txt", 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             stop_words.append(line.strip())

#     # 添加关键词
#     my_words = ['', '']  
    
#     for i in my_words:
#         jieba.add_word(i) 

#     # 自定义停用词
#     my_stop_words = ['节目', '中国','一部']   
#     stop_words.extend(my_stop_words)               

#     # 分词
#     word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

#     # 条件筛选
#     word_num_selected = [i for i in word_num if i not in stop_words and len(i)>=2]
    
#     return word_num_selected

# # 绘制词云图
# text1 = get_cut_words(content_series=df['previews'])
# stylecloud.gen_stylecloud(text=' '.join(text1), max_words=200,
#                           collocations=False,
#                           font_path='font/字酷堂清楷体.ttf',
#                           icon_name='fas fa-video',
#                           size=653,
#                           #palette='matplotlib.Inferno_9',
#                           output_name='./1.png')
# Image(filename='./1.png') 


df4 = df3.iloc[:,8:].sum().reset_index().sort_values(0,ascending = False)
df4.columns = ['角色','次数']
df4['占比'] = df4['次数'] / df4['次数'].sum()
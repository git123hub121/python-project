import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar, Pie
import pandas as pd 
df = pd.read_csv('D:\Python\df_resuluts.csv')
x = list(df['name'])
data = []
for i in df[1:]:
    data.append(i)
data = data[1:]
datay = []
for i in range(1,40):
    datay.append(list(df.iloc[:,i]))
def get(date: int) -> Bar:
    bar = (
        Bar()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(
            series_name="弹幕探讨次数",
            y_axis=datay[date],
            label_opts=opts.LabelOpts(is_show=False),
        )
        # .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name="弹幕人物", axislabel_opts={"rotate": 60}),#
            title_opts=opts.TitleOpts(
                title="{}".format(data[date]), subtitle="人物被提及次数"
            ),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside"),],
            tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="shadow"
            ),
        )
    )
    return bar
# 生成时间轴的图
timeline = Timeline(init_opts=opts.InitOpts(width="1400px", height="600px"))

for i in range(39):
    timeline.add(get(date = i),time_point=str(data[i]))
# 1.0.0 版本的 add_schema 暂时没有补上 return self 所以只能这么写着
timeline.add_schema(is_auto_play=True, play_interval=1000,orient = "horizontal",pos_top= '-100%')#vertical
timeline.render("弹幕人物提及次数可视化.html")

#想做一个升级版的按降序排列的   #这样做不现实，即使我们可以在列表中变化，但是也会出现name不匹配的问题，那样会加大难度，现在没必要会
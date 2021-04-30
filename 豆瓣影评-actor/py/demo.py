import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import time
# #先爬取一页，首页
# url = "https://movie.douban.com/subject/35163988/comments?start=0&limit=20&status=P&sort=new_score"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
# }
# request = requests.get(url,headers=headers)
# # print(request.status_code)
# # html = requests.text 两种方法
# html = request.content.decode("utf-8")
# # print(html)
# #解析数据
# html = BeautifulSoup(html,"html.parser")
# comments = html.find_all("div",class_="comment")
# # print(comments)

ids = []
times = []
stars = []
previews = []
likes = []
for i in range(0,25):
    url = f"https://movie.douban.com/subject/35163988/comments?start={str(i*20)}&limit=20&status=P&sort=new_score"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection":"keep-alive",
        "Host":"movie.douban.com",
        "Cookie":'ll="118280"; bid=JVG-D58Gj9s; __yadk_uid=nvSxefnHcD25VBpKqzGibd14Jvo8DOYJ; _vwo_uuid_v2=DE652E69B40FE43EAB29EF14117AF8B01|b930d3c2cb075bf63b7c69a69759ad07; __utmz=30149280.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __utmz=223695111.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __gads=ID=2a953fd7603107be-223a118f58c400ce:T=1603259129:S=ALNI_MZWODSgZmy7xtPZ4TezGYTwK5cHCg; _pk_id.100001.4cf6=70b13907e7074b14.1599395136.8.1603292497.1603259129.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1603292497%2C%22http%3A%2F%2Fguozhivip.com%2Frank%2F%22%5D; __utma=30149280.38508497.1599395137.1603257834.1603292497.8; __utma=223695111.1967269573.1599395137.1603257834.1603292498.8; push_doumail_num=0; push_noty_num=0; ap_v=0,6.0; dbcl2="199068702:ZrEym3ot79Q"; ck=So_m'
    }
    request = requests.get(url,headers=headers)
    # print(request.status_code)
    # html = requests.text 两种方法
    html = request.content.decode("utf-8")
    # print(html)
    #解析数据
    html = BeautifulSoup(html,"html.parser")
    comments = html.find_all("div",class_="comment")
    # print(comments)
    for comment in comments:
        try:
            comment = str(comment).strip()
            # print(comment)
            id = re.findall(r'<a class="" href=".*?">(.*?)</a>',comment)[0]
            ids.append(id)
            time = re.findall(r'<span class="comment-time" title="(.*?)">',comment)[0]
            time = time.split(" ")[0]
            times.append(time)
            star = re.findall(r'<span class="allstar(.*?) rating" title=".*?">',comment)[0]
            stars.append(star)
            preview = re.findall(r'<span class="short">(.*?)</span>',comment)[0]
            #preview.replace("\r","").replace(" ","")#气死我了
            previews.append(preview)
            like = re.findall(r'<span class="votes vote-count">(.*?)</span>',comment)[0]
            likes.append(like)       
        except:
                pass
# print(ids)
# print(times)
# print(stars)
# print(previews)
# print(likes)
#这里有两种方法 1.用csv保存， 2.用pd保存
#1
th = ['ids','times','stars','previews','likes']
result = [ids,times,stars,previews,likes]
print(result)
# print(result[0][0])
with open("actor3.csv",'a',encoding="utf-8") as f:
    f.write(','.join(th))
    f.write("\n")
    for i in range(0,len(ids)):
        try:
            f.write(result[0][i]+","+result[1][i]+","+result[2][i]+","+result[3][i].replace("\r","").replace(" ","")+","+result[4][i])
            f.write("\n")
        except:
            pass
#pd保存
data = {
    'ids':ids,
    'time':times
}
savedata = pd.DataFrame(data=data)
print(savedata)
savedata.to_csv('1.csv',index =None)

#被限制只能爬取193条，咋办呢,但是登录可以查看后面的，---补全headers信息
#还是第一种方法好，不会报错 试试把第二种放阿飞里面的,换成/,应该是这个问题
#明天将其写成函数


import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import time


def get_url():
    page = 0
    for i in range(0, get_page):
        page += 1
        url = f"https://movie.douban.com/subject/35163988/comments?start={str(i*20)}&limit=20&status=P&sort=new_score"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Host": "movie.douban.com",
            "Cookie": 'll="118280"; bid=JVG-D58Gj9s; __yadk_uid=nvSxefnHcD25VBpKqzGibd14Jvo8DOYJ; _vwo_uuid_v2=DE652E69B40FE43EAB29EF14117AF8B01|b930d3c2cb075bf63b7c69a69759ad07; __utmz=30149280.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __utmz=223695111.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __gads=ID=2a953fd7603107be-223a118f58c400ce:T=1603259129:S=ALNI_MZWODSgZmy7xtPZ4TezGYTwK5cHCg; _pk_id.100001.4cf6=70b13907e7074b14.1599395136.8.1603292497.1603259129.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1603292497%2C%22http%3A%2F%2Fguozhivip.com%2Frank%2F%22%5D; __utma=30149280.38508497.1599395137.1603257834.1603292497.8; __utma=223695111.1967269573.1599395137.1603257834.1603292498.8; push_doumail_num=0; push_noty_num=0; ap_v=0,6.0; dbcl2="199068702:ZrEym3ot79Q"; ck=So_m'
        }
        request = requests.get(url, headers=headers)
        status = request.status_code
        if status == 200:
            print(f"第 {page} 页爬取成功   状态码 {status} 正常")
        else:
            print(f"状态码为 {status}，不正常,继续爬取...")

        html = request.content.decode("utf-8")
        # 解析数据
        html = BeautifulSoup(html, "html.parser")
        comments = html.find_all("div", class_="comment")

        # 利用re进行匹配
        for comment in comments:
            try:
                comment = str(comment).strip()
                id = re.findall(
                    r'<a class="" href=".*?">(.*?)</a>', comment)[0]
                ids.append(id)
                time = re.findall(
                    r'<span class="comment-time" title="(.*?)">', comment)[0]
                # time = time.split(" ")[0]
                times.append(time)
                star = re.findall(
                    r'<span class="allstar(.*?) rating" title=".*?">', comment)[0]
                stars.append(star)
                preview = re.findall(r'<span class="short">(.*?)</span>', comment)[0].replace(
                    "\r", "").replace("\n", "").replace(",", "，").replace(" ", "")
                previews.append(preview)
                like = re.findall(
                    r'<span class="votes vote-count">(.*?)</span>', comment)[0]
                likes.append(like)
            except:
                pass
            # print(ids)
            # print(times)
            # print(stars)
            # print(previews)
            # print(likes)
    result = [ids, times, stars, previews, likes]
    # print(result)
    return result, page
# 这里有两种方法 1.用csv保存， 2.用pd保存
# 1


def save_content(result):
    th = ['ids', 'times', 'stars', 'previews', 'likes']
    with open("actor_d1.csv", 'a', encoding="utf-8") as f:
        f.write(','.join(th))
        f.write("\n")
        count = 0
        for i in range(0, (get_page*20+1)):
            try:
                f.write(result[0][i]+","+result[1][i]+"," +
                        result[2][i]+","+result[3][i]+","+result[4][i])
                f.write("\n")
                count += 1
            except:
                pass
    return count


if __name__ == "__main__":
    # movie_id = input("请输入电影名字ID：")
    get_page = int(input("请输入你要爬去的页数："))
    ids = []
    times = []
    stars = []
    previews = []
    likes = []
    data, page = get_url()
    time.sleep(1)
    r_page = save_content(data)
    print(f"爬取完毕！理论获取{str(page*20)} 条数据,实际获取 {r_page} 条数据")
# 3
# th = ['ids','times','stars','previews','likes']
# #列表数据相加
# list_ = []
# n = 1
# for i in range(0,len(ids)):
#     try:
#         a = (ids[i]+'/'+times[i]+'/'+stars[i]+'/'+previews[i].replace("\r","").replace(" ","")+'/'+likes[i]).split('/')
#         # print(a)
#         list_.append(a)
#         print(n)
#         n += 1
#     except:
#         pass
# print(list_,n)

# if n%20 == 0:
#     time.sleep(2)
# pd.DataFrame(data=list_).to_csv('actor_pd1.csv',header=th,index=None)#出现报错


# 被限制只能爬取193条，咋办呢,但是登录可以查看后面的，---补全headers信息
# 还是第一种方法好，不会报错 试试把第二种放阿飞里面的,换成/,应该是这个问题
# 将其写成函数
# 2.同理3
# result = {'ids':ids,'times':times,'stars':stars,'previews':previews,'likes':likes}
# df= pd.DataFrame.from_dict(result, orient='index')
# comments_list = []
# comments_list.append(df)
# comments_data=pd.concat(comments_list)
# comments_data.to_csv('actor_pd.csv',index=False)
# 总之，保存为csv数据还是推荐第一种，第二种适合用来爬取。数据会有部分流失。




import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import time as t
def get_url():
    page = 0 
    datalist = []
    for i in range(0, get_page):
        page += 1
        url = f"https://movie.douban.com/subject/35163988/comments?start={str(i*20)}&limit=20&status=P&sort=new_score"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "movie.douban.com",
                "Cookie": 'll="118280"; bid=JVG-D58Gj9s; __yadk_uid=nvSxefnHcD25VBpKqzGibd14Jvo8DOYJ; _vwo_uuid_v2=DE652E69B40FE43EAB29EF14117AF8B01|b930d3c2cb075bf63b7c69a69759ad07; __utmz=30149280.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __utmz=223695111.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __gads=ID=2a953fd7603107be-223a118f58c400ce:T=1603259129:S=ALNI_MZWODSgZmy7xtPZ4TezGYTwK5cHCg; _pk_id.100001.4cf6=70b13907e7074b14.1599395136.8.1603292497.1603259129.; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1603292497%2C%22http%3A%2F%2Fguozhivip.com%2Frank%2F%22%5D; __utma=30149280.38508497.1599395137.1603257834.1603292497.8; __utma=223695111.1967269573.1599395137.1603257834.1603292498.8; push_doumail_num=0; push_noty_num=0; ap_v=0,6.0; dbcl2="199068702:ZrEym3ot79Q"; ck=So_m'
        }
        request = requests.get(url, headers=headers)
        status = request.status_code
        if status == 200:
            print(f"第 {page} 页爬取成功   状态码 {status} 正常")
        else:
            print(f"状态码为 {status}，不正常,继续爬取...")
        
        html = request.content.decode("utf-8")
        #解析数据
        html = BeautifulSoup(html, "html.parser")
        comments = html.find_all("div", class_="comment")
        
        #利用re进行匹配
        n = 0
        for comment in comments:
            try:
                id = re.compile(r'<a class="" href=".*?">(.*?)</a>')
                time = re.compile(r'<span class="comment-time" title="(.*?)">')
                star = re.compile(r'<span class="allstar(.*?) rating" title=".*?">')
                preview = re.compile(r'<span class="short">(.*?)</span>',re.S)
                like = re.compile(r'<span class="votes vote-count">(.*?)</span>')
                data = []
                comment = str(comment).strip()
                id = re.findall(id, comment)[0]
                # print(id)
                data.append(id)
                time = re.findall(time, comment)[0]
                # time = time.split(" ")[0]
                data.append(time)
                star = re.findall(star, comment)[0]
                data.append(star)
                preview = re.findall(preview, comment)[0].replace("\r","").replace(" ","").replace("\n","").replace(",","，")
                data.append(preview)
                like = re.findall(like, comment)[0]
                data.append(like)
                n += 1
                # print(n,"-",data)
                datalist.append(data)
            except:
                    pass
    return datalist,page
#1
def save_content(datalist):
    th = ['ids','times','stars','previews','likes']
    with open("actor_d.csv",'a',encoding="utf-8") as f:
        f.write(','.join(th))
        f.write("\n")
        count = 0
        for data in datalist:
            count += 1
            for i in data:
                try:
                    # ','.join(datalist[data])
                    # print(i)
                    f.write(i+",")
                except:
                    pass
            f.write("\n")
    return count
if __name__ =="__main__":
    # movie_id = input("请输入电影名字ID：")
    get_page = int(input("请输入你要爬去的页数："))
    data,page = get_url()
    t.sleep(1)
    r_page =  save_content(data)
    print(f"爬取完毕！理论获取{str(page*20)} 条数据,实际获取 {r_page} 条数据") 

#写入列表里面，存在无法去除最后一个分隔符,  解决办法就是直接再循环里面读取，不导入到外面的datalist列表里面








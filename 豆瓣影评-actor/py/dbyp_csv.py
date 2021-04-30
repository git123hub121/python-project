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
                "Cookie": 'll="118280"; bid=JVG-D58Gj9s; _vwo_uuid_v2=DE652E69B40FE43EAB29EF14117AF8B01|b930d3c2cb075bf63b7c69a69759ad07; __utmz=30149280.1600925804.2.2.utmcsr=guozhivip.com|utmccn=(referral)|utmcmd=referral|utmcct=/rank/; __gads=ID=2a953fd7603107be-223a118f58c400ce:T=1603259129:S=ALNI_MZWODSgZmy7xtPZ4TezGYTwK5cHCg; __utma=30149280.38508497.1599395137.1603257834.1603292497.8; push_doumail_num=0; ap_v=0,6.0; dbcl2="217290512:sGZ6QKfLZtY"; ck=gT0k; push_noty_num=0'
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
    with open("actor_d1.csv",'a',encoding="utf-8",newline='') as f:
        # f.write(','.join(th))
        # f.write("\n")
        count = 0
        a = csv.writer(f,delimiter=",")
        a.writerow(th)
        for data in datalist:
            count += 1
            a.writerow(data)
    return count
if __name__ =="__main__":
    # movie_id = input("请输入电影名字ID：")
    get_page = int(input("请输入你要爬去的页数："))
    data,page = get_url()
    t.sleep(1)
    r_page =  save_content(data)
    print(f"爬取完毕！理论获取{str(page*20)} 条数据,实际获取 {r_page} 条数据") 


# -*- coding: utf-8 -*-
#根据好评、中评、差评分别爬取25页，可爬取1300多条

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import random
def get_page_info(start_num,type):
    url="https://movie.douban.com/subject/"+ movie_id +"/comments?percent_type="+type+"&start="+str(start_num)+"&limit=20&status=P&sort=new_score&comments_only=1&ck=myI8"
    print(url)
    header = {
    "Accept":"application/json, text/plain, */*",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"movie.douban.com",
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    "Cookie":'你的'
    }
    response=requests.get(url,headers=header)
    req_parser = BeautifulSoup(response.content.decode('unicode_escape'),features="html.parser")
    comments = req_parser.find_all('div',class_="comment-item")
    id_list=[]
    link_list=[]
    name_list=[]
    vote_list=[]
    star_list=[]
    time_list=[]
    content_list=[]
    for comment in comments:
        try:
            comment=str(comment)
            id=re.findall(r'data-cid="(.*?)">',comment)[0]
            link=re.findall(r'href="(.*?)" title=',comment)[0]
            name=re.findall(r'title="(.*?)">',comment)[0]
            name=name.encode('utf-8', 'replace').decode('utf-8')
            vote=re.findall(r'"votes vote-count">(.*?)</span>',comment)[0]
            star=re.findall(r'<span class="allstar(.*?) rating"',comment)[0]
            time=re.findall(r'class="comment-time" title="(.*?)">',comment)[0]
            content=re.findall(r'<span class="short">(.*?)</span>',comment)[0]
            content=content.encode('utf-8', 'replace').decode('utf-8')
            # print(content)
            id_list.append(id)
            link_list.append(link)
            name_list.append(name)
            vote_list.append(vote)
            star_list.append(star)
            time_list.append(time)
            content_list.append(content)
        except:
            pass
    result=pd.DataFrame({"user_id":id_list,"user_name":name_list,"user_link":link_list,
                             'comment_voted':vote_list,'movie_star':star_list,"comment_time":time_list,'comment':content_list})
    return result

if __name__ =="__main__":
    movie_id = input("请输入电影id：")
    comments_list=[]
    times=25
    n=1
    types=['h','m','l']
    for i in range(times):
        print(i)
        start_num=i*20
        for j in range(3):
            comments = get_page_info(start_num,type=types[j])
            print('contain:%d'%comments.shape[0])
            comments_list.append(comments)
        time.sleep(2)
        n+=1
        if n%20==0:
            time.sleep(10)

    comments_data=pd.concat(comments_list)
    comments_data.to_csv(f'comment_{movie_id}.csv',index=False)



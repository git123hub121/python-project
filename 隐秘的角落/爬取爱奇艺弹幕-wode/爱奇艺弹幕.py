import requests
import zlib
import pandas as pd
import re
import time
def get_df():
    df_all = pd.DataFrame()#定义空df要放在最前面,你放在循环里面就全被自己删除了
    for i in range(1,100):
        print(f'正在获取第{i}页的弹幕数据')
        try:
            headers ={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                'Accept-Encoding':'gzip, deflate, br'
            }
            # page_num = 1
            url = f'https://cmts.iqiyi.com/bullet/41/00/7658778702074100_300_{str(i)}.z'
            #这一步报错，Error -3 while decompressing data: incorrect header check  需要添加try异常  
            try:
                req = requests.get(url, headers=headers, timeout=3)
            except Exception as e:
                print(e)
                req = requests.get(url, headers=headers, timeout=3)  
            # req = requests.get(url=url,headers=headers)
            zarray = bytearray(req.content)
            xml = zlib.decompress(zarray, 15+32).decode('utf-8')
            # xml[:700]
            '''
            <contentId>1607173538753008728</contentId>\n
            <content>吕不韦吕不韦把自己玩死了</content>\n
            <parentId>0</parentId>\n
            <showTime>1</showTime>\n
            <font>14</font>\n
            <color>ffffff</color>\n
            <opacity>5</opacity>\n
            <position>0</position>\n
            <background>0</background>\n
            <isReply>null</isReply>\n
            <likeCount>0</likeCount>\n
            <plusCount>0</plusCount>\n
            dissCount>0</dissCount>\n
            <isShowLike>false</isShowLike>\n
            <userInfo>\n
            <senderAvatar>https://www.iqiyipic.com/common/fix/headicons/male-130.png</senderAvatar>\n
            <uid>1413441584</uid>\n
            <udid>868084036467723</udid>\n
            <name>爱懒床的司马芳润</name>
            '''
            name = re.findall('<name>(.*?)</name>', xml)
            # 评论ID
            contentId = re.findall('<contentId>(.*?)</contentId>', xml)
            # 评论信息
            content = re.findall('<content>(.*?)</content>', xml)
            # 展示时间
            showTime = re.findall('<showTime>(.*?)</showTime>', xml)
            # 点赞次数
            likeCount = re.findall('<likeCount>(.*?)</likeCount>', xml)

            # 保存数据
            df_one = pd.DataFrame({
                'name': name,
                'contentId': contentId,
                'content': content,
                'showTime': showTime,
                'likeCount': likeCount
            })
            df_all = df_all.append(df_one, ignore_index=True)

            # 休眠一秒
            time.sleep(1)
            
        except Exception as e:
            print(e)
            break
    return df_all
df_all = get_df()
df_all.insert(0, 'episodes', '第15集')
episodes = '第15集'
df_all.to_csv(f'df_{episodes}.csv')
# def get_aiqiyi_danmu():
#     """
#     功能：给定tvid，获取爱奇艺一集的弹幕评论信息
#     """
#     # 建立空df
#     df_all = pd.DataFrame()

#     # 初始page_num
#     page_num = 1

#     while True:
#         # 打印进度
#         print(f'正在获取第{page_num}页的弹幕数据')

#         try:
#             # 获取URL
#             url = f'https://cmts.iqiyi.com/bullet/41/00/7658778702074100_300_{page_num}.z'

#             # 添加headers
#             headers = {
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
#             }

#             # 发起请求
#             try:
#                 r = requests.get(url, headers=headers, timeout=3)
#             except Exception as e:
#                 print(e)
#                 r = requests.get(url, headers=headers, timeout=3)

#             # 转换为arrry
#             zarray = bytearray(r.content)

#             # 解压字符串
#             xml = zlib.decompress(zarray, 15+32).decode('utf-8')

#             # 用户名
#             name = re.findall('<name>(.*?)</name>', xml)
#             # 评论ID
#             contentId = re.findall('<contentId>(.*?)</contentId>', xml)
#             # 评论信息
#             content = re.findall('<content>(.*?)</content>', xml)
#             # 展示时间
#             showTime = re.findall('<showTime>(.*?)</showTime>', xml)
#             # 点赞次数
#             likeCount = re.findall('<likeCount>(.*?)</likeCount>', xml)

#             # 保存数据
#             df_one = pd.DataFrame({
#                 'name': name,
#                 'contentId': contentId,
#                 'content': content,
#                 'showTime': showTime,
#                 'likeCount': likeCount
#             })

#             # 循环追加
#             df_all = df_all.append(df_one, ignore_index=True)

#             # 休眠一秒
#             time.sleep(1)

#             # 页数+1
#             page_num += 1

#         except Exception as e:
#             print(e)
#             break

#     return df_all

# df = get_aiqiyi_danmu()
# # 插入列
# df.insert(0, 'episodes', '第15集')
# # 导出数据
# df.to_csv('第15集.csv')





























# import pandas as pd
# import csv
# url = 'http://www.compassedu.hk/qs'
# df = pd.read_html(url)[0]
# df.to_csv('世界大学排名.csv',index=0)
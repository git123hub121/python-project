import requests
import json
import time
import pandas as pd
#构建多页,调用get_json()
def get_page(target_id,vid):
    df_all = pd.DataFrame()#创建一个空的df可遍历对象 初始化，跟定义空列表一样
    for i in range(15,10000,30):
        try:
            url = 'https://mfm.video.qq.com/danmu?target_id={}&vid={}&timestamp={}'.format(target_id,vid,i)
            df = get_json(url)
            # i = 15
            # url = 'https://mfm.video.qq.com/danmu?target_id={}&vid={}&timestamp={}'.format(target_id,vid,i)
            # df = get_json(url)
            #设置判断条件，确定有效数据信息
            if df.shape[0] == 0:
                print("没有数据")
            #break  break函数不可以用于if函数 break函数不能用于循环语句和switch语句之外的任何其他语句中
            else:
                df_all = df_all.append(df,ignore_index=True)
                # 休眠一秒
                time.sleep(1)
        except Exception as e:
            print(e)
            #continue
    print(f'爬虫程序中止，共获取{df_all.shape[0]}条弹幕!')
    return df_all

#先爬取一页
def get_json(url):
    #因为是get请求，所以不需要post参数
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52',
        'cookie': 'eas_sid=s115c9j6Z7e7T6U1K6o2u682h6; pgv_pvid=4528139576; pgv_pvi=2829546496; RK=46aBvytDYO;\
        ptcz=b23540e14a153ad5404cc630bf77baf27b8c91f1fe580df555fd2590cbb15f88; LW_uid=t1O5M9N713e9P4F9P0E2g7c2s4;\
        tvfe_boss_uuid=d102441917179fb8; video_guid=3c75255df04c8e0f; video_platform=2; uin_cookie=o2095793572;\
        ied_qq=o2095793572; o_cookie=2095793572; _video_qq_login_time_init=1605105041; main_login=qq;\
        vqq_access_token=A9C91DBD31BB01860E2C29ED38C63B06; vqq_appid=101483052; vqq_openid=A139C76293F38C93EB16E59AD4D404C1;\
        vqq_vuserid=510447283; vqq_refresh_token=037220337B231DF20FD6D5C442081F05; LW_sid=K1p6Y0L6888283v8d286f4V8j5; uid=802180484;\
        vqq_vusession=u3zQGXKQ0me1u1NM3-bqDQ..; pgv_info=ssid=s2433808784; vqq_next_refresh_time=5775; vqq_login_time_init=1607132968;\
        login_time_last=2020-12-5 9:49:27'
    }
    req = requests.get(url = url, headers= headers)
    # print(req.text)   如果你要处理的是文件而不是字符串，你可以使用json.dump()和json.load()来编码和解码JSON数据,这里很显然不是.json文件
    data = json.loads(req.text,strict = False)['comments']
    #print(data)
    #这里需要明确一个道理，js、xhr文件都是一种json格式 {'变量':[数组],...},如下图，这里面就有我们需要的数据
    '''
    "comments":[
        {
            "commentid":"6717761143597148315",
            "content":"19.40我第一",
            "upcount":74,
            "isfriend":0,
            "isop":0,
            "isself":0,
            "timepoint":9,
            "headurl":"",
            "opername":"",有空值而已，并非全空
            "bb_bcolor":"",
            "bb_head":"",
            "bb_level":"http://i.gtimg.cn/qqlive/images/20170106/i1483692016_1.jpg",
            "bb_id":"",
            "rich_type":0,
            "uservip_degree":3,
            "content_style":"{\"color\":\"ffffff\",\"gradient_colors\":[\"FDA742\",\"FBF076\"],\"position\":1,\"colorConfigId\":\"11\",\"lowVipDegree\":1}"
            },
        ...]
    '''
    #指定需要的数据---#[index]['参数key']
    # Commentid = []
    # for i in range(len(data)):
    #     commentid = data[i]['commentid']
    #     Commentid.append(commentid)
    # print(Commentid)
    commentid = [ i['commentid'] for i in data]#学会写列表表达式，效率会快很多，代码也简洁
    content  = [ i['content'] for i in data]
    df_data = {
        'commentid':commentid,
        'content':content
    }
    df_one = pd.DataFrame(df_data)
    return df_one
#构建数据字典
# df_all = {

# }

df = get_page(target_id='5979258600',vid='f0034cqed1f')
df.insert(0, 'episodes', '第一期上')#插入一列 在0列插入列名为e..，行值为'第一期上'的一列数据
df_list = [df]
for df_name in df_list:
    csvname = df_name.episodes[0]
    df_name.to_csv(f'{csvname}.csv',index = True)



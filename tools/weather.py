#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib, sys, urllib2
import ssl
import json
import requests

def send_msg(msg):
   headers = {"Content-Type": "application/json"}
   data = {
      "msgtype": "markdown",
      "markdown": {
         "content": msg,
      }
   }
   r = requests.post(
      url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=TOKEN',
      headers=headers, json=data)
   # print(r.text)

def main():
    host = 'https://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    method = 'GET'
    appcode = 'APPCODE'
    querys = 'cityid=76'
    bodys = {}
    url = host + path + '?' + querys
    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        response = urllib2.urlopen(request, context=ctx)
        content = response.read()
        if (content):
            load_dict = json.loads(content)
            # load_dict = content
            reload(sys)
            sys.setdefaultencoding('utf-8')
            msg ="【今日" +  load_dict['result']['city'] + "天气预报】(" + \
                load_dict['result']['updatetime'] + " 发布)\n" + \
                "> 实时天气 " + load_dict['result']['weather'] + "\n\n" + \
                "> 当前温度 "+load_dict['result']['temp'] + "℃, 今日温度范围 " + \
                load_dict['result']['templow'] + "℃ ~ " +  load_dict['result']['temphigh'] + "℃\n\n" +\
                "> 空气质量(AQI)\n" + load_dict['result']['aqi']['aqiinfo']['level'] + " " + \
                load_dict['result']['aqi']['aqiinfo']['affect'] + \
                load_dict['result']['aqi']['aqiinfo']['measure'] + "\n\n"

            notice = "> 温馨提示\n"
            notice_msg = ""
            for i in range(len(load_dict['result']['index'])):
                notice_msg = notice_msg + "- " + load_dict['result']['index'][i]['iname'] + \
                load_dict['result']['index'][i]['detail'] + "\n"
            # print(msg + notice + notice_msg)
            #  发送消息
            send_msg(msg + notice + notice_msg)

    except Exception:
        send_msg("获取天气预报信息失败")
if __name__ == "__main__":
    main()

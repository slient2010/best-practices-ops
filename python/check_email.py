#!/usr/bin/env python3
"""
mail client
"""
# -*- coding:utf-8 -*-
###############################################
# Author        : Nelson
# EMail         : slient2010@163.com
# Created Time  : 2021-09-30 13:30:10
# File Name     : check_email.py
# Description   : nothing
###############################################

# 引入模块及IMAPClient类
import email
import sys
import os
import time
from html.parser import HTMLParser
from imapclient import IMAPClient

HOSTNAME = 'imap.163.com'
USERNAME = 'slient2010@163.com'
# 163的授权码
PASSWD = 'GRANT_PERMISION_CODE'
# check mail every 10 seconds
MAIL_CHECK_FREQ = 10


class MyHTMLParser(HTMLParser):
    '''
    Parse HTML.
    '''
    def handle_data(self, data):
        if len(data) > 1:
            print(data)


def send_notice():
    '''
    发送消息到终端或IM（钉钉）。
    '''
    os.system('echo "有你关注的邮件，请即使查看/data/mail目录下的邮件内容" | wall ')


def filter_email_content(mail_content):
    '''
    过滤自己关心的邮件
    '''
    if "自己" in str(mail_content):
        parser = MyHTMLParser()
        # TODO: 保存便于终端读取
        parser.feed(mail_content)
        print("xxxxxxxxxxx, found it")
        # 发送消息
        send_notice()
    else:
        print("抱歉，未匹配到邮件内容。")


class CompanyEmailChecker():
    '''
    query, filter emails.
    '''
    def __init__(self):
        self.mail_client = IMAPClient(HOSTNAME, ssl=True)
        try:
            # 登录个人帐号
            self.mail_client.login(USERNAME, PASSWD)
            self.mail_client.id_({"name": "IMAPClient", "version": "0.12"})
        except self.mail_client.Error:
            print('Could not log in')
            print(self.mail_client.Error)
            sys.exit(1)

    def get_mail_folders(self):
        '''
        Get all mail folers, including customize folders.
        Return: string list
        '''
        folders_list = []
        folders = self.mail_client.list_folders()
        for folder in folders:
            if folder[2] not in ["草稿箱", "已发送", "已删除", "垃圾邮件"]:
                folders_list.append(folder[2])
        return folders_list

    def get_inbox_mails(self):
        '''
        just get the inbox folder mails.
        '''
        # 利用select_folder()函数进行文件夹，'INBOX'为收件箱，readonly = True 表明只读并不修改任何信息
        self.mail_client.select_folder('INBOX', readonly=False)
        result = self.mail_client.search('UNSEEN')
        msgdict = self.mail_client.fetch(result, ['BODY.PEEK[]'])
        print('You have ' + str(len(msgdict.items())) + ' mail(s).')

    def get_selected_mails(self, folder):
        '''
        get the selected folder mails.
        '''
        self.mail_client.select_folder(folder, readonly=False)
        result = self.mail_client.search('UNSEEN')
        msgdict = self.mail_client.fetch(result, ['BODY.PEEK[]'])
        print('You have ' + str(len(msgdict.items())) + ' mail(s) in '
              + folder + ' folder.')
        if len(msgdict.items()) == 0:
            return None
        return msgdict

    # def get_all_mails(self):
    def read_mail(self, msgdict):
        '''
        read mail
        '''
        # 统计邮件数量
        i = 0
        # 现在已经把邮件取出来了，下面开始解析邮件
        for message_id, message in msgdict.items():
            for key, value in message.items():
                if "BODY" in str(key):
                    # 生成Message类型
                    e = email.message_from_bytes(message[key])
                    # 由于'From', 'Subject' header有可能有中文，必须把它转化为中文
                    subject = email.header.make_header(
                                  email.header.decode_header(e['SUBJECT']))
                    mail_from = email.header.make_header(
                                  email.header.decode_header(e['From']))
                    # 解析邮件正文
                    maintype = e.get_content_maintype()
                    if maintype == 'multipart':
                        for part in e.get_payload():
                            if part.get_content_maintype() == 'text':
                                mail_content = part.get_payload(
                                    decode=True).strip()
                    elif maintype == 'text':
                        mail_content = e.get_payload(decode=True).strip()

                    # 此时，需要把content转化成中文，利用如下方法：
                    try:
                        mail_content = mail_content.decode('gbk')
                    except UnicodeDecodeError:
                        try:
                            mail_content = mail_content.decode()
                        except UnicodeDecodeError:
                            print('decode error')
                            sys.exit(1)
                    # getstr = input('If you wanna read it, input y: ')
                    # if getstr.startswith('y'):
                    # read the mail content
                    i += 1
                    print('\nThe ' + str(i) + ' mail')
                    print('From: ', mail_from)
                    # TODO：保存后面发送消息提示
                    print('Subject: ', subject)
                    print('='*30, 'mail content start', '='*28)

                    parser = MyHTMLParser()
                    parser.feed(mail_content)
                    # 邮件过滤
                    filter_email_content(mail_content)
                    print('='*30, 'mail content end', '='*30)
        # 设置邮件已读
        self.mail_client.set_flags(msgdict, b'\\Seen', silent=False)

    def logut(self):
        '''
        logout
        '''
        self.mail_client.logout()


if __name__ == "__main__":
    # TODO: 修改循环
    N = 100
    counter = 1
    while counter <= N:
        print('='*30, 'check start', '='*28)
        mail_checker = CompanyEmailChecker()
        need_to_check_mail_folder = mail_checker.get_mail_folders()
        # mail_checker.get_inbox_mails()
        if len(need_to_check_mail_folder) >= 1:
            for check_folder in need_to_check_mail_folder:
                msg_dicts = mail_checker.get_selected_mails(check_folder)
                if msg_dicts:
                    mail_checker.read_mail(msg_dicts)
        mail_checker.logut()
        print('='*30, 'check end', '='*28)
        time.sleep(MAIL_CHECK_FREQ)
        counter += 1

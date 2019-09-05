'''
@description: basic function for common
@return : return value is all by jsondata
'''

#-*- coding:utf-8 -*-
import json
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate

def checkUserLoginInfo(username,password):
    '''
    @brief: basic function to check password and username
    :param username: 用户名
    :param password: 密码
    :return: jsondata that whether has password or user problem
    if OK == 1 : means checkResult ok
    '''
    dict_Result = {}
    dict_Result['OK'] = 0
    if len(username) < 6 :
        str_error_type = "输入用户名过短,请重新输入"
        dict_Result['error'] = str_error_type
        return json.dumps(dict_Result,ensure_ascii=False,sort_keys=True)
    if len(password) < 6 :
        str_error_type = "输入密码过短,请重新输入"
        dict_Result['error'] =  str_error_type
        return json.dumps(dict_Result,ensure_ascii=False,sort_keys=True,)
    dict_Result['OK'] = 1
    return json.dumps(dict_Result)


''' password method : 加密 or 解密 '''
def generateSecurityPassword(password):
    '''
    @description: gernerate Security Word:
    :param password:
    :return: str type that has make it security
    '''
    security_password = make_password(password)
    return security_password

def checkSecurityPassword(password,security_password):
    '''
    @description: check security password
    :param password:
    :param security_password:
    :return: bool type
    '''
    b_Result = check_password(password,security_password)
    return b_Result
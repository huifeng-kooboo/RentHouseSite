'''
@description: basic function for common
@return : return value is all by jsontype
'''
import json

def checkUserLoginInfo(username,password):
    '''
    @description: basic function to check password and username
    :param username: 用户名
    :param password: 密码
    :return: jsondata that whether has problem
    if OK == 1 : means checkResult ok
    '''
    dict_Result = {}
    dict_Result['OK'] = 0
    if len(username) < 6 :
        dict_Result['error'] = "输入用户名过短,请重新输入"
        return json.dumps(dict_Result)
    if len(password) < 6 :
        dict_Result['error'] = "输入密码过短,请重新输入"
        return json.dumps(dict_Result)
    dict_Result['OK'] = 1
    return json.dumps(dict_Result)
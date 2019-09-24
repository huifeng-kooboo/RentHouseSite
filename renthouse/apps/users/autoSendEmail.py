'''
@brief:自动发送邮件功能：用来通知以及debug
简单测试，后续进行封装
'''
import yagmail


yag = yagmail.SMTP(user='942840260@qq.com',password='diyjrylkgtmcbfbe',host='smtp.qq.com')

contents = {'测试一下数据咯'}

yag.send('2885369654@qq.com','subject',contents)
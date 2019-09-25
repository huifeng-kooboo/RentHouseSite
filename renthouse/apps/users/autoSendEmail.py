'''
@brief:自动发送邮件功能：用来通知以及debug
简单测试，后续进行封装
'''
import yagmail

#user:发件人邮箱号
#password:发件人授权码
#host：发件人主机地址
yag = yagmail.SMTP(user='942840260@qq.com',password='diyjrylkgtmcbfbe',host='smtp.qq.com')

#content：需要发送的消息
contents = {'测试一下数据咯'}

#发送的信息
yag.send('2885369654@qq.com','subject',contents)
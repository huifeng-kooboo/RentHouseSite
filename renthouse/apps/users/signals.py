# author: ytouch
# createdate:2019.8.27
# brief: a basic function to manage all signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserModel

@receiver(post_save,sender=UserModel)
def user_save(sender,instance,created=False,**kwargs):
    '''
    :brief: 对注册的密码进行加密保存
    :param sender: 需要监听的model
    :param instance: 实例
    :param created: 被创建时触发
    :param kwargs:
    :return:
    '''
    if created:
        password = instance.password
        instance.set_password(password) #加密
        instance.save()


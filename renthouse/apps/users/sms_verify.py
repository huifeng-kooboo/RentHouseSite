#短信认证模块 ： 后续完善
#参考网站：https://cloud.tencent.com/document/product/382/11672
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

appid = 1400258274
appkey = '5f24c52f157d1b490bc9cacbcc1df32e'
phone_numbers = ["13824464121"]
template_id = 7839  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "测试"  #

ssender = SmsSingleSender(appid, appkey)
params = ["5678"]  # 当模板没有参数时，`params = []`
try:
  result = ssender.send_with_param(86, phone_numbers[0],
      template_id, params, sign=sms_sign, extend="", ext="")
except HTTPError as e:
  print(e)
except Exception as e:
  print(e)
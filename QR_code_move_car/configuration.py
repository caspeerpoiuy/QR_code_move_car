# send message configuration
appid = 1400188694  # SDK AppID是1400开头

# 短信应用SDK AppKey
appkey = "8b961b4ae58d0381f70777ae77314de2"

# 需要发送短信的手机号码
phone_numbers = ["13021990159"]

# 短信模板ID，需要在短信应用中申请
template_id = 7839  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
# templateId 7839 对应的内容是"您的验证码是: {1}"
# 签名
sms_sign = "腾讯云"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID
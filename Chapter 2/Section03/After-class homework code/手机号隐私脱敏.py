print("-------- 手机号隐私脱敏 --------")
phone = "13812345678 "
change_phone = phone[:3] + "****" + phone[7:]
print(change_phone)
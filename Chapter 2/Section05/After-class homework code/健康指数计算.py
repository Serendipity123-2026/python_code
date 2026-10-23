from custom_module import MALE_BMI_MAX, FEMALE_BMI_MAX, bmi

m_w = float(input("请输入男生体重："))
m_h = float(input("请输入男生身高："))
f_w = float(input("请输入女生体重："))
f_h = float(input("请输入女生身高："))

if bmi(m_w, m_h) <= MALE_BMI_MAX or bmi(f_w, f_h) <= FEMALE_BMI_MAX:
    print("健康")
else:
    print("超重")
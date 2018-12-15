# BMI計算公式 BMI = 體重(公斤)/身高2(公尺2)

height = input('請輸入您的身高(cm): ')
weight = input('請輸入您的體重(kg): ')
height = int(height)
weight = int(weight)
height = height / 100
bmi = weight / height / height
if bmi < 18.5:
	print('您的BMI值為: ',bmi ,'屬於體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的BMI值為: ',bmi ,'屬於正常範圍')
elif bmi >= 24 and bmi < 27:
	print('您的BMI值為: ', bmi ,'稍重')
elif bmi >= 27 and bmi < 30:
	print('您的BMI值為', bmi ,'輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的BMI值為', bmi ,'中度肥胖')
else:
	print('您的BMI值為', bmi, '重度肥胖')
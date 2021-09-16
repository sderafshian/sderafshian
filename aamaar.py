people = int(input('لطفا تعداد افراد خانواده خودتان را وارد کنید'))
r = 1
while r <= people:
	name = input('لطفا نام و نام خانوادگی خود را وارد کنید')
	sex = input('مرد یا زن؟')
	age = int(input('سن شما؟'))
	live = input('مرده یا زنده?')
	r = r + 1
	if live == 'مرده؟':
		continue
	if age > 18:
		edu = input('تحصیلات شما؟')
		job = input('آیا شاغلید؟')
		if job == 'بله':
			tax = int(input('میانگین درآمد؟'))
		maried = input('آیا ازدواج کردید؟')
		m1 = 0
		if maried == 'بله':
			m1 = m1 + 1
print("تعداد افراد متأهل در این خانواده " + str(people) + "نفری " + str(m1) + "نفر است.")

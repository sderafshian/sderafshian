right = input('لطفا متن مورد نظر را وارد کنید')
mis = input('حرف غلط را وارد کنید')
cor = input('حرف درست را وارد کنید')
len1 = len(right)
for r in range (len1):
	if right[r] == mis:
		right = right[:r] + cor + right[r+1:]
	r = r + 1
print(right)
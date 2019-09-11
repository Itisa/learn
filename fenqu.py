def fen_qu(req):
	ans1 = []
	ans = {}
	num = 0
	for i in req:
		num += i[1]
	for i in range(num):
		ans[i] = 0
	num = float(num)
	for i in req:
		lo = 0
		blank = num/i[1]
		bl = 100
		er_bl = 0
		i1 = 0
		fl = 0
		# print(i[1])
		
		# ans1 = []
		# for ix in ans:
		# 	ans1.append(ans[ix])
		# print(ans1)
		
		while i1 < i[1]:
			lo += 1
			if lo == num:
				lo = 0
				er_bl += 1
		# for i1 in range(i[1]):
			# print('bl:',bl,'i1:',i1,'lo:',lo,'blank:',blank,'fl:',fl,'er_bl:',er_bl)
			if ans[lo] == 0 and blank - bl - 1 <= er_bl:
				ans[lo] = i[0]
				i1 += 1
				# print('in',lo,i[0])
			if ans[lo] == i[0]:
				bl = 0
			if not (ans[lo] == 0 and blank-bl <= er_bl):
				bl += 1
				# fl += blank-int(blank)
				# if fl>1:
					# lo += 1
					# bl += 1
					# fl = 0
			
				# lo += blank-1
		# print('blank:',blank,num,i)

	# print(ans)
	ans1 = []
	for i in ans:
		ans1.append(ans[i])
	print(ans1)
	
	x = []
	for i in ans1:
		x.append(i)
		if len(x) == 4:
			print(x)
			x = []
	# print('a:',ans1.count('a'))
	# print('b:',ans1.count('b'))
	# print('c:',ans1.count('c'))
	# print('d:',ans1.count('d'))



# lis = [['a',15],['b',10],['c',3],['d',4]]
lis = [['O',3],['X',4],['S',10],['T',15]]
# print(lis)
fen_qu(lis)

def spl(a,b):
	lb = len(b)
	d = []
	i1 = 0
	for i in range(len(a)):
		print(i)
		if a[i:i+lb] == b:
			d.append(a[i1:i])
			i1 = i+lb
			print(i,i1)
	if not i1-1 == i:
		d.append(a[i1:])
	return d

a = '21345gfhdwq3rgfh23tgfhyuftyggfh'
b = 'gf'
# print(spl(a,b))

def makesure_xoy(a):
	a.sort()
	if len(a) < 2:
		return False
	if a[0][0] == a[1][0]:
		x = 1
		while x < len(a)-1:
			if a[x][0] == a[x+1][0] and a[x][1]-a[x+1][1] == -1:
				pass
			else:
				return False
			x += 1
		return True

	if a[0][1] == a[1][1]:
		x = 1
		while x < len(a)-1:
			if a[x][1] == a[x+1][1] and a[x][0]-a[x+1][0] == -1:
				pass
			else:
				return False
			x += 1
		return True

	i = a[0]
	i1 = a[1]
	k = (i[1]-i1[1])/(i[0]-i1[0])
	l = i[1]-k*i[0]
	print(k,l)
	if k == 1 or k == -1:
		x = 1
		while x < len(a):
			if a[x][0]*k+l==a[x][1] and a[x][0]-a[x+1][0] == -1:
				return False
			x += 1
		return True
	else:
		return False
		
	# if a[0] == b[0]:
	# 	if c[0] == a[0]:
	# 		if d[0] == a[0]:
	# 			return True
	# 		else:
	# 			return False
	# 	else:
	# 		return False
	# if a[1] == b[1]:
	# 	if c[1] == a[1]:
	# 		if d[1] == a[1]:
	# 			return True
	# 		else:
	# 			return False
	# 	else:
	# 		return False

	# k = (a[1]-b[1])/(a[0]-b[0])
	# l = b[1]-((a[1]-b[0])*a[0])/(a[0]-b[0])
	# if k == 1 or k == -1:
	# 	if c[0]*k+l==c[1]:
	# 		if d[0]*k+l == d[1]:
	# 			return True
	# 		else:
	# 			return False
	# 	else:
	# 		return False
				
	return False
# a = [[0,0],[1,2],[3,6],[7,3]]
# print(makesure_xoy(a))

class btree(object):
	def __init__(self, number):
		self.number = number
		self.left = None
		self.right = None


def do_tree(num):
	root = btree(1)
	print(root)
	
	for i in range(2,num+1):
		find(root,i)
	pri(root)

def find(root,num):
	a = [root]
	b = []
	while 1:
		for i in range(len(a)):
			if not a[i].left:
				num = btree(num)
				a[i].left = num
				return True
			elif not a[i].right:
				num = btree(num)
				a[i].right = num
				return True
			else:
				b.append(a[i].left)
				b.append(a[i].right)
		# print(root.left,root.left.left,root.right)
		a = b[:]
def pri(now):
	print(now.number)
	# if now.left:		
	# 	pri(now.left)
	# if now.right:
	# 	pri(now.right)
	a = [now]
	b = []
	while 1:
		for i in a:
			if i.left:
				b.append(i.left)
				print(i.left.number)
			else:
				return
			if i.right:
				b.append(i.right)
				print(i.right.number)
			else:
				return
		a = b[:]
do_tree(15)




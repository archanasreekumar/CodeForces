n = raw_input()
n = int(n)
l = []

for i in range(n):

	inp = raw_input()
	l.append(inp)

for i in range(n):
	s_len = len(l[i])
	#print s_len
	if s_len<=10:
		print l[i]
	else:
		print l[i][0]+str(s_len-2)+l[i][s_len-1]
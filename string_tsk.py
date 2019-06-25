s = raw_input()
l = []
for i in s:
	#print i
	if (i=="a" or i=="e" or i=="i" or i=="o" or i =="u" or i == "y" or i=="A" or i=="E" or i=="I" or i=="O" or i =="U" or i =="Y"):
		s = s.replace(i,"")
#print s

for i in s:
	l.append(".")
	l.append(i.lower())
#for i in l:
#	print i
str1 =''
str1 =''.join(l)
print str1

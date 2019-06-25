n,k = raw_input().split(" ")
n = int(n)
k = int(k)
count=0
l=[]

score = raw_input().split(" ")
#score=int(score)
#print score
#for i in range(n):
	
	#l.append(score)

for i in range(n):
	if int(score[i])!=0 or int(score[k-1])!=0:
		if int(score[i]) >=  int(score[k-1]):
			count+=1
print count

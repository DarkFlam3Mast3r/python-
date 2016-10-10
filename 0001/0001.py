import random

def ConvertToLower(word):
	if( ord(word) >= 65 and ord(word) <= 90):
		word = chr(ord(word) + 32)

	return word


def checkUniqueness(array, code):
	check = 0
	count = 0
	for word in array:
	# 	for ch in word:
	# 		ch = ConvertToLower(ch)
	# array[count] = word
	# count += 1

		if code not in array:
			check = 1
	#print(check)
	return check


Character = []
#add upper A-Z
for i in range (65,91):
	Character.append(i)
#add lower a-z
for i in range (97,123):
	Character.append(i)
#add 0-9
for i in range (48,58):
	Character.append(i)

ChrCharacter = []
count = 0
for i in Character:
	ChrCharacter.append(chr(Character[count]))
	count+=1

#create an array to store the Code
activeCode = [[]]*200
#create string to store code
activeCodeinStr= [[]]*200
#print(activeCode)
temp = []
for i in range(200):
	temp = random.sample(ChrCharacter,5)
	if(checkUniqueness(activeCode,temp)):
		activeCode[i] =temp
		activeCodeinStr[i] = "".join(temp)
	else:
		i-=1
# count1 = 0
# count2 = 0
# for word in activeCode:
# 		for ch in word:
# 			ch = ConvertToLower(ch)
# 			print(ch)
# 			activeCode[count2][count1]=ch
# 			count1 +=1
# 		count2 += 1
		

#print it
for code in activeCodeinStr:
	print(code)
	








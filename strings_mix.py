def mix(s1,s2):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	count1 = []
	count2 = []
	max1 = []
	max2 = []
	equal = []
	form1 = []
	form2 = []
	forme = []
	
	for letter in alpha:
		lets = list(filter(lambda x: x == letter, s1))
		count1.append(lets)
	for letter in alpha:
		lets = list(filter(lambda x: x == letter, s2))
		count2.append(lets)
			
	for i in range(0,len(count1)):
		if len(count1[i]) == len(count2[i]) and len(count1[i]) > 1:
			equal.append(count1[i])
		elif len(count1[i]) > len(count2[i]) and len(count1[i]) > 1:
			max1.append(count1[i])
		elif len(count1[i]) < len(count2[i]) and len(count2[i]) > 1:
			max2.append(count2[i])
	
	for items in max1:
		form1.append('1:' + items[0]*len(items))
	for items in max2:
		form2.append('2:' + items[0]*len(items))
	for items in equal:
		forme.append('=:' + items[0]*len(items))
		
	final = form1 + form2 + forme
	final.sort(key=len, reverse=True)
	return '/'.join(final)
	
	
	
	
	
	
	
	
# - Test Case - 
mix("looping is fun but dangerous", "less dangerous than coding")#, "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")

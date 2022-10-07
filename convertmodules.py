#来自博客https://blog.csdn.net/qq_42479394/article/details/105342446
def zh(path):
	result=[]
	with open(path, encoding='utf-8') as f:
		for line in f:
			result.append(line.strip('\n').split(',')[0])
	return result
	#下面是对读取到的数组进行变化
	result_gai = []
	a = 0
	for i in result:
		while(a%2 == 0):
			pos = i.find('：') #查找某一个字符在在字符串的位置
			result_gai.append(i[pos+1:])
			break
		a+=1
	return len(result)


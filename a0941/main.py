def len_input():
	length = raw_input()
	data = raw_input()
	return data.split(' ')

alist = len_input()
blist = len_input()
# alist = ['-1','5','8']
# blist = ['2','3','6']
dlist = alist+blist
dlist.sort()
print ' '.join(dlist)+' '
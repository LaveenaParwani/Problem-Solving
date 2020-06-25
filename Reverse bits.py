'''def reverseBits(a):
    
    result=[]
    for n in a:
        rev = 0
        while (n > 0):
                # bitwise left shift 'rev' by 1 
	        rev = rev << 1
		
                # if current bit is '1' 
	        if (n & 1 == 1):
	            rev = rev ^ 1
		
		# bitwise right shift 'n' by 1 
	        n = n >> 1
	        
        result.append(rev)
    return result
	
if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    print(reverseBits(a))
'''
def reverseBits(a):
    
    rlt=[]
    for n in a:
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        rlt.append(result)
    return rlt
	
if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    print(reverseBits(a))
 

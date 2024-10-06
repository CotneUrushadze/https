def is_Palindrom(st):
    if not isinstance(st, str):
        return False
    left, right = 0, len(st) - 1
    while left < right:
        if st[left] != st[right]:
            return False 
        
        left += 1
        right -= 1
        return True
        
print(is_Palindrom("racecar"))
        
        
        
        
            
        
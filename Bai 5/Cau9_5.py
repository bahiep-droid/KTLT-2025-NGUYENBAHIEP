print(" Sinh vien: Nguyen Ba Hiep")
print(" MSV : 245752021610098")
binary_search([1,2,3,5,8], 6) 
binary_search([1,2,3,5,8], 5) 
def binary_search(dlist, item):
    lowerBound = 0
    upperBound = len(dlist) - 1
    found = False
    
    while lowerBound <= upperBound and not found:
        midPoint = (lowerBound + upperBound) // 2
        
        if dlist[midPoint] == item:
            found = True
        elif dlist[midPoint] < item:
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1
    
    return found

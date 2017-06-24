
# coding: utf-8

# In[3]:

largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    try:
        if (num == "done") : break
        num = int(num)
        if (largest is None):
            largest = num
        if (smallest is None):
            smallest = num
        if (num < smallest):
            smallest = num
        if (num > largest):
            largest = num
        
    except:
        print ("Not a valid number!")
        
print ("Maximum is", largest)
print ("Minimum is", smallest)


# In[ ]:




# In[5]:

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == 'done' : break
 
    try:
        num = int(num)
        
    except:
        print ("Invalid input")
        continue
    
    if (largest is None):
    	largest = num
    if (smallest is None):
        smallest = num
    if (num < smallest):
        smallest = num
    if (num > largest):
        largest = num
        
print ('Maximum is', largest)
print ('Minimum is', smallest)


# In[ ]:




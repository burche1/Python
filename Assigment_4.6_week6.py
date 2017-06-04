
# coding: utf-8

# In[4]:

rate = input("Enter rate: ")
hrs = input("Enter Hours: ")
def computepay(hrs, rate):
    hours = float(hrs)
    rate = float(rate)
    if (hours > 40):
        x = hours - 40
        pay = (rate*40) + (rate*1.5*x)
    else:
        pay = rate * hours
    return pay

p = computepay(hrs, rate)
print(p)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




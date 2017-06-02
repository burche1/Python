
# coding: utf-8

# In[2]:

#Assigment 3.1

hrs = input("Enter Hours: ")
hours = float(hrs)
rate = input("Enter rate: ")
rate = float(rate)
if (hours > 40):
    x = hours - 40
    pay = (rate*40) + (rate*1.5*x)
else:
    pay = rate * hours
print(pay)


# In[8]:

#Assigment 3.3

score = input("Enter Score: ")
score = float(score)
if (score < 0.0 and score > 1.0):
    print ("Error, the score is out of range.")
    quit()
else:
    if (score >= 0.9):
        print ("A")
    elif (score >= 0.8):
        print ("B")
    elif (score >= 0.7):
        print ("C")
    elif (score >= 0.6):
        print ("D")
    else:
        print ("F")


# In[ ]:




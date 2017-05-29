
# coding: utf-8
Head First Python
Cap. 01:
# In[3]:

#Lista de filmes

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies)
print(movies[1])


# In[8]:

#pág 10

cast = ["Cleese", "Palin", "Jones", "Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)

cast.remove("Chapman")
cast.insert(0, "Chapman")
print(cast)


# In[11]:

#pág 15, for:

fav_movies = ["The Holy Gray", "The Life of Brian"]
for each_flick in fav_movies:
    print(each_flick)

#while

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count = count + 1


# In[18]:

#pág 19

movies = ["The Holy Gray", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)


# In[20]:

#pág. 30 function:
movies = ["The Holy Gray", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(movies)


# In[ ]:




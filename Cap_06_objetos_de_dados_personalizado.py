
# coding: utf-8

# In[1]:

import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter6')            #muda o diretório
os.getcwd()

def sanitize(time_string):
    if '-' in time_string:                      
        splitter = '-'                          
    elif ':' in time_string:                    
        splitter = ':'                          
    else:                                       
        return(time_string)                     
    (mins, secs) = time_string.split(splitter)  
    return(mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)
    
sarah = get_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)                                                #separando os dois primeiros itens da lista
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))  #imprimindo


# In[7]:

cleese = {}
palin = dict()
type(cleese)
type(palin)

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}

palin['Name']
cleese['Occupations'][-1]

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"

palin
cleese


# In[8]:

def sanitize(time_string):
    if '-' in time_string:                      
        splitter = '-'                          
    elif ':' in time_string:                    
        splitter = ':'                          
    else:                                       
        return(time_string)                     
    (mins, secs) = time_string.split(splitter)  
    return(mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)
    
sarah = get_data('sarah2.txt')

sarah_data = {}                                           #criando dicionário vazio
sarah_data['Name'] = sarah.pop(0)                         #atribuindo o nome ao identificado Name
sarah_data['DOB'] = sarah.pop(0)                          #atribuindo data de nascimento ao identificador DOB
sarah_data['Times'] = sarah                               #atribuindo tempos ao identificador Times
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))


# In[10]:

def sanitize(time_string):
    if '-' in time_string:                      
        splitter = '-'                          
    elif ':' in time_string:                    
        splitter = ':'                          
    else:                                       
        return(time_string)                     
    (mins, secs) = time_string.split(splitter)  
    return(mins + '.' + secs)

#agregando funções a função get_data:

def get_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        temp = data.strip().split(',')
        return ({'Name': temp.pop(0), 'DOB': temp.pop(0), 'Times': str(sorted(set([sanitize(t) for t in temp]))[0:3])})
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)
    
james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

print(james['Name'] + "'s fastest times are: " + james['Times'])
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])


# In[23]:

#classes

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
type(sarah)
type(james)

sarah.name
james.name
sarah.dob
james.dob
sarah.times
james.times


# In[27]:

#mesmo programa, porém usando classes:
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self, time_value):
        self.times.append(time_value)
    
    def add_times(self, list_of_times):
        self.times.extend(list_of_times)
    
def get_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        temp = data.strip().split(',')
        return (Athlete(temp.pop(0), temp.pop(0), temp))
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)
    
james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))


#testando novas funcionalidades da classe Athlete
vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())

vera.add_times(['2.22', "1-21", '2:22'])
print(vera.top3())


# In[32]:

#classe herdada:
class NamedList(list):                #fornecemos o nome da classe da qual deriva essa nova classe
    def __init__(self, a_name):
        list.__init__([])             #iniciamos a derivada da classe
        self.name = a_name            #atribuimos o argumento ao atributo
        
johnny = NamedList("John Paul Jones")
type(johnny)
dir(johnny)                           #faz tudo que uma lista faz, incusive name

johnny.append("Bass Player")
johnny.extend(['Composer', 'Arranger', 'Musician'])
johnny
johnny.name

for attr in johnny:
    print(johnny.name + " is a " + attr + ".")


# In[35]:

#classe herdada:
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', "1-21", '2:22'])
print(vera.top3())


# In[36]:

#programa completo:

import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter6')            #muda o diretório
os.getcwd()

def sanitize(time_string):
    if '-' in time_string:                      
        splitter = '-'                          
    elif ':' in time_string:                    
        splitter = ':'                          
    else:                                       
        return(time_string)                     
    (mins, secs) = time_string.split(splitter)  
    return(mins + '.' + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
    
def get_data(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        temp = data.strip().split(',')
        return (AthleteList(temp.pop(0), temp.pop(0), temp))
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)
    
james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))


# In[ ]:




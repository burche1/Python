
# coding: utf-8

# In[10]:

import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter5')            #muda o diretório
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

with open('james.txt') as jam:                   #abrindo o arquivo
    data = jam.readline()                        #lendo a linha e armazenando em data
james = data.strip().split(',')                  #convertendo os dados em uma lista, encadeamento de métodos... processa da esquerda para a direita
with open('julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')

james_new = []
julie_new = []
mikey_new = []
sarah_new = []

for each_item in james:
    james_new.append(sanitize(each_item))

for each_item in julie:
    julie_new.append(sanitize(each_item))
    
for each_item in mikey:
    mikey_new.append(sanitize(each_item))
    
for each_item in sarah:
    sarah_new.append(sanitize(each_item))
    
print(sorted(james_new))                       #encadeamento de funções... processado da direita para a esquerda
print(sorted(julie_new))
print(sorted(mikey_new))
print(sorted(sarah_new))


# In[12]:

lista = [6, 3, 1, 2, 4, 5]
lista.sort()                                  #substituí lista pela versão ordenada
print(lista)
lista.sort(reverse=True)                      #argumento reverse=True para ordenar na ordem decrescente
print(lista)

lista2 = [6, 3, 1, 2, 4, 5]
lista2_sorted = sorted(lista2)                #cria uma cópia ordenada em lista2_sorted sem alterar a lista2 original
lista2_reverse = sorted(lista2, reverse=True) #argumento reverse=True para ordenar na ordem decrescente
print(lista2)
print(lista2_sorted)
print(lista2_reverse)


# In[13]:

def sanitize(time_string):
    if '-' in time_string:                      #procura por um - e caso ache entra no if
        splitter = '-'                          #aloca o valor - à variável splitter
    elif ':' in time_string:                    #procura por um : e caso ache entra no elif
        splitter = ':'                          #aloca o valor : à variável splitter
    else:                                       #caso contrário nenhuma ação é necessária
        return(time_string)                     #retornamos o valor de time_string sem modificações
    (mins, secs) = time_string.split(splitter)  #divide time_string pelo valor de splitter
    return(mins + '.' + secs)                   #retorna os valores divididos separados por .


# In[20]:

#compreensão de listas

#transformando lista de minutos em lista de segundos
mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print(secs)

#metros em pés
meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

#minúsculas em maiúsculas
lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

#sanitize criada anteriormente
dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

#strings em floats
clean = [float(s) for s in clean]
print(clean)

#usando com cadeia de funções
clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)


# In[22]:

#código enxuto com compreensão de listas
import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter5')            #muda o diretório
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

with open('james.txt') as jam:                   #abrindo o arquivo
    data = jam.readline()                        #lendo a linha e armazenando em data
james = data.strip().split(',')                  #convertendo os dados em uma lista, encadeamento de métodos... processa da esquerda para a direita
with open('julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])      #maneira direta: print(sorted([sanitize(t) for t in sarah]))

unique_james = []                                 #lista vazia para armazenar james sem duplicatas
for each_item in james:                           #para cada item de james
    if each_item not in unique_james:             #se o item ainda não existe em unique_james
        unique_james.append(each_item)            #adicionamos ele ao final da lista unique_james
        
unique_julie = []
for each_item in julie:
    if each_item not in unique_julie:
        unique_julie.append(each_item)
        
unique_mikey = []
for each_item in mikey:
    if each_item not in unique_mikey:
        unique_mikey.append(each_item)
        
unique_sarah = []
for each_item in sarah:
    if each_item not in unique_sarah:
        unique_sarah.append(each_item)
        
print(unique_james[0:3])                          #print do valores índice 0, 1 e 2 de unique_james, não incluí o índice 3
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])


# In[23]:

#conjuntos
distances = set()

distances = {10.6, 11, 8, 10.6, "two", 7}          #quando criamos um conjunto podemos usar {}, 10.6 no caso irá aparecer apenas uma vez
distances = set(james)                             #transforma james em um conjunto e remove as duplicatas


# In[24]:

#código enxuto com compreensão de listas
import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter5')            #muda o diretório
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

with open('james.txt') as jam:                   #abrindo o arquivo
    data = jam.readline()                        #lendo a linha e armazenando em data
james = data.strip().split(',')                  #convertendo os dados em uma lista, encadeamento de métodos... processa da esquerda para a direita
with open('julie.txt') as jul:
    data = jul.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mik:
    data = mik.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as sar:
    data = sar.readline()
sarah = data.strip().split(',')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


# In[25]:

#código mais enxuto
import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter5')            #muda o diretório
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
    
james = get_data('james.txt')
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
sarah = get_data('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


# In[ ]:




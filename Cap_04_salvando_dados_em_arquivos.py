
# coding: utf-8

# In[15]:

import os
os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter3')            #muda o diretório
os.getcwd()                                                                              #testando se estamos no correto
man = []
other = []
try:
    data = open('sketch.txt')                                                            #abre o arquivo e coloca em data
    for each_line in data:                                                               #for com cada linha obtida de data
        try:
            (role, line_spoken) = each_line.split(':', 1)                                #divide a linha no ':'
            line_spoken = line_spoken.strip()                                            #retira espaços antes e depois do texto
            if role == 'Man':                                                            #testa o responsável da fala
                man.append(line_spoken)                                                  #armazena a fala na lista man   
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass                                                                         #continua o código
    data.close()                                                                         #fecha o arquivo
except IOError:
    print ('The datafile is missing!')
    
try:
    man_file = open('man_data.txt', 'w')                                                 #abre o arquivo em modo gravação
    other_file = open('other_data.txt', 'w')
    
    print(man, file = man_file)                                                          #print salva man em man_file
    print(other, file = other_file)

except IOError:
    print('File error.')
    
finally:                                                                                 #finally é sempre executado
    man_file.close()
    other_file.close()


# In[13]:

try:
    data = open('missing.txt')                         #tentando abrir arquivo que não existe
    print (data.readline(), end='')
except IOError as err:
    print ('File error: ' + str(err))                  #gerando uma msg de erro mais detalhada
finally:
    if 'data' in locals():                             #testa se data está na coleção de nomes locals, são os nomes definidos no escopo atual
        data.close()


# In[14]:

#Uso do with ao invés do padrão acima try, except, finally
try:
    with open('its.txt', "w") as data:                 
        print("It's...", file=data)
except IOError as err:
    print ('File error: ' + str(err))                  #gerando uma msg de erro mais detalhada


# In[16]:

with open('man_data.txt') as mdf:                      #percebemos que o arquivo man_data tem apenas uma grande linha salva
    print(mdf.readline())                              #Aqui solicitamos um print e o resultado é toda a lista


# In[18]:

import sys
import os
def print_lol(the_list, indent = False, level = 0, fh=sys.stdout):
    
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)

os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter3')            #muda o diretório
os.getcwd()                                                                              #testando se estamos no correto
man = []
other = []
try:
    data = open('sketch.txt')                                                            #abre o arquivo e coloca em data
    for each_line in data:                                                               #for com cada linha obtida de data
        try:
            (role, line_spoken) = each_line.split(':', 1)                                #divide a linha no ':'
            line_spoken = line_spoken.strip()                                            #retira espaços antes e depois do texto
            if role == 'Man':                                                            #testa o responsável da fala
                man.append(line_spoken)                                                  #armazena a fala na lista man   
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass                                                                         #continua o código
    data.close()                                                                         #fecha o arquivo
except IOError:
    print ('The datafile is missing!')
    
try:
    with open('man_data.txt', 'w') as man_file:                                          #abre o arquivo em modo gravação
        print_lol(man, fh = man_file)                                                        #print salva man em man_file
    with open('other_data.txt', 'w') as other_file:
        print_lol(other, fh = other_file) 

except IOError:
    print('File error.')


# In[24]:

import pickle
import os

def print_lol(the_list, indent = False, level = 0, fh=sys.stdout):
    
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)

os.getcwd()                                                                              #diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter3')            #muda o diretório
os.getcwd()                                                                              #testando se estamos no correto
man = []
other = []
try:
    data = open('sketch.txt')                                                            #abre o arquivo e coloca em data
    for each_line in data:                                                               #for com cada linha obtida de data
        try:
            (role, line_spoken) = each_line.split(':', 1)                                #divide a linha no ':'
            line_spoken = line_spoken.strip()                                            #retira espaços antes e depois do texto
            if role == 'Man':                                                            #testa o responsável da fala
                man.append(line_spoken)                                                  #armazena a fala na lista man   
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass                                                                         #continua o código
    data.close()                                                                         #fecha o arquivo
except IOError:
    print ('The datafile is missing!')
    
try:
    with open('mydata.pickle', 'wb') as mysavedata:                                      #abre o arquivo em modo gravação binário
        pickle.dump([1, 2, 'three'], mysavedata)                                         #o arquivo salvo tem um próprio protocolo e pode parecer intelegível
    with open('mydata.pickle', 'rb') as myrestoredata:
        a_list = pickle.load(myrestoredata) 
        
    print(a_list)                                                                        #imprime a lista normalmente

except IOError:
    print('File error.')
    
print_lol(a_list)                                                                        #imprime a lista com print_lol


# In[ ]:




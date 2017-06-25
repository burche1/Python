
# coding: utf-8

# In[15]:

import os
os.getcwd()
#diretório que estamos
os.chdir('C:\\Users\\Alexandre\\Desktop\\hfpython_code\\hfpy_code\\chapter3')
#muda o diretório
os.getcwd()
#testando se estamos no correto
data = open('sketch.txt')
#abre o arquivo e coloca em data
print(data.readline(), end='')
print(data.readline(), end='')
#imprime uma linha
data.seek(0)
#volta ao início do arquivo
for each_line in data:
    print(each_line, end='')
#imprime tudo de uma vez
data.close()
#fecha o arquivo


# In[24]:

import os

if os.path.exists('sketch.txt'):                             #testando se o arquivo existe
    data = open('sketch.txt')
    for each_line in data:
        if (each_line.find(':') > 0):                        #if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)    #método split quando encontra :, apenas 1 vez
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
    
    data.close()
    
else:
    print('The data file is missing!')


# In[27]:

try:                                                         #testando se o arquivo existe com try/except
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)    #método split quando encontra :, apenas 1 vez
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:                                   #especifica o erro que queremos ignorar
            pass
    
    data.close()
    
except IOError:                                              #especifica o erro que queremos ignorar
    print('The data file is missing!')


# In[ ]:




import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import re
import csv
from collections import Counter

# file = open("isaacHB.txt","r")
train_text = state_union.raw("/Users/thomasduvinage/Desktop/my_project/isaacHB.txt")
sample_text = state_union.raw("/Users/thomasduvinage/Desktop/my_project/isaacHB.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

double_name_list = []

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            
            regex = re.compile("â[@_#$,%^&()*<>\/|.}{~]") 
      
            for k in words:
                if(regex.search(k) != None): 
                    #print("String is not accepted.", k) 
                    words.remove(k)

                if(k[0] == chr(258)  or k[0] == chr(350) or k[0] == chr(226) or k[0] == chr(194)):
                    words.remove(k)
                
                for letter in k:
                    if(letter.isdigit()):
                        words.remove(k)
                        break

            tagged = nltk.pos_tag(words)

            #print(tagged)

            for p in tagged[:-1]:
                if(p != tagged[:-1]):
                    if(p[1] == 'NNP'):
                        print(tagged[tagged.index(p)])
                        pass

            for p in tagged[:-1]:
                if(p != tagged[:-1]):
                    if(p[1] == 'NNP' and tagged[tagged.index(p)+1][1] == 'NNP'):
                        print(i,tagged[tagged.index(p)+1])
                        double_name_list.append(p[0]+' '+tagged[tagged.index(p)+1][0])
                        pass


    except Exception as e:
        print(str(e))

process_content()

cnt = Counter()

for long_word in double_name_list:
    cnt[long_word] += 1

print(cnt)

for repetition in cnt:
    if(cnt[repetition] == 1):
        print(repetition)
        del cnt[repetition]

print(cnt)


####### the following block enable us to know all the page numbers #########

file = open('isaacHB.txt','r')

res = [int(i) for i in file.read().split() if i.isdigit()] 

## the following part allows us to list all the page numbers
def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
 
tri_bulle(res)

#### the following part permits to delete all numbers repetitions  ####
for k in res:
    if(k  < len(res)):
        if(k == res[res.index(k)+1]):
            res.remove(k)

if(res[len(res)-1] - res[len(res) - 2] != 1):
    res.remove(res[len(res)-1])
    


with open('presence.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
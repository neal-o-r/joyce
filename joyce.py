from nltk import tokenize
import string
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd


def get_txt(filename):

        with open(filename, 'r') as f:
                txt = f.read()

        txt = txt.replace('\n', ' ')
        txt = txt.decode('utf-8')

        return txt


def w_avg(text):

        only_words = text.lower().encode('utf-8').translate(None, string.punctuation)
        words = only_words.split(' ')
        return(sum([len(word) for word in words]) / float(len(words)),
               len(words), len(set(words)))


def sent_avg(text):

        tkn = tokenize.sent_tokenize(text)
        
        nwords = 0
        for sent in tkn:
            nwords += len(sent.split(' '))
        
        avgsent = nwords / float(len(tkn))
        return avgsent


def in_dict(text, dwords):

        text = text.lower()
        only_words = text.encode('utf-8').translate(None, string.punctuation)
        words = only_words.split(' ')

        not_in = 0
        for word in set(words):
                if word not in dwords:
                        not_in += 1
 
        nwords = len(words)
        not_in_pc = 100 * not_in / float(nwords)

        return not_in_pc


with open('small_words.txt', 'r') as f:
        dwords = f.read()
'''
dwords = dwords.lower().split('\n')

dub = get_txt('dub.txt')
fin = get_txt('fw.txt')
uly = get_txt('uly.txt')
poa = get_txt('poa.txt')

text_all = [dub, poa, uly, fin]

years = ['1914', '1916', '1922', '1939']
names = ['Dubliners', 'Portrait of the Artist as a Young Man',
         'Ulysses', 'Finnegans Wake']

avg_w, n_w, n_u = [], [], []
avg_s = []
dict_pc = []
for text in text_all:

        avg, n, n2 = w_avg(text)

        avg_w.append(avg)
        n_w.append(n)
        n_u.append(n2)

        avg_s.append(sent_avg(text))

        dict_pc.append(in_dict(text, dwords))

titles = [i+' ('+j+')' for i,j in zip(names, years)]

d = {'Average_word_length': avg_w, 'Number_of_words': n_w, 
     'Unique_words': n_u, 'Average_sentence_length': avg_s, 
     'PC_words_not_in_dict': dict_pc}

df = pd.DataFrame(data=d, index=titles)

df.PC_words_not_in_dict.plot(style='-o', xlim=[-0.5,3.5], ylim=[0,20])
plt.ylabel('Percentage of words not in dictionary')
plt.savefig('words_not_in_dict.png')

(df.Unique_words / df.Number_of_words).plot(rot=0)
plt.ylabel('Number of Unique Words / Toal Word Count')
plt.savefig('ratio.png')
'''

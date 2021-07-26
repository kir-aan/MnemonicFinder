import requests
from bs4 import BeautifulSoup
import csv

def findMnemonic(word):
    link = 'https://mnemonicdictionary.com/?word=' + word
    page = requests.get(link)
    txt = page.text
    status = page.status_code
    soup = BeautifulSoup(page.content,'html5lib')
    page_body = soup.body
    mnemonicDiv = soup.find('div',attrs={'class':'card-text'})
    mnemonic = ''
    for w in mnemonicDiv.find('p').text.split():
        mnemonic = mnemonic + w + ' '
    print(mnemonic)

    line = {'word':word, 'mnemonic':mnemonic}
    filename = 'mnemonicDictionary.csv'
    with open(filename,'a', newline='') as f:
        w = csv.DictWriter(f,fieldnames=['word','mnemonic'])
        w.writerow(line)
        f.close()


print("Enter the word you want to find mnemonic for: ",end='')
word = input()
findMnemonic(word)

while(True):
    next = input("Do you want to find mnemonic for another word?(Y/N): ")
    if(next=="N"):
        break
    print("Enter the word you want to find mnemonic for: ",end='')
    word = input()
    findMnemonic(word)
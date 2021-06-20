from bs4 import BeautifulSoup
import requests
import sys
import argparse


def stats(language,keyword):
    usr_agent = usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}
    page = requests.get("https://www.google.com/search?q={}&hl={}".format(keyword,language), headers=usr_agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        first = soup.find('div', attrs={'class' : 'EIaa9b'})
        related_keywords = []
        for div in first.findAll('div'):
            if div.text != '':
                related_keywords.append(div.text)
        related_keywords.pop(0)
        related_keywords.pop(4)
    except:
        pass
    try:
        info = soup.find('div', attrs={'id':'result-stats'})
        s = str(info).split(" ")
    except:
        pass
    try:
        result = "{}\n-------------------\n Search volume: {},\n Related Suchanfragen: {}".format(keyword,s[2], related_keywords)
    except:
        result ="error"
    print(result)
    return result

if __name__ == '__main__':
    print("\nstart script\n\n")
    try:
        language = sys.argv[2]
    except:
        language = "en"
    try:
        keyword = sys.argv[1]
    except:
        keyword = "error"
        print("please insert a keyword as argument and try again")
        exit()
    stats(language, keyword)
    #print(stats("What means ghosted"))
    #print(stats("How to improve my SEO?"))
    #print(stats("How much money do I need to surive in Dubai"))
    #print(stats("Average income San Diego"))

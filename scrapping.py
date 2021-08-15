from bs4 import BeautifulSoup
import requests
import os
def main():
    url = "https://news.google.com/news/headlines?ned=in&hl=en-IN&gl=IN"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    path = os.path.abspath(os.path.dirname(__file__))
    #print(path)
    filename = os.path.join(path,'data/scrapped_headlines.txt')
     
#for jupyter"
    #filename = os.path.join("e:\\clustering", 'data\Scrapped_headlines.txt')
    links = soup.find_all("a")
    with open(filename, 'w') as f:
        for link in links:
            text = link.text
            
            headline_length = len(text.split())
            if headline_length > 4 :
                f.write(text)
                f.write('\n')
                
if __name__ == '__main__':
    main()
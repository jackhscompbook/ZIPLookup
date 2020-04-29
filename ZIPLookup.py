
import requests
import bs4
import argparse
from bs4 import BeautifulSoup



class lookerUpper():

    def __init__(self):
        self.logo = '''
 _______       _                 _                
|___  (_)     | |               | |               
   / / _ _ __ | |     ___   ___ | | ___   _ _ __  
  / / | | '_ \\| |    / _ \\ / _ \\| |/ / | | | '_ \\ 
./ /__| | |_) | |___| (_) | (_) |   <| |_| | |_) |
\\_____/_| .__/\\_____/\\___/ \\___/|_|\\_\\__,_| .__/ 
        | |                                | |    
        |_|                                |_|

'''
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('zipCode', type=str, help='Zip Code which gets looked up.')
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}  

    def startUp(self);
        pass
        
    def parseArgs(self):
        self.args = parser.parse_args()

    def getPage(self):
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (args.zipCode), headers=headers)

    def parsePage(self):
        soup = BeautifulSoup(page.text, 'html.parser')
        city = soup.table.tbody.tr.tb




## parser.add_argument('-M', '--moreInfo', action='store_true', help='Use this Tag if you want more information about the Zip Code. (Non Working ATM)')




print('https://www.unitedstateszipcodes.org/%s/' % (args.zipCode))
#print(page.text)
print(page)
print('-------------------------------------------------------------------------------------------------------------------------------')



print('-------------------------------------------------------------------------------------------------------------------------------')

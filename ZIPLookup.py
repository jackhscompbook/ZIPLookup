
import time

import requests
import argparse
from bs4 import BeautifulSoup



class ZIPLookup():

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
        self.parser.add_argument('-M', '--moreInfo', action='store_true', help='Use this Tag if you want more information about the Zip Code. (Non Working ATM)')
        self.parser.add_argument('-d', '--debug', action='store_true', help='Use this flag to activate debug mode, which prints more information about the program as it runs.')
        self.parser.add_argument('-D', '--verboseDB', action='store_true', help='Use this flag to activate verbose debug mode, which prints more information than you want about the program as it runs.')
        self.parser.add_argument('-o', '--offline', action='store_true', help='This flag disables online mode. This mode requires you have the offline zipcode database file in the proper dir. It is stored in ./data/ZIPdata.txt')
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}  

    def startUp(self):  
        self.startTime = time.time()

        self.parseArgs()

        print(self.logo)
        print('Created by a_personlol#2828, contact me if you run into issues.')
        print('Looking up ZIPCode')
        if self.args.debug == True:
            print('[*] Debug mode is active.')
        elif self.args.verboseDB == True:
            print('[%s] verboseDB mode is active (Why did you do this?)' % time.localtime())


        if self.args.offline == True:
            self.getOffline()
            self.displayOffline()
        else:
            self.getPage()
            self.parsePage()
            self.displayPage()

        self.endTime = time.time()
        self.elapsedTime = self.startTime - self.endTime
        
    def parseArgs(self):
        if self.args.debug == True:
            print('[*] Parsing web page...')
            self.args = parser.parse_args()
            print('[*] Done...')

    def getPage(self):
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (args.zipCode), headers=headers)

    def parsePage(self):
        self.soup = BeautifulSoup(page.text, 'html.parser')
        self.city = soup.findAll('td')[0]

    def displayPage(self):
        print(self.city)

    def getOffline(self):
        pass

    def displayOffline(self):
        pass

if __name__ == '__name__':

    ZIPLookup = ZIPLookup()

    ZIPLookup.startUp()

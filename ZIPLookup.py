import requests
import argparse
from bs4 import BeautifulSoup

from random_proxies import random_proxy



class lookerUpper():

    def __init__(self):
        self.logo = [' ',
                    ' _______       _                 _               ',
                    '|___  (_)     | |               | |               ',
                    '   / / _ _ __ | |     ___   ___ | | ___   _ _ __  ',
                    '  / / | | \'_ \\| |    / _ \\ / _ \\| |/ / | | | \'_ \\', 
                    './ /__| | |_) | |___| (_) | (_) |   <| |_| | |_) | ',
                    '\\_____/_| .__/\\_____/\\___/ \\___/|_|\\_\\__,__| .__/ ',
                    '        | |                                | |    ',
                    '        |_|                                |_|',
                    ' '
                    ]
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('zipCode', type=str, help='Zip Code which gets looked up. If you want to look up a range of codes, do this: code1/code2')
        self.parser.add_argument('-d', '--debug', action='store_true', help='Shows extra information as the program runs.')
        self.parser.add_argument('-D', '--verboseDB', action='store_true', help='Like debug, but it shows EVEN more info.')
        self.parser.add_argument('-u', '--userAgent', help='Used to define a userAgent if you don\'t want to use the default one')
        self.parser.add_argument('-p', '--proxy', action='store_true', help='use this option if you want to use a proxy server')
        self.defaultUserAgent = 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
        self.headers = {
                            'authority': 'www.unitedstateszipcodes.org',
                            'cache-control': 'max-age=0',
                            'upgrade-insecure-requests': '1',
                            'origin': 'https://www.unitedstateszipcodes.org',
                            'content-type': 'application/x-www-form-urlencoded',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-user': '?1',
                            'sec-fetch-dest': 'document',
                            'referer': 'https://www.unitedstateszipcodes.org/63131/',
                            'accept-language': 'en-US,en;q=0.9',
                        }
        self.data = {
                      'q':None
                    }
        self.proxies = {
                      'http':None
                    }

        # userAgents = [
        #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        #     'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36',
        #     'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.1.0.26.115 (iPhone11,6; iOS 13_3; en_US; en-US; scale=3.00; 1242x2688; 190542906)',
        #     'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #     'Ancestry 9.13 rv:6189 (iPad; iOS 11.1; en-CA)'
        # ]


    def startUp(self):

        for i in self.logo:
            print(i) 
        print('Made by [REDACTED FOR COLLEGE BOARD] (Contact with issues)')
        print('Looking Up ZIP code...')
        self.parseArgs()
        if self.args.debug == True:
            print('[*] Getting page...')
            if self.args.proxy == True:
                self.getPageProxy()
            else:
                self.getPage()
            print('[*] Done...')
            print('[*] Parsing page...')
            self.parsePage()
            print('[*] Done...')
            print('[*] Displaying City:')
            self.displayCityDB()
        elif self.args.verboseDB == True:
            print('[*] Getting page...')
            if self.args.proxy == True:
                self.getPageProxyVDB()
            else:
                self.getPageVDB()
            print('[*] Done...')
            print('[*] Parsing page...')
            self.parsePageVDB()
            print('[*] Done...')
            print('[*] Displaying City:')
            self.displayCityDB()
        else:
            if self.args.proxy == True:
                self.getPageProxy()
            else:
                self.getPage()
            self.parsePage()
            self.displayCity()

    def parseArgs(self):

        self.args = self.parser.parse_args()

    def getPage(self):

        if self.args

        self.data['q'] = self.args.zipCode
        if self.args.userAgent != None:
            self.headers['user-agent'] = self.args.userAgent
        else:
            pass
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (self.args.zipCode), headers=self.headers)
        #print(self.page)


    def getPageProxy(self):

        self.data['q'] = self.args.zipCode
        self.proxies['http'] = random_proxy(protocol='http')
        if self.args.userAgent != None:
            self.headers['user-agent'] = self.args.userAgent
        else:
            pass
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (self.args.zipCode), headers=self.headers, proxies=self.proxies)
        #print(self.page)

    def getPageProxyVDB(self):

        print('[*]\tDefining data paramter...')
        self.data['q'] = self.args.zipCode
        print('[*]\tDone...')
        print('[*]\tAttempting to assign a user defined UA...')
        if self.args.userAgent != None:
            self.headers['user-agent'] = self.args.userAgent
            print('[*]\t\tUser defined UA assigned as "', end='')
            if len(self.args.userAgent) <= 15:
                print(self.args.userAgent, end='')
            else:
                print(self.args.userAgent[:15], end='')
                print('...', end='')
            print('"')
        else:
            print('[*]\t\tNo user defined UA was specified, using default...')
        print('[*]\tFinding a proxy...')
        self.proxies['http'] = random_proxy(protocol='http')
        print('[*]\tDone (Using proxy [%s])...' % (self.proxies['http']))
        print('[*]\tRequesting page...')
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (self.args.zipCode), headers=self.headers)
        print('[*]\tDone [%s]...' % (self.page))
        #print(self.page)

    def getPageVDB(self):

        print('[*]\tDefining data paramter...')
        self.data['q'] = self.args.zipCode
        print('[*]\tDone...')
        print('[*]\tAttempting to assign a user defined UA...')
        if self.args.userAgent != None:
            self.headers['user-agent'] = self.args.userAgent
            print('[*]\t\tUser defined UA assigned as "', end='')
            if len(self.args.userAgent) <= 15:
                print(self.args.userAgent, end='')
            else:
                print(self.args.userAgent[:15], end='')
                print('...', end='')
            print('"')
        else:
            print('[*]\t\tNo user defined UA was specified, using default...')
        print('[*]\tRequesting page...')
        self.page = requests.get('https://www.unitedstateszipcodes.org/%s/' % (self.args.zipCode), headers=self.headers)
        print('[*]\tDone [%s]...' % (self.page))
        #print(self.page)

    def parsePage(self):

        self.soup = BeautifulSoup(self.page.text, 'html.parser')
        try:
            self.city = self.soup.findAll('td')[0]
            self.city = str(self.city)[4:]
            self.city = self.city[:-44]
        except IndexError as e:
            self.city = 'None Found'

    def parsePageVDB(self):

        print('[*]\tStarting Soup...')
        self.soup = BeautifulSoup(self.page.text, 'html.parser')
        print('[*]\tDone...')
        try:
            print('[*]\tFormatting result...')
            self.city = self.soup.findAll('td')[0]
            self.city = str(self.city)[4:]
            self.city = self.city[:-44]
            print('[*]\tDone...')
        except IndexError as e:
            self.city = 'None Found'

    def displayCityDB(self):
        print('\n\t%s\n' % self.city)

    def displayCity(self):
        print('\nCity: %s\n' % self.city)



if __name__ == '__main__':

    lU = lookerUpper()

    lU.startUp()
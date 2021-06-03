import gevent, requests, sys, re, configparser
from threading import Thread
from queue import Queue
from bs4 import BeautifulSoup

Config = configparser.ConfigParser()
Config.read(sys.path[0] + "/config.conf")
genders = re.sub(' ', '', Config.get('settings', 'genders')).split(",")
lastPage = {'female': 10, 'couple': 10, 'trans': 10, 'male': 10}

q = Queue()
online = []
workers = []


green = '\033[32m'
white = '\033[0m'
red = '\033[31m'

# def getOnlineModels():
#     global lastPage
#     global q
#     global online
#     if not q.empty():
#         args = q.get()
#         page = args[0]
#         gender = args[1]
#         if page < lastPage[gender]:
#             attempt = 1
#             while attempt <= 3:
#                 try:
#                     print('CheckPoint #1')
#                     timeout = gevent.Timeout(8)
#                     timeout.start()
#                     URL = "https://chaturbate.com/{gender}-cams/?page={page}".format(gender=gender.lower(), page=page)
#                     result = requests.request('GET', URL)
#                     result = result.text
#                     soup = BeautifulSoup(result, 'lxml')
#                     print(page)
#                     if lastPage[gender] == 20:
#                         break
#                     print(int(soup.findAll('li', {'class': 'active'})[1].string))
#                     if int(soup.findAll('li', {'class': 'active'})[1].string) == page:
#                         print('CheckPoint #2')
#                         print(int(soup.findAll('li', {'class': 'active'})[1].string))
#                         LIST = soup.findAll('ul', {'class': 'list'})[0]
#                         models = LIST.find_all('div', {'class': 'title'})
#                         for model in models:
#                             online.append(model.find_all('a', href=True)[0].string.lower()[1:])
#                     break
#                 except gevent.Timeout:
#                     print('CheckPoint #3')
#                     attempt = attempt + 1
#                     if attempt > 3:
#                         break

def getOnlineModels2():
    global lastPage
    global q
    global online
    for gender in genders:
        page = 1
        lastP = 0
        whileCount = 0

        # only go through pages upto last page
        while page < lastPage[gender]:
            attempt = 1
            whileCount += 1
            #print('While Count: ' + str(whileCount))

            # if the page is not the same as last
            if lastP != page:
                try:
                    #print('CheckPoint #1')
                    timeout = gevent.Timeout(8)
                    timeout.start()
                    URL = "https://chaturbate.com/{gender}-cams/?page={page}".format(gender=gender.lower(), page=page)
                    result = requests.request('GET', URL)
                    result = result.text
                    soup = BeautifulSoup(result, 'lxml')

                    #print('Page: ' + str(page))
                    #print('Last Page: ' + str(lastP))
                    #if lastPage[gender] == 20:
                        #break
                    #print('Test: ' + str(soup.findAll('li', {'class': 'active'})))

                    #print(green + str(int(soup.findAll('li', {'class': 'active'})[1].string)) + white)
                    lastP = page
                    if int(soup.findAll('li', {'class': 'active'})[1].string) == page:
                        #print('CheckPoint #2')
                        LIST = soup.findAll('ul', {'class': 'list'})[0]
                        models = LIST.find_all('div', {'class': 'title'})
                        for model in models:
                            online.append(model.find_all('a', href=True)[0].string.lower()[1:])
                        page += 1
                        #print(red + 'Page After: ' + str(page) + white)


                except gevent.Timeout:
                    #print('CheckPoint #3')
                    attempt = attempt + 1
                    if attempt > 3:
                        break
            elif lastP == page:
                attempt += 1


# def getModels():
#     global workers
#     for gender in genders:
#         if gender == 'couple':
#             for i in range(1, 3):
#                 q.put([i, gender])
#         else:
#             for i in range(1, 30):
#                 q.put([i, gender])
#     while not q.empty():
#         for i in range(10):
#             t = Thread(target=getOnlineModels)
#             workers.append(t)
#             t.start()
#         for t in workers:
#             t.join()


# if __name__ == '__main__':
#     q = Queue()
#     online = []
#     workers = []
#     getModels()
#     online = list(set(online))
#     #for model in online:
#         #print(model)
# 		return online

def getMs():
    global online
    getOnlineModels2()
    online = list(set(online))
    return online

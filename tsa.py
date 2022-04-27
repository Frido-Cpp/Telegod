from telethon import TelegramClient, events, sync,utils
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
from telethon.tl.functions.channels import InviteToChannelRequest
import time,os,random,csv,sys
import pyautogui
from pathlib import Path
r= "\u001b[31;1m"
a= "\u001b[32m"
y = "\u001b[33;1m"
b="\u001b[34;1m"
m="\u001b[35;1m"
c="\u001b[36;1m"
myfile1 = Path('logs.txt')
myfile1.touch(exist_ok=True)
clear = lambda:os.system('clear')
inf = (y+'||||||>>>['+a+' TELEGRAM'+' '+m+'SCRAPER'+' '+r+'BY'+' '+c+'#CYB3RW4RRIOR'+' '+y+']<<<||||||')
el=0
def Sleep(timE):
    try:
        time.sleep(timE)
    except KeyboardInterrupt:
        print(r+"[!] KeyboardInterrupt , ........")
def info():
    print("")
    print("")
    print(inf)
    print("")
    print("")
clear()
info()
def ospath():
    o=int(input(b+"||||||>>> How many telegram accounts do you have ? : "))
    for po in range(o):
        if os.path.isfile('logs.txt'):
            with open('logs.txt', 'r') as f:
                data = f.readlines()
            v=int(len(data)/2)
            z=v
        else:
            z=0
        api_id= input(b+'||||||>>> Enter api_id_{}: '.format(z+1))
        api_hash= input('||||||>>> Enter api_hash_{}: '.format(z+1))
        with open('logs.txt', 'a') as f:
            f.write(api_id+'\n'+api_hash+'\n')
        client = TelegramClient("CyberWarrior{}".format(z), api_id, api_hash)
        client.start()

        clear()
        info()
        client.disconnect()
if os.path.isfile('logs.txt'):
    cy=input("||||||>>> Wanna add more accounts? "+a+" (y/n) ? ")
    if cy=='y':
        ospath()
    else:
        pass
clear()
info()
x=0
inh=2
t=0
with open('logs.txt', 'r') as f:
    data = f.readlines()
v=int(len(data)/2)
for s in range(v):
    api_id = data[t]
    api_hash = data[t+1]
    print(a+ ' \n[+] Trying... to connect to the Account {} \n'.format(x+1)+y+ ' \n api {}= '.format(x+1) +m+ api_id +'\n' +y+ ' api hash {} = '.format(x+1) +m+ api_hash)
    Sleep(1)
    client = TelegramClient("CyberWarrior{}".format(x), api_id, api_hash)
    client.start()
    name=utils.get_display_name(client.get_me())
    print(a+" \n\n||||||>>>[  Successfully connected as {} ]<<<||||||\n\n".format(name))
    t+=2
    lines=[]
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)
    for chat in chats:
        try:
            if chat.megagroup==True:
                groups.append(chat)
        except:
            continue
    print(b+'[+] Choose a group to scrape members from:')
    i=0
    for g in groups:
        print(m+str(i) +y+ ' - '+a + g.title)
        i+=1
        continue
    path_to_file = 'Members.csv'
    path = Path(path_to_file)
    if path.is_file():
        g_index = input(pyautogui.press('enter', presses=1))
        if g_index == '':
            print(m+"\n[+] Skipping...")
        clear()
    else:
        g_index = input(b+'||||||>>> Enter a number : ')
        target_group=groups[int(g_index)]
        print(y+'[+] Fetching Members...')
        all_participants = []
        all_participants = client.get_participants(target_group)
        print(y+'[+] Saving In file...')
        with open("Members.csv","w",encoding='UTF-8') as f:
            writer=csv.writer(f,delimiter=",",lineterminator="\n")
            writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    username= ""
                if user.first_name:
                    first_name= user.first_name
                else:
                    first_name= ""
                if user.last_name:
                    last_name= user.last_name
                else:
                    last_name= ""
                name= (first_name + ' ' + last_name).strip()
                writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
        print(a+'[+] Members scraped successfully.')
        Sleep(1)
        clear()

    print(b+'[+] Choose a group to add members:\a')
    i=0
    for group in groups:
        print(m+str(i) +y+ ' - ' +a+ group.title)
        i+=1
    g_index = input(b+'||||||>>> Enter a Number: ')
    if g_index=='':
        print(m+" \n[+] U 've pressed Enter,Now exiting...")
        sys.exit()
    input_file = 'Members.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        for row in rows:
            lines.append(row)
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)
    my_participants = client.get_participants(groups[int(g_index)])
    target_group=groups[int(g_index)]
    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
    my_participants_id = []
    for my_participant in my_participants:
        my_participants_id.append(my_participant.id)
    info()
    n,q=0,0
    for user in users:
        usR=str(user['id'])
        n+=1
        if n % 20 == 0:
            info()
            print (y+'[+] waiting for 12 seconds to avoid flooding....')
            Sleep(12)
        elif q>= 9:
            client.disconnect()
            if x<v:
                x+=1
                inh+=1
                break
            else:
                print(b+"[+] No more clients found.Now exiting..")

                sys.exit()
        if user['id'] in my_participants_id:
            print(a+' User already present,skipping...')
            n-=1
            with open('Members.csv', 'r',encoding='UTF-8') as f:
                dat = csv.reader(f,delimiter=",",lineterminator="\n")
                for tad in dat:
                    if usR in tad:
                        lines.remove(tad)
                        break
            Sleep(1)
            continue
        else:
            try:
                print (a+' Adding {}'.format(user['name']))
                if True :
                    if user['username'] == "":
                        continue
                print (a+'[+] Adding {}'.format(user['name']))
                user_to_add = client.get_input_entity(user['username'])
                client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                print(m+"[+] Waiting for 3-5 Seconds...")
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            break
                with open("Members.csv","w",encoding='UTF-8') as f:
                    writer=csv.writer(f,delimiter=",",lineterminator="\n")
                    for line in lines:
                        writer.writerow(line)

                time.sleep(random.randrange(3,5))

                q=0
            except PeerFloodError:
                print(r+'[+] Getting Flood Error from telegram. Script is stopping now. Please try again after some time.')
                x+=1
                break

            except PhoneNumberBannedError:
                print(r+'[!] {} Is Banned.....')

                x+=1
                break

            except UserPrivacyRestrictedError:
                print(r+'[!] The user\'s privacy settings do not allow you to do this. Skipping.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            x+=1
                            break
            except UserBotError:
                print(r+'[!] Can\'t add Bot. Skipping...')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            x+=1
                            break
            except InputUserDeactivatedError:
                print(r+'[!] The specified user was deleted. Skipping...')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            x+=1
                            break

            except UserChannelsTooMuchError:
                print(r+'[!] User in too much channel. Skipping.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            x+=1
                            break

            except UserNotMutualContactError:
                print(r+'[!] Mutual No. Skipped.')
                with open('Members.csv', 'r',encoding='UTF-8') as f:
                    dat = csv.reader(f,delimiter=",",lineterminator="\n")
                    for tad in dat:
                        if usR in tad:
                            lines.remove(tad)
                            x+=1
                            break

            except KeyboardInterrupt:
                i=0
                kst=["switch to next account","stop"]
                for ks in kst:
                    print('\n'+m+ str(i) +y+ ' - ' +a+ ks)
                    i=1
                    keyb=int(input(y+"||||||>>> Enter a number : "))
                    if keyb==1:
                        print(y+" Now Exiting...")
                        sys.exit(1)
                    elif keyb==0:
                        print(a+ " \n\nSwitching... to next account\n\n")
                        x+=1
                        break
            except ValueError as e:
                print(e)
                x+=1
                break

            except Exception as e:
                print(r+'[!] Error:', e)
                print('[+]Trying to continue...')
                q += 1
                continue


import pyttsx3,speech_recognition as sr,pywhatkit,pyautogui as p,time as t,os,datetime,webbrowser as web
listener=sr.Recognizer()
engine=pyttsx3.init()
now= datetime.datetime.now()
today_day=now.strftime("%A")
global receiver
current_time=int(datetime.datetime.now().strftime('%H''%M'))
days_to_check=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
def greeting_teacher():
    answer=p.confirm('Want to greet the teacher')
    if answer=='OK':
        print('HI')
    else:
        print("ELSE BLOCK")

def open_to_do_onenote():
    p.press('winleft')
    p.typewrite('OneNote for Windows 10')
    p.press('enter')
    t.sleep(1.5)
    p.keyDown('alt')
    p.press('tab',2)
    p.keyUp('alt')

def talk(text):
    engine.say(text)
    engine.runAndWait()
def joining_CLASS():
    web.open('https://meet.google.com/lookup/abxfjk3mqz')
    t.sleep(6)
    p.click(x=960,y=540)
    p.hotkey('ctrl', 'e')
    p.hotkey('ctrl', 'd')
    t.sleep(0.2)
    p.click(x=1365, y=625)
    t.sleep(0.5)
    p.click(x=1222, y=375)

    # greeting_teacher()
range_time_min="%04d"%(800,)
range_time_max="%04d"%(930,)
# override
# range_time_min=2256
# range_time_max=2359

if today_day in days_to_check:
    if current_time>int(range_time_min) and current_time<int(range_time_max):
        joining_CLASS()


def console_mode():
        print("\n\n1.VOICE MODE \n\n2.SHUTDOWN OR RESTART \n\n3.DOWNLOAD MATHS LECTURE \n\n4.PLAYMUSIC \n\n5.OPEN FOLDERS FOR STUDYING \n\n6.YOUTUBE \n\n7.CLASS PERIOD \n\n8.GOOGLE SEARCH \n\n9.NNFS")
        user_input_console=input("\n\nGO AHEAD : ")


        if user_input_console=='sd':

            print("SHUTDOWN COMMAND ACTIVATED YOUR PC WILL WIND DOWN IN 20 SECONDS..")
            pywhatkit.shutdown()

        elif user_input_console=='d':
            default()

        elif user_input_console=='nnfs':
            os.startfile('C:\\Users\Adhithya\Desktop\FILES\\NN 81')
            console_mode()

        elif user_input_console=='vm':
            voice_mode()

        elif user_input_console=='of':
            study_MODE_OPEN_FOLDERS()

        elif user_input_console=='math':
            open_to_do_onenote()


        elif user_input_console=='rs':

            print("RESTARTING...")
            p.hotkey('winleft','d')
            t.sleep(0.5)
            p.hotkey('alt','f4')
            p.keyDown('down')
            p.press('enter')


        elif user_input_console=='gs':

            usersaying=input("\n\nYA IAM GOOGLE : ")
            pywhatkit.search(usersaying)

            console_mode()


        elif user_input_console=='m':

            print("PLAYING MUSIC StANDBY")
            p.press('winleft')
            t.sleep(0.1)
            p.typewrite('gr')
            p.press('enter')
            t.sleep(1.5)
            p.click(x=500,y=212)
            p.click(x=1764,y=24)
            console_mode()


        elif user_input_console=='j':
            web.open('https://meet.google.com/lookup/abxfjk3mqz')
            t.sleep(7)
            p.hotkey('ctrl', 'e')
            p.hotkey('ctrl', 'd')
            t.sleep(0.5)
            p.click(x=1365, y=625)
            t.sleep(1.5)
            p.click(x=1222, y=375)
            console_mode()


        elif user_input_console=='yt':
            print("\n\nYOUTUBE MODE ACTIVATED")
            usersaying=input("\n\nTYPE HERE WHAT YOU WANT SEARCH ON YOUTUBE:")
            pywhatkit.playonyt(usersaying)
            console_mode()
        else:
            print("DEI OLUNNGA TYPE PANNU!!(•_•)")
            console_mode()
def ask_user_input():
    try:
        with sr.Microphone() as mic:

            voice_of_user=listener.listen(mic)
            information_processed=listener.recognize_google(voice_of_user)
            return information_processed.upper()
    except:
        pass
def voice_mode():

                print("\nTALK")
                user_input=ask_user_input()

                if user_input=='CLASS':

                    talk("CLASS MODE...")
                    name_of_period = ask_user_input()
                    if today_day == 'Monday':
                        timetable_Monday = {
                            'FIRST PERIOD': 'ENGLISH',
                            'SECOND PERIOD': 'CHEMISTRY',
                            'THIRD PERIOD': 'PROGRAMMING using C',
                            'LAST PERIOD': 'MATHS'

                        }
                        user_input = ask_user_input()
                        receiver = timetable_Monday[name_of_period]
                        print(receiver)


                    elif today_day == 'Tuesday':
                        timetable_Tuesday = {
                            'FIRST PERIOD': 'ICFM',
                            'SECOND PERIOD': 'MATHS',
                            'THIRD PERIOD': 'PROGRAMMING using C',
                            'LAST PERIOD': 'CHEMISTRY'

                        }
                        receiver = timetable_Tuesday[name_of_period]
                        print(receiver)
                    elif today_day == 'Wednesday':

                        timetable_Wednesday = {
                            'FIRST PERIOD': 'PROGRAMMING using C',
                            'SECOND PERIOD': 'MATHS',
                            'THIRD PERIOD': 'ENGLISH',
                            'LAST PERIOD': 'CHEMISTRY'

                        }
                        receiver = timetable_Wednesday[name_of_period]
                        print(receiver)

                    elif today_day == 'Thursday':
                        timetable_Thrusday = {
                            'FIRST PERIOD': 'CHEMISTRY',
                            'SECOND PERIOD': 'PROGRAMMING using C',
                            'THIRD PERIOD': 'MATHS',
                            'LAST PERIOD': 'ICFM'

                        }
                        receiver = timetable_Thrusday[name_of_period]
                        print(receiver)

                    elif today_day == 'Friday':
                        timetable_Friday = {
                            'FIRST PERIOD': 'MATHS',
                            'SECOND PERIOD': 'ENGLISH',
                            'THIRD PERIOD': 'ICFM',
                            'LAST PERIOD': 'PROGRAMMING using C'

                        }
                        receiver = timetable_Friday[name_of_period]
                        print(receiver)

                    elif today_day == 'Saturday':
                        timetable_Saturday = {
                            'FIRST PERIOD': 'PROGRAMMING using C',
                            'SECOND PERIOD': 'ENGLISH',
                            'THIRD PERIOD': 'CHEMISTRY',
                            'LAST PERIOD': 'MATHS'

                        }
                        receiver = timetable_Saturday[name_of_period]
                        print(receiver)

                    else:
                        print("NO CLASS TODAY ")
                        talk('NO CLASS TODAY.....')

                    t.sleep(3)

                elif user_input=='STUDY':
                    study_MODE_OPEN_FOLDERS()

                elif user_input=='JOIN CLASS':
                    joining_CLASS()

                elif user_input=='YOUTUBE':
                    talk("YOUTUBE MODE ACTIVATED")
                    youtube_query=str(ask_user_input())
                    print(youtube_query)
                    print("\n PLAYING NOW SIR")
                    pywhatkit.playonyt(youtube_query)

                elif user_input=='MATHEMATICS':
                    print("SORRY ABaNDED")

                elif user_input=='PLAY MUSIC':
                    talk('PLAYING MUSIC STANDBY....')
                    p.press('winleft')
                    t.sleep(0.1)
                    p.typewrite('gr')
                    p.press('enter')
                    t.sleep(2)
                    p.click(x=500,y=212)
                    p.click(x=1764,y=24)

                elif user_input=='GOOD DAY':
                    print("SHUTDOWN COMMAND ACTIVATED YOUR PC WILL WIND DOWN IN 20 SECONDS..")
                    pywhatkit.shutdown()

                elif user_input=='GOOD DAY AGAIN':
                    talk("WHY SHOULD I?...")
                    print("RESTARTING...")
                    p.hotkey('winleft','d')
                    t.sleep(0.5)
                    p.hotkey('alt','f4')
                    p.keyDown('down')
                    p.press('enter')

                elif user_input=='GAMES':
                    talk("GAME MODE ACTIVATED")
                    def game_selection():
                            game_selection = ask_user_input()
                            if game_selection=='TANGO':
                                print(game_selection)
                                os.startfile('GAMES\BeamNG.drive.exe - Shortcut.lnk')
                                t.sleep(1)
                                p.press('enter')
                            elif game_selection=='TRAIN':
                                print(game_selection)
                                os.startfile('GAMES\TS2Prototype.exe - Shortcut.lnk')
                            elif game_selection=='CRY':
                                print(game_selection)
                                os.startfile('GAMES\farcry3.exe - Shortcut.lnk')
                            elif game_selection == 'MOTO':
                                print(game_selection)
                                os.startfile('GAMES\motogp20.exe - Shortcut.lnk')
                            elif user_input=='TANGO':
                                print("OPENING MATHS PDF")
                                t.sleep(1)
                                p.hotkey('winleft','e')
                                p.click(x=374,y=188)
                                path="B:\REC collage\MAths\PDFS"
                                p.typewrite()
                                p.press('enter')
                            else:
                                talk("PARDON SIR")
                                game_selection()
                    game_selection()

                else:
                    talk("CAN YOU REPEAT IT AGAIN SIR PLEASE....")
                    voice_mode()
def study_MODE_OPEN_FOLDERS():
                    bmfull=[]

                    maths_code='m'
                    icfm_code='i'
                    chemistry_code='c'
                    english_code='e'

                    def mode_selection():
                            p=input("\n\nENTER SUBJECT CODE : ")
                            if p == maths_code:
                                u=input('\n\nWhat pdf ? ')
                                web.open('file:///B:/REC%20collage/MAths/PDFS/UNIT%204/{}.pdf'.format(u))
                                console_mode()
                            elif p=='bm':
                                print("\n\nBulk mode")
                                hm=int(input("HOW MANY PDFS?"))
                                for i in range(hm):
                                    u = input('\n\nWhat pdf ? ')
                                    web.open('file:///B:/REC%20collage/MAths/PDFS/UNIT%204/{}.pdf'.format(u))

                            elif p == chemistry_code:
                                print("\n\nCHEMISTRY MODE")
                                os.startfile('B:\REC collage\CHEMISTRY')
                            elif p==icfm_code:
                                print("\n\nICFM")
                                os.startfile('B:\REC collage\ICFM')
                                console_mode()
                            elif p==english_code:
                                print("\n\nENGLISH MODE")
                                os.startfile('B:\REC collage\ENGLISH')
                                console_mode()
                            else:
                                print("ENTER ANY OF THE FOLLOWING CODE\n1. c for Chemistry\n2. i for ICFM \n3. m for Maths \n4. e for English ")
                                mode_selection()

                    mode_selection()
console_mode()
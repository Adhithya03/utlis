import pyautogui as p,time as t,os,datetime,webbrowser as web
days_to_check=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']#for joining class
current_time=int(datetime.datetime.now().strftime('%H''%M'))
now= datetime.datetime.now()
today_day=now.strftime("%A")

def alt_tab():
    p.hotkey('alt','tab')

def dark_pdf():
	t.sleep(1)
	p.hotkey('ctrl','shift','j')
	t.sleep(0.6)
	p.click(1491,471)
	p.write('var')
	p.press('down')
	p.press('enter')
	p.press('enter')
	p.hotkey('ctrl','shift','j')
	p.hotkey('ctrl','\\')

def math_pdf_opener():
    unit=input("\nUNIT ? ")
    u=input('\nWhat pdf ? ')
    web.open('file:///B:/REC%20collage/MAths/PDFS/UNIT%20{}/{}.pdf'.format(unit,u))
    dark_pdf()

def bulk_pdf_opener():
    hm = int(input("\n\nHOW MANY PDFS?"))
    unit = input("UNIT??")
    for i in range(hm):
        u = input('What pdf ?')
        web.open('file:///B:/REC%20collage/MAths/PDFS/UNIT%20{}/{}.pdf'.format(unit, u))
        t.sleep(0.5)
        alt_tab()
def bulk_mode_2():
	unit = input("\n\nUNIT??")
	from_one=int(input("\n\nChoose till.."))
	for i in range(1,from_one+1,1):
		web.open('file:///B:/REC%20collage/MAths/PDFS/UNIT%20{}/{}.pdf'.format(unit, i))
def open_onenote():
    p.press('winleft')
    t.sleep(0.2)
    p.click(x=655,y=880)
def play_mc_music():
    os.startfile('B:\\TAMIL SONGS MY COLLECTION\\Minecraft FULL SOUNDTRACK ( 256kbps cbr ).mp3')
def joining_CLASS():
    web.open('https://meet.google.com/lookup/abxfjk3mqz/1')
    t.sleep(9)
    while True:
        mic=p.locateCenterOnScreen('''B:\\Python works\\ADHI's assistant\\gmeetimages\\mic.png''')
        vid=p.locateCenterOnScreen('''B:\\Python works\\ADHI's assistant\\gmeetimages\\video.png''')
        join_img = p.locateCenterOnScreen('''B:\\Python works\\ADHI's assistant\\gmeetimages\\join.png''')
        p.click(mic)
        p.click(vid)
        p.click(join_img)
        break
def default_morning():
    range_time_min="%04d"%(800,)
    range_time_max="%04d"%(930,)
    if today_day in days_to_check:
        if current_time>int(range_time_min) and current_time<int(range_time_max):
            joining_CLASS()
def math_mode():
    math_pdf_opener()
    play_mc_music()
    t.sleep(2)
    open_onenote()
def google_mode():
    usersaying = input("\nGOOGLE : ")
    pywhatkit.search(usersaying)

def unmotivated():
    web.open("https://www.youtube.com/watch?v=M7FIvfx5J10&ab_channel=VolvoTrucks&t=0m35s")
    t.sleep(2)
    p.press('f11')
    t.sleep(1.5)
    p.press('f')
    t.sleep(45)
    p.hotkey('ctrl','w')
    web.open("https://www.youtube.com/watch?v=sX1Y2JMK6g8&ab_channel=SpaceflightTV&t=3m08s")



def class_s():
    time=int(input("\n\nChoose any from 30,25,20,15,10,5 mins : "))
    alt_tab()
    if time==30:
        print("\n\nJoining in 30 mins")
        t.sleep(1740)
        joining_CLASS()
    elif time==25:
        print("\n\nJoining in 25 mins")
        t.sleep(1500)
        joining_CLASS()
    elif time==20:
        print("\n\nJoining in 20 mins")
        t.sleep(1200)
        joining_CLASS()
    elif time==15:
        print("\n\nJoining in 15 mins")
        t.sleep(900)
        joining_CLASS()
    elif time==10:
        print("\n\nJoining in 10 mins")
        t.sleep(600)
        joining_CLASS()
    elif time==5:
        print("Joining in 5 mins")
        t.sleep(300)
        joining_CLASS()
    elif time==1:
        print("Joining in 10 secs")
        t.sleep(10)
        joining_CLASS()
    else:
        print("Choose from them 30,20,15,10,5")
def alarm_time_start():
    p.press('winleft')
    p.typewrite('cl')
    p.press('enter')
    t.sleep(1.5)
    p.click(972,263)
    t.sleep(0.5)
    p.click(1889,20)

def youtube_mode():
    usersaying = input("\n\nYOUTUBE:")
    pywhatkit.playonyt(usersaying)
def window_max():
    p.hotkey('winleft','up')
window_max()


def user_choicei():
        user_choice=input("\n\nGo? ").lower()
        if user_choice=='yt':
            youtube_mode()
            user_choicei()
        elif user_choice=='ti':
            alarm_time_start()
        elif user_choice=='cs':
            os.startfile('''B:\\Python works\\ADHI's assistant\\Assitant2.0.py''')
            t.sleep(1.5)
            alt_tab()
            window_max()
            class_s()
        elif user_choice=='um':
            unmotivated()
        elif user_choice=='nnfs':
            os.startfile("C:\\Users\\Adhithya\\Desktop\\FILES\\NNFS.pdf")
        elif user_choice=='omc':
            play_mc_music()
            open_onenote()
        elif user_choice=='sh':
            shield()
        elif user_choice=='mc':
            play_mc_music()
            t.sleep(0.5)
            p.click(1774,19)
        elif user_choice=='g' :
            google_mode()
            user_choicei()
        elif user_choice == 'mwm'  :
            math_mode()
            user_choicei()
        elif user_choice=='bmt':
        	bulk_mode_2()
        elif user_choice == 'm' :
            math_pdf_opener()
            user_choicei()

        elif user_choice == 'j' :
            joining_CLASS()
            user_choicei()
        elif user_choice == 'bmo':
            bulk_pdf_opener()
            user_choicei()

user_choicei()

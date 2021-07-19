cursor="Hi BOSS :) \n---------	 \n"

command=input(cursor)

exam_link			= "https://meet.google.com/lookup/fqjcn7lsmt/?authuser=1"	
class_link			= "https://meet.google.com/lookup/bmzzbz3ygp/?authuser=1"
classroom_maths		= "https://classroom.google.com/u/1/c/MzE0MDc1MzU1MTk2"
classroom_eg		= "https://classroom.google.com/u/1/c/MzE0OTM0NjIzMDIw"
classroom_physics	= "https://classroom.google.com/u/1/c/MzE1ODk0OTEwMzk0"
classroom_civil		= "https://classroom.google.com/u/1/c/MzI1NTU3NDkxNDc0"
classroom_evs		= "https://classroom.google.com/u/1/c/MzE1NjgyMzM1Nzcw"

import pyautogui, time as t, webbrowser as web ,datetime,os,subprocess,random

current_time	= int(t.strftime('%H''%M'))
today_day		= t.strftime("%A")

def random_tut():
	with open("Don't touch\\to watch.txt", 'r') as file:
		lines=file.read().splitlines()
		choice=random.choice(lines)
		web.open(choice)

def explore(path):
	subprocess.run([os.path.join('explorer.exe'), path])

def Startup():
	'''Startup check every moring between 08:30 and 09:05'''
	if today_day == 'Sunday':
	    pass
	else:
		if current_time>=int("%04d"%(830,)) and current_time<=int("%04d"%(905,)):
			gmeet_join(class_link)

def timetable():
	if today_day=='Monday':
		period={"1":"CIVIL",
				"2":"GRAPHICS",
				"3":"MATHS",
				"4":"CIRCUITS",
				"5":"CIRCUITS"}
		print(period.values())

	elif today_day=='Tuesday':
		period={"1":"PHYSICS",
				"2":"CIVIL",
				"3":"CIRCUITS",
				"4":"ENVI",
				"5":"MATHS"}
		print(period.values())

	elif today_day=='Wednesday':
		period={"1":"GRAPHICS",
				"2":"GRAPHICS",
				"3":"ENVI",
				"4":"MATHS",
				"5":"PHYSICS"}
		print(period.values())
			
	elif today_day=='Thursday':
		period={"1":"CIRCUITS",
				"2":"ENVI",
				"3":"MATHS",
				"4":"PHYSICS",
				"5":"CIVIL"}
		print(period.values())
		
	elif today_day=='Friday':
		period={"1":"MATHS",
				"2":"CIRCUITS",
				"3":"PHYSICS",
				"4":"GRAPHICS",
				"5":"GRAPHICS"}
		print(period.values())
		
	elif today_day=='Saturday':
		period={"1":"ENVI",
				"2":"PHYSICS",
				"3":"CIVIL",
				"4":"CIRCUITS",
				"5":"CIVIL"}
		print(period.values())
	else:
		print("\nPoda loose")
	t.sleep(10)

def shot_and_ret(x,y,channel):
    return (pyautogui.screenshot().getpixel((x,y))[channel]) 

def gmeet_join(link):
	web.open(link)
	t.sleep(4)
	while 1:
		# screenshot=pyautogui.screenshot() 
		b=shot_and_ret(1333,666,2)# Red - 0 Green - 1 BLUE - 2  
		if  b > 65 :
			break
	pyautogui.click(620,830)
	pyautogui.click(723,830)
	pyautogui.click(1333,666)

def class_s():
	tm=int(input("\nEnter time in mins :"))
	ts=tm*60
	print(f"Waiting {ts} secs")
	t.sleep(ts)
	gmeet_join(class_link)

def main():

	if command=='j':
		gmeet_join(class_link)
	elif command=='ej':
		gmeet_join(exam_link)
	elif command=='s':
		class_s()
	elif command=='tt':
		timetable()
	elif command=='c':
		web.open(classroom)	
	elif command=='cc':
		web.open(classroom_civil)
	elif command=='cm':
		web.open(classroom_maths)
	elif command=='cp':
		web.open(classroom_physics)
	elif command=='ce':
		web.open(classroom_evs)
	elif command=='cg':
		web.open(classroom_eg)
	elif command=='on':
		web.open('https://www.youtube.com/watch?v=MBRqu0YOH14&&t=3m43s')
	elif command=='cmail':
		web.open('https://mail.google.com/mail/u/1/#inbox')
	elif command=='fc':
		explore('B:\\Collage\\Circuits')
	elif command=='fm':
		explore('B:\\Collage\\Maths')
	elif command=='fg':
		explore('B:\\Collage\\Eng grap')
	elif command=='rt':
		random_tut()
	elif command=='yt':
		web.open("youtube.com")

Startup()

all_commands=['ej','j','yt','s','tt','c','cc','cm','cp','ce','cg','on','cmail','fc','fm','fg','rt']
if command in all_commands: 
	main()
else:
	web.open(f'https://www.google.com/search?q={command}')
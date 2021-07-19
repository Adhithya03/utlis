import time as t,webbrowser as web , pyautogui as pg , os

#I created a file called constants.py as the name impliles it contains all the constants
import constants


#Functions
def join_meet(link):

	def shot_and_ret_pix_color(x,y,channel):
		return (pg.screenshot().getpixel((x,y))[channel])

	web.open(link)
	t.sleep(constants.minimum_cooldown)
	
	while 1:
		result_value = shot_and_ret_pix_color ( constants.join_now_x , constants.join_now_y , constants.channel_to_check )
		if  result_value > constants.threshold :
			break
		
		else :
			t.sleep(constants.interval)

	pg.hotkey("ctrl","e")
	pg.hotkey("ctrl","d")
	pg.click(constants.join_now_x,constants.join_now_y)
	t.sleep(constants.interval)
	#Gmeet spotlight minize button
	pg.click(constants.my_status_x , constants.my_status_y)

command =  input ( constants.cursor )
parsed_command = command.split(" ")

if   command == "j":
	join_meet(constants.gmeet_link)

elif command =="js":
	web.open(constants.gmeet_link)

elif command == "c":
	web.open(constants.classroom_home)

elif command == "mp":
	os.system("disp /rotate:90")

elif command == "ml":
	os.system("disp /rotate:0")

elif parsed_command[0] =="b":
	os.system(f"disp /brightness:{parsed_command[-1]}")

elif parsed_command[0] =="c":
	os.system(f"disp /contrast:{parsed_command[-1]}")

elif parsed_command[0] =="bc":
	os.system(f"disp /brightness:{parsed_command[-1]}")
	os.system(f"disp /contrast:{parsed_command[-1]}")
elif command == "matlab":
	web.open("https://youtu.be/NSSTkkKRabI?t=249")

else:
	web.open(constants.google_query_template + command)

def join_meet(link):

	def shot_and_ret_pix_color(x,y,channel):
		return ()
	import time as t
	import constants
	import pyautogui as pg
	import webbrowser as web
	web.open(link)
	t.sleep(constants.minimum_cooldown)

	while 1:

		result_value = pg.screenshot().getpixel((constants.join_now_x,constants.join_now_y))[constants.channel_to_check] 
		
		if  result_value > constants.threshold :
			break
	t.sleep(0.1)
	pg.hotkey("ctrl","e")
	pg.hotkey("ctrl","d")
	pg.click(constants.join_now_x,constants.join_now_y)

def main():
	
	command =  input ("$ ")

	match command:

		case "j":		
			join_meet(constants.gmeet_link)

		case "ja":
			join_meet("https://meet.google.com/lookup/LearnTogetherWithAdhithya?authuser=1")

		case "t":

			import wget,os
			import glob
			link = input("Paste the URL :")
			link = link.split("=")
			os.chdir(r"D:\My-works\intern\Thumbnails\Inspiration network")
			wget.download(fr"http://img.youtube.com/vi/{link[1]}/maxresdefault.jpg")
			list_of_files = glob.glob("*")
			latest_file = max(list_of_files, key=os.path.getctime)
			os.startfile(latest_file)

		case "x":
			import os
			os.startfile(r"D:\My-works\dev\ahk scripts\latex_obsi.ahk")

		case "l":
			import constants
			from Adafruit_IO import Client, Data
			adafruit_client = Client(constants.ADAFRUIT_IO_USERNAME , constants.ADAFRUIT_IO_KEY)
			light_relay = adafruit_client.feeds('relay1').key
			adafruit_client.send_data(light_relay,1)

		case "ll":
			import constants
			from Adafruit_IO import Client, Data
			adafruit_client = Client(constants.ADAFRUIT_IO_USERNAME , constants.ADAFRUIT_IO_KEY)
			light_relay = adafruit_client.feeds('relay1').key
			adafruit_client.send_data(light_relay,0)

		case "mp2":
			import os
			os.system("disp /device 2 /rotate:90")
		
		case "mp1":
			import os
			os.system("disp /device 1 /rotate:90")

		case "ml1":
			import os
			os.system("disp /device 1 /rotate:0")
		case "ml2":
			import os
			os.system("disp /device 2 /rotate:0")

		case "b1":
			import os
			level = input("Brightness :")
			os.system(f"disp /device 1 /brightness:{level}")
			os.system(f"disp /device 1 /contrast:{level}")

		case "b":
			import os
			level = input("Brightness :")
			os.system(f"disp /device 2 /brightness:{level}")
			os.system(f"disp /device 2 /contrast:{level}")
		case "bs":
			import webbrowser as web
			nameOfBook = input("Book name :")
			web.open(f"https://1lib.net/s/{nameOfBook}")

		case _:
			print("bs - Book search in 1lib.net\n")
			print("\nmp - monitor portrait")
			print("b  - monitor 2 brightness")
			print("b1  - monitor 1 brightness")
			print("ml - monitor landscape")
			print("l  - lights on")
			print("ll - lights off")
			print("ll - lights off")
			print("t  - Download thumbnail")
			print("x  - AutoHotkey script")
			print("ja - Join adhithya meet\n")
			main()
if __name__ == '__main__':
	main()

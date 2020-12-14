import pyautogui
import random
import time
import tkinter
import sys
import threading

def start_cursor_thread():
	print('Screen size is : ', pyautogui.size())

	global i
	i = 3
	while i > 0:
		x = random.randint(0,1365) 
		y = random.randint(0,767)
		pyautogui.moveTo(x,y)
		print('value of i is : ', i)
		time.sleep(3)
		print('current position : ', pyautogui.position())
		i -= 1

def move_my_cursor():
	global t1
	t1 = threading.Thread(target = start_cursor_thread)
	t1.start()

def on_closing():
	top.destroy()
	global i
	i = -1
	print('value of i is : ', i)
	sys.exit(0)
	t1.join()

if __name__ == '__main__':

	global top
	top = tkinter.Tk()
	top.geometry("100x100")
	start_button = tkinter.Button(top, text = "start", command = move_my_cursor)
	start_button.pack()

	stop_button = tkinter.Button(top, text = 'stop', command = on_closing)
	stop_button.pack()

	top.protocol("WM_DELETE_WINDOW", on_closing)
	top.mainloop()
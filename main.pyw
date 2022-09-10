from tkinter import Tk, Frame, Button, PhotoImage
from tkinter.ttk import *
from os import path, startfile
from subprocess import call

root = Tk()
root.title("Windows Explorer Toggle")
root.geometry("325x100")
root.resizable(False, False)

icon_code = 'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAAAAADmVT4XAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAnRSTlMAAHaTzTgAAAACYktHRAD/h4/MvwAAAAd0SU1FB+UGCAACOa2aF1QAAADVSURBVHja7djNCQJBDAbQXUlRFuDNJmzCfmzCm7XYhj+rYANDkHEgKi/HCZk8vsuwO01KqeKaD52Du0GAVXUCAAAAAAAAcekcPP9LAgAAAAAAAHPvq3b9lwQAAAAAAABi1Kv2swkAAAAAAACUAyJrnsbs2Hx1AgAA5YBYkuZtzI5sRX0CAAAAAAAA8Uyazf9H2+y6Y+swW1GfAABAOSD9NlzeveWDifIEAADKAXFPmo/WYTbQMVGeAABAOcBrCABQDoh10ty3DrOBjonyBAAAygFKKfUCr3IY2+NH1/QAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDYtMDhUMDA6MDI6NTUrMDA6MDDrVmeQAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIxLTA2LTA4VDAwOjAyOjU1KzAwOjAwmgvfLAAAAABJRU5ErkJggg=='
root.iconphoto(False, PhotoImage(data = icon_code))

def click_toggle():
	if button["text"] == "Disable Windows Explorer":
		call("TASKKILL /F /IM explorer.exe", shell=True)
		button.configure(text="Enable Windows Explorer")
	else:
		call("start %SystemRoot%\\explorer.exe", shell=True)
		button.configure(text="Disable Windows Explorer")
		
def click_folder():
	startfile(path.dirname(__file__))
			
frame = Frame(root)
frame.pack(pady = 12)			

button = Button(root, text="Disable Windows Explorer", command=click_toggle, width=25)
button.pack()

button_folder = Button(root, text="Open Folder", command=click_folder, width=25)
button_folder.pack()
	  
root.mainloop()
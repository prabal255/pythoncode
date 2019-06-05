import webbrowser
import subprocess
import time
import os


option = int(input("""
press  1 FOR firefox
press  2 FOR fav song in youtube
press  3 FOR seaching on google
press  4 FOR check current date and time
press  5 FOR reboot
"""))
print(option)
type(option)
if option==1:
	subprocess.getoutput("firefox")
elif option==2:
	webbrowser.open_new_tab("https://www.youtube.com/watch?v=JRjkOtnd2Ak")
elif option==3:
	data=input("enter your search")
	webbrowser.open_new_tab("https://www.google.com/#q="+data)
elif option==4:
	print(time.ctime())
elif option==5:
	os.system("reboot");
	
	


#example for UPM
import UPDATE_MODULE
UPDATE_MODULE.admin() #it availables to move files after download
from os import getcwd

UPDATE_MODULE.update_self()

update_available=UPDATE_MODULE.update_check("2022-10-13", "PNG-Prime_Number_Generator")
if update_available==None:
    print("You don't have internet connection.")
elif update_available==True:
    print("Update is available!")
    ask=input("Do you want download it now (Y/n): ")
    ask=ask.upper()
    if ask=="Y":
        if_download=UPDATE_MODULE.download_update_repo("https://github.com/wleng2001/PNG-Prime_Number_Generator", getcwd())
        if if_download==False:
            print("Lost connection file wasn't downloaded")
else:
    print("App is current")

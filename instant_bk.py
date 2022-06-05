######INSTANTBK######
######https://github.com/nunzilor######

import shutil
import os
from pathlib import Path
import pathlib
print()
print("###################START SCRIPT###################")
print()
print("###################INSTANTBK###################")
print()
# ricavo nome user e lo converto stringa
nome_os= (Path.home())

nome_os_str = (os.path.abspath(nome_os))


# dichiaro il percoso per la creazione della cartella e le concateno 

directory = "file_backup"

parent_dir = "\Desktop\\"

nome_dir_concat = nome_os_str + parent_dir  


# Path
path = os.path.join(nome_dir_concat, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '%s' creata :D" %directory)
print()
print("la cartella di trova in '%s' " %nome_dir_concat )
print()
#ciclare tutto per decidere cosa backuppare

#copia dei file thunderbird
def question():
    i = 0
    while i < 2:
        answer = input("fare backup di mthunderbird? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_thunder = "\AppData\Roaming\Thunderbird\\"
            src =  nome_os_str + path_thunder
            dest_aggiunta = "\B_thudner"
            dest = path + dest_aggiunta


            shutil.copytree(src, dest)
            print()
            print("thunderbird_fatto ^_^")

 
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('dimmi si o no,non ho tempo da perdere!')
            else:
                print("dajeeee")


question()



#copia chrome 
def question():
    i = 0
    while i < 2:
        answer = input("fare backup di chrome? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_chrome = "\AppData\Local\Google\\"
            src2 =  nome_os_str + path_chrome
            dest_aggiunta = "\B_chrome"
            dest2 = path + dest_aggiunta


            shutil.copytree(src2, dest2)
            print()
            print("chrome_fatto ^_^")


 
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('dimmi si o no,non ho tempo da perdere!')
            else:
                print("dajeeee")


question()


#copia nordvpn
def question():
    i = 0
    while i < 2:
        answer = input("fare backup di nordvpn? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_nordvpn = r"\AppData\Local\NordVPN\\"
            src3 =  nome_os_str + path_nordvpn
            dest_aggiunta = "\B_nordvpn"
            dest3 = path + dest_aggiunta

            shutil.copytree(src3, dest3)
            print()
            print("nordvpn_fatto ^_^")



 
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('dimmi si o no,non ho tempo da perdere!')
            else:
                print("dajeeee")


question()


#copia desktop
def question():
    i = 0
    while i < 2:
        answer = input("fare backup del desktop? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_desktop = r"\Desktop\\"
            src3 =  nome_os_str + path_desktop
            dest_aggiunta = "\B_desktop"
            dest3 = path + dest_aggiunta

            shutil.copytree(src3, dest3)
            print()
            print("desktop_fatto ^_^")



 
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('dimmi si o no,non ho tempo da perdere!')
            else:
                print("dajeeee")


question()

#copia desktop
def question():
    i = 0
    while i < 2:
        answer = input("fare backup del download? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_download = r"\Downloads\\"
            src3 =  nome_os_str + path_download
            dest_aggiunta = "\B_Downloads"
            dest3 = path + dest_aggiunta

            shutil.copytree(src3, dest3)
            print()
            print("Donwload_fatto ^_^")



 
            break
        elif any(answer.lower() == f for f in ['no', 'n', '0']):
            print("No")
            break
        else:
            i += 1
            if i < 2:
                print('dimmi si o no,non ho tempo da perdere!')
            else:
                print("dajeeee")


question()






print()
print("GRAZIE PER AVER USATO INSTANTBK")


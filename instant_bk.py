######INSTANTBK######
######https://github.com/nunzilor######

import shutil
import os
from pathlib import Path
import pathlib
from tkinter.messagebox import YES
print()
print("###################START SCRIPT###################")
print()
print("###################INSTANTBK###################")
print()
print("###################################################################################")
print("################### ATTENZIONE SE SI DECIDERE DI COPIARE I FILE ###################")
print("###################     LE APPLICAZIONI VERRANO CHIUSE          ###################")
print("###################################################################################")
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
            
            os.system("TASKKILL /F /IM thunderbird.exe")
            path_thunder = r"\AppData\Roaming\Thunderbird\\"
            src0 =  nome_os_str + path_thunder
            dest_aggiunta = "\B_thunder"
            dest0 = path + dest_aggiunta


            shutil.copytree(src0, dest0)
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
            
            os.system("TASKKILL /F /IM chrome.exe")
            path_chrome = r"\AppData\Local\Google\\"
            src1 =  nome_os_str + path_chrome
            dest_aggiunta = "\B_chrome"
            dest1 = path + dest_aggiunta


            shutil.copytree(src1, dest1)
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


#copia firefox
def question():
    i = 0
    while i < 2:
        answer = input("fare backup di firefox? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            #os.system chiude l'app prima di salvare i file
            os.system("TASKKILL /F /IM firefox.exe")
            path_firefox = r"\AppData\Roaming\Mozilla\Firefox\\"
            src2 =  nome_os_str + path_firefox
            dest_aggiunta = "\B_firefox"
            dest2 = path + dest_aggiunta

            shutil.copytree(src2, dest2)
            print()
            print("firefox_fatto ^_^")



 
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



#copia path_vpnsophos
def question():
    i = 0
    while i < 2:
        answer = input("fare backup di vpnsophos? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_vpnsophos = r"C:\Program Files (x86)\Sophos"
            src3 = path_vpnsophos
            dest_aggiunta = "\B_vpnsophos"
            dest3 = path + dest_aggiunta

            shutil.copytree(src3, dest3)
            print()
            print("vpnsophos_fatto ^_^")



 
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
            src4 =  nome_os_str + path_desktop
            dest_aggiunta = "\B_desktop"
            dest4 = path + dest_aggiunta

            shutil.copytree(src4, dest4)
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
            src5 =  nome_os_str + path_download
            dest_aggiunta = "\B_Downloads"
            dest5 = path + dest_aggiunta

            shutil.copytree(src5, dest5)
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



#copia documenti
def question():
    i = 0
    while i < 2:
        answer = input("fare backup dei documenti? yes o no)")
        if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
            
           
            path_documents = r"\Documents\\"
            src6 =  nome_os_str + path_documents
            dest_aggiunta = "\B_Documents"
            dest6 = path + dest_aggiunta

            shutil.copytree(src6, dest6)
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


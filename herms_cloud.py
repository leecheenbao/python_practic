#coding:utf-8
import requests
import time
import os
import re
import datetime
import smtplib

start = time.time()
now=datetime.datetime.now()

for root, dirs, files in os.walk("."):
    for name in files:
        if name.endswith(".txt") and "hermes_sac" in name:
            previousFileName=str(os.path.join(root,name))            
print(previousFileName)


list1=[]
with open(previousFileName,"r") as file:
    contents=file.readlines()
    for line in contents:
        if line != "\n":
            list1.append(line)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; ×64) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

url = "https://www.hermes.com/fr/fr/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/#fh_view_size=36&country=fr&fh_location=--%2Fcategories%3C%7Bwomenbagsbagsclutches%7D&fh_start_index=72|relevance|Ligne"

r=requests.get(url,headers=headers)
print(r)
# r=requests.get("https://www.youtube.com/")

newfilename="./hermes_sac_"+str(now.month)+"_"+str(now.day)+"_"+str(now.hour)+"_"+str(now.minute)+".txt"
with open(newfilename,"w") as file:
    file.write(r.text)


end1 = time.time()
print("request and create file time",end1 - start)


list2=[]
with open(newfilename,"r") as file:
    contents=file.readlines()
    for line in contents:
        if line != "\n":
            list2.append(line)



print("list1 size = " + str(len(list1)))
print("list2 size = " + str(len(list2)))
pattern=re.compile(r"[Pp]icotin|[Ll]indy|[Gg]arden [Pp]arty")
i=1
while i < len(list2):
    if list2[i] not in list1:#here, compare the two document
            print("-----------------------Differ-------------------at------"+str(i)+"---------")
        
            if re.findall(pattern,list2[i]):
                print("yes")
                name_of_bag=str(set(re.findall(pattern,list2[i])))
                def send_email():
                # creates SMTP session 
                    s = smtplib.SMTP('smtp.gmail.com', 587) 
                # start TLS for security 
                    s.starttls() 
                # Authentication 
                    s.login("leecheenbao@gmail.com", "6421Bomb") 
                # message to be sent 
                    message = """Today, """+name_of_bag+"""\n is/are available online, please check the adresse below

https://www.hermes.com/fr/fr/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/#positionsku=H075142CKAA||

"""
                # sending the mail 
                    s.sendmail("#######*******@gmail.com", "clientname@foxmail.com", message) 
                # terminating the session 
                    s.quit()
                send_email()
                print(name_of_bag)

    i+=1
    
# os.remove(previousFileName)
         
end2 = time.time()
print("open file and compare difference time",end2 - start)
    

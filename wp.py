#!/usr/bin/python
import requests
import mechanize
import re

banner = """
 __      ____________   ____ ___                           
/  \    /  \______   \ |    |   \______ ___________  ______
\   \/\/   /|     ___/ |    |   /  ___// __ \_  __ \/  ___/
 \        / |    |     |    |  /\___ \\  ___/|  | \/\___ \ 
  \__/\  /  |____|     |______//____  >\___  >__|  /____  >
       \/                           \/     \/           \/ 
       v.1.0.0
       wordpress user finder
       ~vidura Supun~\n\n"""
print(banner)
address = input("Enter the address of the wordpress website: ")
print("\n1.rest API\n2.URL append\nSkip to try both")

method = input("\nEnter the number of decision\n")

def main():
    if method=="1":
        first()
    elif method=="2":
        second()
    else:
        first()

def first():
    
    try:
        r = requests.get(address+"/wp-json/wp/v2/users/1")
        string = r.json()
        print("\n"+"\n"+"Author is:"+string.get("slug"))
    except:
        second()   
    
def second():
    try:
        for i in range(50):
            r = requests.get(address+"/?author="+str(i))
            text = r.text
            user = text[text.find('<title>') + 7 : text.find('</title>')]
            if i==0:
                siteName = user 
            elif "page not found" in r:
                break
            else:
                new = re.sub(r'[^A-Za-z0-9\s]+', '', user)
                print(new.replace(siteName,""))
    
        
    except:
        print("seems these vulnerabilities are patched in the site!!!")
    

if __name__== "__main__":
    main()
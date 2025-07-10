import subprocess

def listsaved()->list:
    str="nmcli -f NAME connection show"
    result1 = subprocess.run(["bash","-c",str], capture_output=True, text=True)
    output1 = result1.stdout
    output1=output1.split('\n')
    output1 = [x.strip() for x in output1 if x != '']
    output1=output1[1:]
    return output1


def listavailable()->dict:
    """
    Returns a dictionary {SSID:[Strength,Security]}
    where security:True if Network is secure,False if Network is open
    """
    available="nmcli -t -f SSID,SIGNAL,SECURITY device wifi list | sort -t: -k2 -nr | awk -F: '!seen[$1]++'"
    result2 = subprocess.run(["bash","-c",available], capture_output=True, text=True)
    output2 = result2.stdout
    output2=output2.split('\n')
    output2 = [x for x in output2 if x != '']
    avail={} #{'A':['Strength':int,'Security':bool]}
    for i in output2:
        first=i[:i.index(':')]
        i=i[i.index(':')+1:]
        second=i[:i.index(':')]
        i=i[i.index(':')+1:]
        third=i[:-1]
        second=int(second)
        if second>80 and second<=100:
            second = '5'
        elif second>60 and second<=80:
            second = '4'
        elif second>40 and second<=60:
            second = '3'
        elif second>20 and second<=40:
            second = '2'
        else:
            second = '1'
        if third=='':
            third='' #network is open
        else:
            third='🔒' #network is secured
        avail[first]=[second,third]
    return avail


def listwifi()->tuple:
    """
    Returns an list [SavedAndAvailable,OnlyAvailable]
    where SavedAndAvailable->dict{SSID:Strength}
          OnlyAvailable->dict{SSID:Strength}
    """
    saved=listsaved()
    available=listavailable()
    savednavailable={}
    onlyavailable={}
    for i in available:
        if i in saved:
            savednavailable[i]=available[i]
        else:
            onlyavailable[i]=available[i]
    fulldict=(savednavailable,onlyavailable)
    return fulldict


def SavedConnect(ssid)->bool:
    """
    Connects to the given WiFi network given it is a Saved Network.
    """
    res=subprocess.run(["bash","-c",f"nmcli dev wifi connect {ssid}"], capture_output=True, text=True)
    result=res.stdout
    print('SavedConnect Result :',result,end='\n\n')
    if len(result)==0:
        return False
    else:
        return True

def UnsavedConnect(ssid)->bool:
    """
    Connects to the given WiFi network given it is a Saved Network.
    """
    res=subprocess.run(["bash","-c",f"nmcli dev wifi connect {ssid}"], capture_output=True, text=True)
    result=res.stdout
    print('SavedConnect Result :',result,end='\n\n')
    if "successfully" in result:
        return True
    else:
        return False





if __name__=="__main__":
    str1="comm -12 <(nmcli -t -f NAME connection show | sort) <(nmcli -t -f SSID device wifi list | sort)"
    str2="comm -23 <(nmcli -t -f SSID device wifi list | sort | uniq) <(nmcli -t -f NAME connection show | sort | uniq)"
    saved="nmcli -f NAME connection show"
    available="nmcli -t -f SSID,SIGNAL device wifi list | sort -t: -k2 -nr | awk -F: '!seen[$1]++'"
    result1 = subprocess.run(["bash","-c",saved], capture_output=True, text=True)
    result2 = subprocess.run(["bash","-c",available], capture_output=True, text=True)
    output1 = result1.stdout
    output2 = result2.stdout
    output1=output1.split('\n')
    output2=output2.split('\n')
    output1 = [x.strip() for x in output1 if x != '']
    output2 = [x for x in output2 if x != '']
    output1=output1[1:]
    avail={}
    print(type(output2))
    print(type(output2[0]))
    for i in output2:
        ind=i.index(':')
        lhs=i[:ind]
        rhs=i[ind+1:]
        avail[lhs]=rhs
    print(avail)
    print('saved : ',output1)
    print('Available : ',output2)

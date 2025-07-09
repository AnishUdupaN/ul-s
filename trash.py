import subprocess
import wifilists
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
        if third=='':
            third=False #network is secured
        else:
            third=True #network is open
        avail[first]=[second,third]
    return avail


xyz=wifilists.listwifi()
print(xyz[0])
print(xyz[1])

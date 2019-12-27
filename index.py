import subprocess
import getMac 
import setArgs



def mac_changer(interface , new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    print("[+] Changing MAC address of interface " + interface + " to " + new_mac)
    command = subprocess.check_output(["ifconfig",interface])
    mac = getMac.get_mac_from_string(command)
    return mac
    

print("************ Hello To MAC Changer Program *********")
options = setArgs.get_args()
command = subprocess.check_output(["ifconfig",options.interface])
mac_in_begenning = getMac.get_mac_from_string(command)
print("the current mac address is : " + mac_in_begenning)
current_mac = mac_changer(options.interface , options.new_mac)
if options.new_mac == current_mac :
    print("congratulation your MAC Has Changed to " + options.new_mac)
else :
    print("Invalid Mac Address!")




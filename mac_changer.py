import subprocess
import re
from optparse import OptionParser

def get_args():
    parser = OptionParser()
    parser.add_option(
        "-i" ,
        "--interface",
        dest="interface",
        help="The interface that want to change it mac address"
    )
    parser.add_option(
        "-m" ,
        "--mac",
        dest="new_mac",
        help="The new mac address"
    )

    (options , args ) = parser.parse_args()

    if  not options.interface :
        parser.error("you have to provide an interface ,use --help for more details")
    elif not options.new_mac :
        parser.error("you have to provide a new MAC ,use --help for more details")
    else :
        mac_list = options.new_mac.split(":")
        #regular expr that check is that a valid mac 
        mac_cheker = r'[\d,a-f,A-Z]{2}'

        if len(mac_list) != 6 :
            parser.error("this is an invalid MAC Adress")

        for mac_elem in mac_list:
            if not (re.match(mac_cheker , mac_elem) and len(mac_elem) == 2) :
                parser.error("this is an invalid MAC Adress")

    return options

def mac_changer(interface , new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    print("[+] Changing MAC address of interface " + interface + " to " + new_mac)
    print("congratulation your MAC Has Changed to " + new_mac)

    # while True : 
    #     error = False
    #     mac_list = new_mac.split(":")
    #     if len(mac_list) != 6 :
    #         print("this is an invalid MAC Adress \n\n")
    #         continue
    #     # regular expr that check is that a valid mac 
    #     mac_cheker = r'[\d,a-f,A-Z]{2}'

    #     for mac_elem in mac_list:
    #         if not (re.match(mac_cheker , mac_elem) and len(mac_elem) == 2) :
    #             error = True

    #     if not error:
    #         break

    #     print("this is an invalid MAC Adress \n\n")

print("************ Hello To MAC Changer Program *********")
options = get_args()
mac_changer(options.interface , options.new_mac)




from optparse import OptionParser
import re

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
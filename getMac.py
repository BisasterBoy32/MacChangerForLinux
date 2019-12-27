import re

def get_mac_from_string(string):
    mac_regx = r'(:?[\d,a-f,A-F]{2}){6}'
    mac = re.search(mac_regx ,string)
    if mac:
        mac = mac.group()
    return mac
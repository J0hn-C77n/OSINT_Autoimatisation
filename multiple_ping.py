#python 3.11.7

import os

hosts = input('specify path to file \n$ ')
print ('\n')


        # add quiet mode
        # add filtering to Host Up | Host DOWN | Host is Not Known






#quiet_mode = input('would you like to receive only result of scan? \nyes / no \n$ ')
#print ('\n')
#is_up_or_known = input('Would you like to know is host is UP, DOWN and ')

def pure_scan(hosts):

    for DNS_name in open(hosts,'r'):
        response = os.system("ping -c 1 " + DNS_name)
    print()  # This print is for testing purposes only, but maybe it's going to stay here


        
#def quiet(hosts):
        



pure_scan(hosts)

import os

hosts = input('specify path to file \n$ ')
print ('\n')
quiet_mode = input('would you like to recive only result of scan? \ny|n \n$ ')
print ('\n')
is_up_or_known = input('Would you ike to know is host is UP, DOWN and ')

def pure_scan(hosts):

    for DNS_name in open(hosts,'r'):
        response = os.system("ping -c 1 " + DNS_name)
    print()


        # add quiet mode
        # add filtering to Host Up | Host DOWN | Host is not Known
        
#def quiet(hosts):
        



pure_scan(hosts)
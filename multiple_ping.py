import subprocess
from typing import List

hosts = input('specify path to file \n$ ')


def pure_scan(hosts_file) -> List[str]:
    result = list()
    with open(hosts_file, "r") as file:
        for dns_name in file:
            dns_name = dns_name.rstrip()
            response = subprocess.run(['ping', '-c', '1', dns_name], text=True, capture_output=True)
            if response.stdout != '':
                result.append(dns_name)
    return result


print(*pure_scan(hosts), sep="\n")

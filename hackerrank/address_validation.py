# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# number = int(input())

# def valid_IPv4(address):
#     try:
#         host_bytes = address.split('.')
#         valid = [int(b) for b in host_bytes]
#         valid = [b for b in valid if b >= 0 and b <= 255]
#         return len(host_bytes) == 4 and len(valid) == 4
#     except:
#         return False

import re

def validate_addresses(addresses):
    # ipv4
    byte = '([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])'
    ipv4_regex = '^{0}(\.{0}){{3}}$'.format(byte)
    ipv4_pattern = re.compile(ipv4_regex)
    
    # ipv6
    hex_group = '[0-9A-Fa-f]{1,4}'
    ipv6_regex = '^({0})(:{0}){{7}}$'.format(hex_group)
    ipv6_pattern = re.compile(ipv6_regex)
    
    for address in addresses:
        if ipv4_pattern.match(address):
            print('IPv4')
        elif ipv6_pattern.match(address):
            print('IPv6')
        else:
            print('Neither')

if __name__ == '__main__':
    address_count = int(input())
    addresses = (input() for _ in range(address_count))
    validate_addresses(addresses)
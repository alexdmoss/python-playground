from ipaddress import IPv4Address, ip_address

ip_addresses = ("191.168.0.1", "127.0.0.1", "12.34.56.78", "192.168.0.300", "1.0x2.3.4", "2001:0db8:85a3:0000:0000:8a2e:0370:7334")

def validate_ip_address(ip: str) -> bool:
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

def validate_ipv4_address(ip: str) -> bool:
    try:
        return isinstance(ip_address(ip), IPv4Address)
    except ValueError:
        return False

print(f'{"IP Address":<40} | Valid | IPv4?')
print(f'{56*"-"}')
for ip in ip_addresses:
    print(f'{ip:<40} | {str(validate_ip_address(ip)):<5} | {validate_ipv4_address(ip)}')

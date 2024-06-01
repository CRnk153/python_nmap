import nmap
from sys import version
import configparser

config = configparser.ConfigParser()

config.read('cfg.ini')

target_hosts = config['Settings']['target_hosts']
target_ports = config['Settings']['target_ports']
print(target_hosts)
for target_host in target_hosts:
    if target_host.startswith("https://"):
        target_host = target_host[len("https://"):]
        target_host = target_host[:-1]

# nmap_path = r"" # For strict calling
nm = nmap.PortScanner()  # nmap_search_path=(nmap_path,)

def run():
    nm.scan(hosts=target_hosts, ports=target_ports)
    for host in nm.all_hosts():
        print('-----------------------------------------')
        print(f'Хост: {host}')
        print('Статус:', nm[host].state())

        for proto in nm[host].all_protocols():
            print('-----------------------------------------')
            print(f'Протокол: {proto}')

            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port]['name']
                print(f'Порт: {port}\tСтан: {state}\tСервіс: {service}')

if __name__ == '__main__':
    print(f"Running program on nmap {nmap.PortScanner.nmap_version(nm)}, python {version}")
    run()
input("Press Enter to exit...")

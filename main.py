import nmap
from sys import version

nmap_path = r""  # Write your path to Nmap folder
nm = nmap.PortScanner(nmap_search_path=(nmap_path,))

target_hosts = ""  # Specify needed hosts to scan
target_ports = ""  # Specify needed ports in the format "start_port-end_port" e.g. "22-443"

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
    input()

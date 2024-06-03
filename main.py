import nmap
import configparser
from sys import version
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def read_config_with_crlf(file_path):
    with open(file_path, 'rb') as file:
        content = file.read().decode('utf-8')
    
    if '\n' in content and '\r\n' not in content:
        content = content.replace('\n', '\r\n')
    
    config = configparser.ConfigParser()
    config.read_string(content) 
    return config

# Read the configuration file
file_path = 'cfg.ini'
config = read_config_with_crlf(file_path)

try:
    target_hosts = config['Settings']['target_hosts']
    target_ports = config['Settings']['target_ports']
except KeyError as e:
    print(f"{Fore.RED}KeyError: {e} not found in the configuration file.")
    exit(1)

nm = nmap.PortScanner()

def check_http_response(host):
    try:
        response = requests.get(f"http://{host}")
        print(f"{Fore.GREEN}HTTP Response for {host}: {response.status_code} {response.reason}")
    except requests.RequestException as e:
        print(f"{Fore.RED}HTTP check failed for {host}: {e}")

def run():
    print(f"{Fore.CYAN}Target Hosts: {target_hosts}")
    print(f"{Fore.CYAN}Target Ports: {target_ports}")
    for target_host in target_hosts.split(', '): 
        print(f"{Fore.BLUE}Scanning {target_host} on ports {target_ports}")
        try:
            nm.scan(hosts=target_host, ports=target_ports)

            for host in nm.all_hosts():
                print(f'{Fore.GREEN}-----------------------------------------')
                print(f'{Fore.YELLOW}Host: {host}')
                print(f'{Fore.YELLOW}Status: {nm[host].state()}')

                for proto in nm[host].all_protocols():
                    print(f'{Fore.BLUE}-----------------------------------------')
                    print(f'{Fore.BLUE}Protocol: {proto}')

                    ports = nm[host][proto].keys()
                    for port in ports:
                        state = nm[host][proto][port]['state']
                        service = nm[host][proto][port]['name']
                        print(f'{Fore.MAGENTA}Port: {port}\tState: {state}\tService: {service}')

        except Exception as e:
            print(f"{Fore.RED}{target_host} wasn't scanned due to unexpected error: {e}")

if __name__ == '__main__':
    print(f"{Fore.GREEN}Running program on nmap {nmap.PortScanner.nmap_version(nm)}, python {version}")
    run()
    input(f"{Fore.CYAN}Press Enter to exit...")

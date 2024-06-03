import configparser

def read_config_with_crlf(file_path):
    with open(file_path, 'rb') as file:
        content = file.read().decode('utf-8')  # Read file as binary and decode to string
    
    # Normalize line endings to ensure they are CRLF
    if '\n' in content and '\r\n' not in content:
        content = content.replace('\n', '\r\n')
    
    config = configparser.ConfigParser()
    config.read_string(content)  # Parse the normalized string
    return config

# Usage example
file_path = 'cfg.ini'
config = read_config_with_crlf(file_path)

# Debug: Print sections and options to verify they were read correctly
print("Sections found:", config.sections())
for section in config.sections():
    print(f"Section [{section}] has options: {config.options(section)}")

try:
    target_hosts = config['Settings']['target_hosts']
    target_ports = config['Settings']['target_ports']
    print("Target Hosts:", target_hosts)
    print("Target Ports:", target_ports)
except KeyError as e:
    print(f"KeyError: {e} not found in the configuration file.")
echo "Please specify the target hosts and ports in cfg.ini"
read -p "Enter target hosts: " target_hosts
read -p "Enter target ports: " target_ports

echo "[Settings]" > cfg.ini
echo "target_hosts = $target_hosts" >> cfg.ini
echo "target_ports = $target_ports" >> cfg.ini

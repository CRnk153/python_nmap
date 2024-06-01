#!/bin/sh

echo "Please specify the target hosts and ports in cfg.ini"
read -p "Enter target hosts separating by comma: " target_hosts
read -p "Enter target ports: " target_ports

target_hosts=$(echo "$target_hosts" | tr ',' '\n')

echo "hello world"
echo "[Settings]" > cfg.ini
echo "target_hosts =" >> cfg.ini

for host in $target_hosts; do
    echo "$host" >> cfg.ini
done

echo "target_ports = $target_ports" >> cfg.ini

python "main.py"
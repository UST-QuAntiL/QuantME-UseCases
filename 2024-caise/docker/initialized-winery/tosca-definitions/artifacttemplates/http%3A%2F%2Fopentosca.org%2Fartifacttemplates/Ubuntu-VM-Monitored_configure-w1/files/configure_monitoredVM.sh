#!/bin/bash

sudo apt-get update -y

sudo apt-get install -y curl

sudo apt-get install -y jq

name=$(hostname)

cpu_name=$(lscpu | grep 'Model name' | cut -f 2 -d ":" | awk '{$1=$1}1')

cpu_cores=$(grep -c processor /proc/cpuinfo)

ram=$(free -m | awk '/Mem:/ { print $2 }')

disk_size=$(df | awk '$NF=="/"{printf "%d", $2}')

payload="{\"name\": \"$name\", \"cpu\": \"$cpu_name\", \"cpuCores\": \"$cpu_cores\", \"ramSize\": \"$ram\", \"diskSize\": \"$disk_size\"}"

response=$(curl -sb -X POST -H "accept: application/hal+json" -H "Content-Type: application/json" -d "$payload" "$QProvEndpoint/virtual-machines")

id=$(echo "$response" | jq -r '.id')

mkdir ~/monitoring

cat > ~/monitoring/monitoring.sh<< EOF
while true
do
# Get CPU usage as a percentage
cpu_usage=\$[100-\$(vmstat 1 2|tail -1|awk '{print \$15}')]

cpu_speed=\$(cat /proc/cpuinfo | grep 'cpu MHz' | cut -f 2 -d ":" | awk '{\$1=\$1}1' |head -1)

# Get memory usage as a percentage
mem_usage=\$(free | grep Mem | awk '{print (\$3 / \$2) * 100}')

disk_usage=\$(df | awk '\$NF=="/"{printf "%d", \$5}')


# Create a JSON payload
payload="{\"cpuUsage\": \"\$cpu_usage\", \"clockSpeed\": \"\$cpu_speed\", \"ramUsage\": \"\$mem_usage\", \"diskUsage\": \"\$disk_usage\", \"recordingTime\": \"\$(date '+%Y-%m-%dT%H:%M:%S.%3NZ')\"}"

# Send data to the endpoint using cURL
echo \$payload
curl -X PUT -H "accept: application/hal+json" -H "Content-Type: application/json" -d "\$payload" "$QProvEndpoint/virtual-machines/$id/characteristics"
sleep 90
done
EOF

chmod +x ~/monitoring/monitoring.sh

nohup bash ~/monitoring/monitoring.sh &

sleep 1

echo "Successfulls set up Monitoring Agent."
#!/bin/sh
docker exec -it attacker /bin/bash -c '
read -p "Press any key to continue... " -n1 -s
tcpreplay -i eth0 --mbps=100 -l 1000 AttackSimulationDataSet.pcap'
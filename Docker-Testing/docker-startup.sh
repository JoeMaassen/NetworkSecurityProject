#!/bin/sh
docker image load -i Docker-Testing/Docker-Image.tar
docker compose rm -f
docker compose pull

cp ../IDS.py IDS.py
cp ../trained_model.pkl trained_model.pkl
cp ../label_encoder.pkl label_encoder.pkl
cp ../Data/AttackSimulationDataSet.pcap AttackSimulationDataSet.pcap
docker compose up --build -d
rm IDS.py
rm trained_model.pkl
rm label_encoder.pkl
rm AttackSimulationDataSet.pcap

gnome-terminal -- bash -c "sh ./Docker-Testing/target.sh; exec bash"
gnome-terminal -- bash -c "sh ./Docker-Testing/attacker.sh; exec bash"
read -p "Press any key to stop the containers... " -n1 -s
docker container stop target attacker

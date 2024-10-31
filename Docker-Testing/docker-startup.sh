#!/bin/sh
docker image load -i Docker-Image.tar
docker compose rm -f
docker compose pull

cp ../IDS/IDS.py IDS.py
cp ../PreTrainedModels/trained_model_srf.pkl trained_model.pkl # Here change the path to get a diffrent model
cp ../PreTrainedModels/label_encoder.pkl label_encoder.pkl
cp ../Data/AttackSimulationDataSet.pcap AttackSimulationDataSet.pcap
cp ../Data/smallerAttackSimulation.pcap smallerAttackSimulation.pcap

docker compose up --build -d
rm IDS.py
rm trained_model.pkl
rm label_encoder.pkl
rm AttackSimulationDataSet.pcap
rm smallerAttackSimulation.pcap

gnome-terminal -- bash -c "sh ./Docker-Testing/target.sh; exec bash"
gnome-terminal -- bash -c "sh ./Docker-Testing/attacker.sh; exec bash"
read -p "Press any key to stop the containers... " -n1 -s
docker container stop target attacker

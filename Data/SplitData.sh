#!/bin/sh
editcap  SSDP_Flood_pcap.pcap  TrainingDataSet.pcap 3669539-4077266
editcap  -r SSDP_Flood_pcap.pcap  AttackSimulationDataSet.pcap 3669539-4077266
editcap -r AttackSimulationDataSet.pcap  toBeDuplicated.pcap 406728-407728
yaf -i TrainingDataSet.pcap -o flowsTraining.flw
yafscii -i flowsTraining.flw -o TrainingDataset.csv --tabular
python3 duplicate.py
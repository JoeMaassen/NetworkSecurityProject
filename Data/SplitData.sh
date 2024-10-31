#!/bin/sh
editcap  SSDP_Flood_pcap.pcap  TrainingDataSet.pcap 3669539-4077266
editcap  -r SSDP_Flood_pcap.pcap  AttackSimulationDataSet.pcap 3669539-4077266
editcap -r AttackSimulationDataSet.pcap  toBeDuplicated.pcap 406728-407728
yaf -i TrainingDataSet.pcap -o flowsTraining.flw
yafscii -i flowsTraining.flw -o TrainingDataset.csv --tabular
sed -i '1i start-time             |end-time               |duration|rtt     |proto|sip                                   |sp   |dip                                     |dp   |iflags  |uflags  |riflags |ruflags |isn     |risn    |tag|rtag|pkt    |oct     |rpkt    |roct    |end-reason' TrainingDataset.csv
python3 duplicate.py
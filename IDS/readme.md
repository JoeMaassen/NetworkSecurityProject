This is the implementation for the Intrusion Detection System. The IDS loads the pre-trained models and uses them to classify the incoming data. 
The IDS must be run with sudo (scapy requires root privilleges).
And the model that is used for classification needs to be manually placed into this folder. The file for the model should be named `trained_model.pkl` and should be a pickle file.
The IDS generates locally a pcap composed of the pakcets for the particular pakcet window, a pcap containing the ipfix flows and the csv file containing the features extracted from the packets.
Finally, whenever the IDS detects a malicious flow it stores in the `IDS.log` file with the timestamp of the detection and the flow that was detected as malicious.
This is the implementation for the Intrusion Detection System. 

The IDS loads a pre-trained model and uses it to classify the incoming data. It accepts two flags to configure the packet window -m for the maximum number of packets in the window and -t for the time window in seconds.

It must be run with sudo (scapy requires root privilleges).

The model that is used for classification needs to be manually placed into this folder.

The file for the model should be named `trained_model.pkl` and should be a pickle file as well as a `label_encoder.pkl` file for the labels.

The IDS generates locally a pcap composed of the pakcets for the particular pakcet window, a pcap containing the ipfix flows and the csv file containing the features extracted from the packets.

Finally, whenever the IDS detects a malicious flow it stores it in the `IDS.log` file with the timestamp of the detection and the flow that was detected as malicious.

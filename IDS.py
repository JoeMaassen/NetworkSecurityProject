from scapy.all import sniff, send, IP, TCP, UDP,wrpcap
import os
import pandas as pd
import time
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import joblib
import pickle

with open('trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Loading the label encoder
with open('label_encoder.pkl', 'rb') as encoder_file:
    loaded_label_encoder = pickle.load(encoder_file)

# Function to classify packets


# Function to handle the packet processing
def packet_callback(packet):
    
    if IP in packet:
            packet_buffer.append(packet)
    print("Packet: "+str(len(packet_buffer)))
    if (len(packet_buffer) == 10000):
        wrpcap('buffer.pcap', packet_buffer)
        packet_buffer.clear()
        packetsToFlow()

def packetsToFlow():
    os.system("yaf -i buffer.pcap -o flows.flw")
    time.sleep(2)
    os.system("yafscii -i flows.flw -o flows.csv --tabular")
    file_name = 'flows.csv'
    header = 'start-time             |end-time               |duration|rtt     |proto|sip                                   |sp   |dip                                     |dp   |iflags  |uflags  |riflags |ruflags |isn     |risn    |tag|rtag|pkt    |oct     |rpkt    |roct    |end-reason\n'

    # Step 2: Read the existing contents of the file (if it exists)
    try:
        with open(file_name, 'r') as file:
            original_contents = file.read()
    except FileNotFoundError:
        # If the file doesn't exist, set original_contents to an empty string
        original_contents = ''

    # Step 3: Write the header and the original contents back to the file
    with open(file_name, 'w') as file:
        file.write(header)         # Write the header
        file.write(original_contents)  # Write the original conten
    print("Flow file created and headers added!")
    extractFlowFeatures()

def extractFlowFeatures():
    df = pd.read_csv ('flows.csv', sep='|')
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    df['start-time'] = pd.to_datetime(df['start-time'])
    df['end-time'] = pd.to_datetime(df['end-time'])
    le = LabelEncoder()
    #df['proto'] = le.fit_transform(df['proto'])
    #df['tag'] = le.fit_transform(df['tag'])
    #df['rtag'] = le.fit_transform(df['rtag'])
    #df['sp'] = le.fit_transform(df['sp'])
    X = df.drop(columns=['start-time','end-time', 'sip','dip','dp','iflags','uflags','ruflags','riflags','isn','risn','end-reason'])
    classifyFlow(X)

def classifyFlow(X):
    counter = 0
    y_pred = model.predict(X)
    #print(X.head())
    print(y_pred)
    #print("Flow classified!")
    for i in range(len(y_pred)):
        if y_pred[i] == True:
            counter += 1
        else:
           print(X.iloc[i])
    #print("Flow classification done!")
    print("Number of malicious flows: "+str(counter))
    exit()



# Sniff all incoming traffic
print("Sniffing incoming traffic...")
packet_buffer = []
sniff(iface='eth0', prn=packet_callback, store=0)  # Specify the correct interface
# sniff(offline = 'capture.pcap', prn=packet_callback, store=0)
####Block spiaddress when malicious traffic is detected
####Use proper os subprograms
import argparse
from scapy.all import sniff, send, IP, TCP, UDP,wrpcap
import os
import pandas as pd
import time
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pickle
import subprocess
import logging
from imblearn.ensemble import BalancedRandomForestClassifier

# Function to check the timer
def check_timer():
    elapsed_time = time.time() - start_time

    return elapsed_time

# Function to reset the timer
def reset_timer():
    global start_time
    start_time = time.time()





# Function to either append or anallyze the packets depending on the specification of the window
def packet_callback(packet):
    
    if( len(packet_buffer)%1000==0):
        print("Packets sniffed: "+str(len(packet_buffer)))
    if IP in packet:
            packet_buffer.append(packet)

    if (len(packet_buffer) == MaxPackets or check_timer() >= TimeWindows) and len(packet_buffer) > 0:
 
        wrpcap('buffer.pcap', packet_buffer)
        packet_buffer.clear()
        packetsToFlow()

# Function to convert packets to flows
def packetsToFlow():

    subprocess.run(["yaf -i buffer.pcap -o flows.flw"],shell=True)
    time.sleep(1)

    subprocess.run(["yafscii -i flows.flw -o flows.csv --tabular"],shell=True)
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

    extractFlowFeatures()

# Function to extract features from the flows
def extractFlowFeatures():
    df = pd.read_csv ('flows.csv', sep='|')
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    df['start-time'] = pd.to_datetime(df['start-time'])
    df['end-time'] = pd.to_datetime(df['end-time'])
    X = df.drop(columns=['start-time','end-time', 'sip','dip','dp','iflags','uflags','ruflags','riflags','isn','risn','end-reason','sp'])
    if not 'proto' in model.feature_names_in_ :
        X = X.drop(columns=['proto'])
    classifyFlow(X)

# Function to classify the flows
def classifyFlow(X):
    if len(X) == 0:
        return
    print("Classifying flows...")
    counter = 0
    y_pred = model.predict(X)
    for i in range(len(y_pred)):
        if y_pred[i] == True:
            logging.warning(X.iloc[i])
            counter += 1
    print("Number of malicious flows: "+str(counter))
    print("We assume all flows are malicious and obtain the following accuracy: "+str(counter/len(X)))
    reset_timer()








parser = argparse.ArgumentParser(description="A simple AI based IDS.")
parser.add_argument("-t", "--min_time", type=int, help="Minimum number of seconds to sniff traffic for(default 20). Time is relative to the first packet recieved for the window .May run for less if MAX PACKETS is reached")
parser.add_argument("-m", "--max_packets", type=int, help="Maximum number of packets to sniff(default 10000)")
args = parser.parse_args()

with open('trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Loading the label encoder
with open('label_encoder.pkl', 'rb') as encoder_file:
    loaded_label_encoder = pickle.load(encoder_file)






logging.basicConfig(
    filename="ids.log",  # Log file name
    filemode="a",        # Append to the file (use 'w' to overwrite)
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO    # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)


packet_buffer = []
start_time = time.time()
if args.min_time:
    TimeWindows=args.min_time
else:
    TimeWindows=20

if args.max_packets:
    MaxPackets=args.max_packets 
else:
    MaxPackets=10000

print("Configuration:")
print("Time window: "+str(TimeWindows))
print("Max packets: "+str(MaxPackets))


sniff(iface='eth0', prn=packet_callback, store=0)  # Specify the correct interface
# sniff(offline = 'capture.pcap', prn=packet_callback, store=0)
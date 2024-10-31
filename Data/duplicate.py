from scapy.all import rdpcap, wrpcap
 
# Read the pcap file
packets = rdpcap('toBeDuplicated.pcap')

# Duplicate packets
print("Duplicating packets...")
duplicated_packets = []

for packet in packets:
    for i in range(20):
        duplicated_packets.append(packet)


print("Packets duplicated!")
# Save the new pcap file with duplicated packets
wrpcap('smallerAttackSimulation.pcap', duplicated_packets)

print(f"Duplicated {len(packets)} packets, saved in duplicated_output.pcap")

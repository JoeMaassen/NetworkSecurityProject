
# Setup
To run the docker enviorment you need to download this file <https://drive.google.com/file/d/1lboCA1lhzEcceZhXjaH-JMQHJmcBwx8f/view?usp=sharing> and put it into this folder.

The data files mentioned in the Data/readme.mk file are also required.

# Running

After cd-ing into this directory run the docker-startup.sh shell script. It should startup the docker containers and open two new terminals. These terminals each open up to one of the docker containers.

You can change the parameters for the commands in the attacker.sh and target.sh files respectivly.

# Our Parameters

## Small Packet Window
In attacker.sh:
```
tcpreplay -i eth0 --mbps=60 -l 1000 smallerAttackSimulation.pcap.pcap
```

In target.sh:
```
python3 IDS.py -m 10000 -t 10
```

## Large Packet Window
In attacker.sh:
```
tcpreplay -i eth0 --mbps=60 -l 1000 AttackSimulationDataSet.pcap'
```

In target.sh:
```
python3 IDS.py -m 500000 -t 200
```

Results might be smaller than documentation. We know that the this data contains benign flows but the IDS assumes that everything is malicious for calculating the results so the results are aproximates.


# Known issues and Solutions

## File Name after copy
Once during testing the docker-startup.sh file it changed the file names by adding a character to the end. 
If this happens you need to delete that additional character  and then run the files one by one manually.


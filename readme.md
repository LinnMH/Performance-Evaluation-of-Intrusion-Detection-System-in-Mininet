# Mininet SYN Flood Attack and Intrusion Detection System Analysis

## Project Overview
This project simulates an 8-pod Mininet network to analyze the effectiveness of intrusion detection systems (IDS) in detecting SYN flood attacks. The network includes hosts where one initiates a SYN flood attack, while another serves as the victim. Traffic between hosts, including both attack and benign flows, is monitored and processed to match the IDS2017 dataset format. The processed dataset is tested with machine learning models (Random Forest and J48) in Weka to evaluate IDS performance.

## Steps

### Setup Mininet Network
1. Build an 8-pod Mininet network using provided code (based on assignment 1).

### Establish Connection Between Hosts
2. Use flow rules to set up a connection between `h0_1` (attacker) and `h0_5` (victim).

### Monitor and Capture Traffic
3. Capture traffic using `tcpdump` for both attack and benign flows.

### Launch SYN Flood Attack
4. Initiate a SYN flood from `h0_1` to `h0_5`.

### Simulate Benign Traffic
5. Create benign connections between `h0_1` and `h0_5` to simulate normal traffic.

### Extract Features from Captured Traffic
6. Use `tshark` to extract features from both attack and benign traffic captures.

### Data Preparation
7. Standardize the feature set to match IDS2017 format, label attack and benign flows, and convert files to ARFF format for Weka.

### Combine Datasets
8. Merge attack and benign datasets into a single dataset.

### Model Testing in Weka
9. Use IDS2017 as the training set and the combined dataset as the test set in Weka. Test using Random Forest and J48 models.

## Tools and Technologies
- **Mininet**: Network emulation
- **Wireshark and tcpdump**: Traffic monitoring and capturing
- **tshark**: Feature extraction from packet captures
- **Weka**: Machine learning tool for model testing and analysis

## Results
The confusion matrix generated from Random Forest and J48 models in Weka provides insights into IDS performance in distinguishing attack and benign traffic.

## Project Structure
- **src**
    - **attack dataset**: Scripts and data for attack flow processing.
    - **benign dataset**: Scripts and data for benign flow processing.
    - **preprocessing**: Scripts for feature extraction, ARFF conversion, and dataset merging.
    - **setup mininet**: Mininet setup scripts.

## Usage

### Set up Mininet
1. Open a terminal in your project’s working directory and enter:
   ```bash
   sudo mn --custom Custom_FatTree_8Pods.py --topo=fattree --link=tc,bw=8,delay=3ms --arp --mac --controller=none

### Establish Connection Between Hosts
2. In the same directory, run `flow_all.sh` to establish the connection between `h0_1` and `h0_5`.

### Capture Attack Packets
3. In the Mininet terminal, enter:
   ```bash
   h0_5 tcpdump -i h0_5-etho -w h0_5_attack.pcap &
4.  Launch the SYN flood attack with:
   ```bash
   h0_1 hping3 -S -p 80 10.0.0.5 -c 1000 
```
### Stop Attack Packet Capture
5.  When the attack traffic is captured, stop it by running:
   ```bash
   h0_5 pkill -f tcpdump
```
### Capture Benign Packets
6.  Start capturing benign packets:
   ```bash
    h0_5 tcpdump -i h0_5-etho -w h0_5_attack_benign.pcap &
```
### Simulate Benign Traffic
7.  Simulate benign communication between h0_1 and h0_5:
   ```bash
    h0_5 nc -l 1234 &
    h0_1 yes "continuous benign traffic" | nc 10.0.0.5 1234
```
### Stop Benign Packet Capture
8.  Stop capturing benign traffic by running:
   ```bash
    h0_5 pkill -f tcpdump
```
### Extract Attack Features
9.  Extract attack features from h0_5_attack.pcap to a CSV file:
   ```bash
    tshark -r h0_5_attack.pcap -T fields -E separator=, -E quote=d -e tcp.stream -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e frame.len -e frame.time_delta_displayed -e tcp.flags.syn -e tcp.flags.fin -e tcp.flags.ack > extracted_features.csv
```
### Extract Benign Features
10.  Extract benign features from h0_5_attack_benign.pcap to a CSV file:
   ```bash
    tshark -r h0_5_attack_benign.pcap -T fields -E separator=, -E quote=d -e tcp.dstport -e frame.time_delta_displayed -e frame.len -e tcp.flags.fin -e tcp.flags.syn > benign_extracted_features.csv
```
### Process Attack Data
11.  Process the attack data CSV to match the format of IDS2017:
   ```bash
    python3 reorded_features.py
```
### Process Benign Data
12.  Process the benign data CSV to match the format of IDS2017:
   ```bash
    python3 reorded_benign_features.py
```
### Normalize Data
13.  Ensure format consistency with the IDS2017 dataset for both attack and benign data:
   ```bash
    python3 match_column.py
```
### Label Data
14.  Open the generated CSV files (reordered_features_2017_format.csv and reordered_benign_features_2017_format.csv) and manually add a Label column:
     For attack data, set the label as DoS.
     For benign data, set the label as BENIGN.
### Combine Datasets
15.  Use the Combine.java file to merge the attack and benign datasets. Ensure the paths are correct, then run:
   ```bash
    java Combine
```
### Convert to ARFF Format
16.  Convert Combine.csv to ARFF format for use in Weka.
### Train and Test Models in Weka
Import the IDS2017_train.csv file into Weka as the training set.
Delete columns in the training set that are not present in Combine.csv, then save the updated file as ARFF.
Open Weka, load the training file, and select your model (e.g., J48 or Random Forest).
Load Combine.arff as the test set and start the training and testing process.
### Optional: Add 20% DoS Data to Training Set
To include additional DoS data in the training set, update ARFFAppender.java to include paths to DoS.arff and IDS2017_train_filtered_noDoS.arff, then run:
   ```bash
    java ARFFAppender
```
Use the generated IDS2017_train_filtered.arff file for training as described in step 16.
### Analyze Dataset
Use Directory2017CSVProcessor.java to analyze the IDS2017 dataset for attack types, quantities, and proportions.

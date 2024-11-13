# Mininet SYN Flood Attack and Intrusion Detection System Analysis

## Project Overview
This project involves creating an 8-pod Mininet network to simulate communication between hosts, where one host serves as an attacker launching a SYN flood attack, and another host acts as the victim. The traffic between the hosts, including both attack and benign flows, is monitored using Wireshark. The captured traffic is processed into CSV format, standardized to match the IDS2017 dataset's features. The final dataset is then used in Weka for testing with machine learning models like J48 and Random Forest to generate a confusion matrix and analyze the results.

## Steps
1. **Setup Mininet Network**
   - Build an 8-pod Mininet network using existing code (from assignment 1).

2. **Establish Connection Between Hosts**
   - Run `flow_rules` commands to establish a connection between `h0_1` and `h0_5`.

3. **Monitor Traffic with tcpdump**
   - Use `tcpdump` to monitor the port and capture traffic data.

4. **Launch SYN Flood Attack**
   - Use `h0_1` as the attacker machine to launch a SYN flood attack targeting `h0_5` (victim machine).

5. **Capture Attack Traffic**
   - Stop capturing traffic after collecting enough attack flows.

6. **Simulate Benign Traffic**
   - Open a port using `nc 1234` and simulate SSH-like connections from the attacker machine to the victim machine, sending multiple benign messages.

7. **Capture Benign Traffic**
   - Stop capturing benign traffic once enough flows have been collected.

8. **Extract Features from Traffic Data**
   - Use `tshark` commands to extract features and generate separate datasets for attack and benign traffic.

9. **Label Data**
   - Add a label column to identify attack and benign flows. Process the 2017 dataset, selecting matching features to ensure consistency with the test dataset's format.

10. **Convert CSV to ARFF Format**
    - Use custom code to convert the CSV files into ARFF format for Weka compatibility.

11. **Combine Datasets**
    - Merge the two ARFF files (attack and benign) into a single dataset.

12. **Model Testing in Weka**
    - Import the IDS2017 dataset as the training set in Weka and use the combined dataset as the test set. Test using Random Forest and J48 models to generate a confusion matrix and analyze the results.

## Tools and Technologies
- **Mininet**: Network emulation
- **Wireshark and tcpdump**: Traffic monitoring and capturing
- **tshark**: Feature extraction from packet captures
- **Weka**: Machine learning tool for model testing and analysis

## Results
The final confusion matrix obtained from testing with the Random Forest and J48 models in Weka provides insights into the effectiveness of the intrusion detection models in classifying attack and benign traffic.

## Project Structure
- **src**
  - **attack dataset**: Contains scripts and data for attack flow processing.
  - **benign dataset**: Contains scripts and data for benign flow processing.
  - **preprocessing**: Contains utility scripts for feature extraction, ARFF conversion, and dataset merging.
  - **setup mininet**: Contains Mininet setup scripts.

## Usage
1. Set up Mininet with the provided configurations.
2. Run attack and benign traffic simulations as described.
3. Extract features and process the data to match IDS2017 dataset format.
4. Import data into Weka and run model testing.

## Author
Bowen Zhang, Chao Li, Zhifeng huang



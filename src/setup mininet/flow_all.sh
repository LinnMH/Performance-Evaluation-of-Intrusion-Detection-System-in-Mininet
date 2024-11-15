# h1(0_1)-h5(0_5), h4(0_4)-h5(0_5)
sudo ovs-ofctl add-flow e0_1 in_port=5,actions=output:1
sudo ovs-ofctl add-flow e0_1 in_port=8,actions=output:1
sudo ovs-ofctl add-flow a0_1 in_port=5,actions=output:6
sudo ovs-ofctl add-flow e0_2 in_port=1,actions=output:5

sudo ovs-ofctl add-flow e0_2 in_port=5,actions=output:1
sudo ovs-ofctl add-flow a0_1 in_port=6,actions=output:5
sudo ovs-ofctl add-flow e0_1 in_port=1,actions=output:5,output:8

# h17(1_1) - h52(3_4),  h20(1_4) - h25(1_9)
sudo ovs-ofctl add-flow e1_1 in_port=5,actions=output:2
sudo ovs-ofctl add-flow e1_1 in_port=8,actions=output:2
sudo ovs-ofctl add-flow a1_2 in_port=5,actions=output:4,output=7
sudo ovs-ofctl add-flow c8 in_port=2,actions=output:4
sudo ovs-ofctl add-flow a3_2 in_port=4,actions=output:5
sudo ovs-ofctl add-flow e3_1 in_port=2,actions=output:8
sudo ovs-ofctl add-flow e1_3 in_port=2,actions=output:5

sudo ovs-ofctl add-flow e1_3 in_port=5,actions=output:2
sudo ovs-ofctl add-flow e3_1 in_port=8,actions=output:2
sudo ovs-ofctl add-flow a3_2 in_port=5,actions=output:4
sudo ovs-ofctl add-flow c8 in_port=4,actions=output:2
sudo ovs-ofctl add-flow a1_2 in_port=4,actions=output:5
sudo ovs-ofctl add-flow a1_2 in_port=7,actions=output:5
sudo ovs-ofctl add-flow e1_1 in_port=2,actions=output:5,output=8

# h113(7_1) - h126(7_14), h116(7_4) - h125(7_13)
sudo ovs-ofctl add-flow e7_1 in_port=5,actions=output:4
sudo ovs-ofctl add-flow e7_1 in_port=8,actions=output:4
sudo ovs-ofctl add-flow a7_4 in_port=5,actions=output:8
sudo ovs-ofctl add-flow e7_4 in_port=4,actions=output:6,output:5

sudo ovs-ofctl add-flow e7_4 in_port=6,actions=output:4
sudo ovs-ofctl add-flow e7_4 in_port=5,actions=output:4
sudo ovs-ofctl add-flow a7_4 in_port=8,actions=output:5
sudo ovs-ofctl add-flow e7_1 in_port=4,actions=output:5,output=8


import pandas as pd

# 读取tshark生成的CSV文件
df = pd.read_csv('extracted_features.csv', names=[
    "Stream", "Src IP", "Dst IP", "Src Port", "Dst Port",
    "Packet Length", "Time Delta", "SYN Flag", "FIN Flag", "RST Flag"
])

# 定义2017 IDS数据集的完整特征顺序，并按顺序包括我们实际提取的字段
columns_order = [
    'Destination Port', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Total Length of Fwd Packets', 'Total Length of Bwd Packets', 'Fwd Packet Length Max', 
    'Fwd Packet Length Min', 'Fwd Packet Length Mean', 'Fwd Packet Length Std', 
    'Bwd Packet Length Max', 'Bwd Packet Length Min', 'Bwd Packet Length Mean', 
    'Bwd Packet Length Std', 'Flow Bytes/s', 'Flow Packets/s', 'Flow IAT Mean', 
    'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Fwd IAT Mean', 
    'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 
    'Bwd IAT Std', 'Bwd IAT Max', 'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 
    'Fwd URG Flags', 'Bwd URG Flags', 'Fwd Header Length_1', 'Bwd Header Length',
    'Fwd Packets/s', 'Bwd Packets/s', 'Min Packet Length', 'Max Packet Length', 
    'Packet Length Mean', 'Packet Length Std', 'Packet Length Variance', 
    'FIN Flag Count', 'SYN Flag Count', 'RST Flag Count', 'PSH Flag Count', 
    'ACK Flag Count', 'URG Flag Count', 'CWE Flag Count', 'ECE Flag Count', 
    'Down/Up Ratio', 'Average Packet Size', 'Avg Fwd Segment Size', 
    'Avg Bwd Segment Size', 'Fwd Header Length', 'Fwd Avg Bytes/Bulk', 
    'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk', 
    'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate', 'Subflow Fwd Packets', 
    'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes', 
    'Init_Win_bytes_forward', 'Init_Win_bytes_backward', 'act_data_pkt_fwd', 
    'min_seg_size_forward', 'Active Mean', 'Active Std', 'Active Max', 'Active Min', 
    'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min', 'Label'
]

# 将已提取的列映射到2017数据集的列名
df = df.rename(columns={
    "Dst Port": "Destination Port",
    "Time Delta": "Flow Duration",
    "Packet Length": "Total Length of Fwd Packets",  # 需进一步处理以区分方向
    "SYN Flag": "SYN Flag Count",
    "FIN Flag": "FIN Flag Count",
    "RST Flag": "RST Flag Count"
   
})

# 填充缺失的列，以符合完整的列顺序
for col in columns_order:
    if col not in df.columns:
        df[col] = None  # 填充缺失列为空值

# 重新排列列顺序并创建副本
df_reordered = df[columns_order].copy()

# 移除所有空列（即全为NaN的列）
df_reordered.dropna(axis=1, how='all', inplace=True)

# 移除没有目的端口的行（即 'Destination Port' 列为空的行）
df_reordered = df_reordered.dropna(subset=['Destination Port'])

# 保存到新的CSV文件
df_reordered.to_csv('reordered_features_no_empty_rows.csv', index=False)

print("Features reordered, empty columns and rows removed, and saved to 'reordered_features_no_empty_rows.csv'")

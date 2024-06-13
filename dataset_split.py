import os
import shutil
import random

def split_dataset(input_folder, train_folder, test_folder, train_ratio=0.8):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    # 获取输入文件夹中的所有文件
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    
    # 打乱文件列表
    random.shuffle(files)
    
    # 计算训练集和测试集的大小
    train_size = int(len(files) * train_ratio)
    
    # 分配文件到训练集和测试集
    train_files = files[:train_size]
    test_files = files[train_size:]
    
    # 复制文件到相应的文件夹
    for f in train_files:
        shutil.copy(os.path.join(input_folder, f), os.path.join(train_folder, f))
    for f in test_files:
        shutil.copy(os.path.join(input_folder, f), os.path.join(test_folder, f))

# 使用示例
input_folder = "./dataset/all/tree"  # 替换为你的输入文件夹路径
train_folder = "./dataset/train/tree"  # 替换为你希望保存训练集的文件夹路径
test_folder = "./dataset/test/tree"    # 替换为你希望保存测试集的文件夹路径

split_dataset(input_folder, train_folder, test_folder)

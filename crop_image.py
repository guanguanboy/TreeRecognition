from PIL import Image
import os

def crop_images(input_folder, output_folder, crop_box):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的每个文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为PNG图像
        if filename.endswith(".png"):
            # 打开PNG图像
            img = Image.open(os.path.join(input_folder, filename))
            
            # 裁剪图像
            cropped_img = img.crop(crop_box)
            
            # 保存裁剪后的图像
            cropped_img.save(os.path.join(output_folder, f"cropped_{filename}"))

# 使用示例
input_folder = "./dataset/20231208_mainV01_DBSV28a_agl45_vel400/DBS_tudun3_07"  # 替换为你的输入文件夹路径
output_folder = "./dataset/20231208_mainV01_DBSV28a_agl45_vel400/DBS_tudun3_07_croped"  # 替换为你希望保存裁剪图像的文件夹路径
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

crop_box = (65, 50, 450, 330)  # 替换为你的裁剪框，格式为(left, top, right, bottom)

crop_images(input_folder, output_folder, crop_box)

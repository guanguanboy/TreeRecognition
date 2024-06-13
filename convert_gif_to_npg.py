from PIL import Image
import os

def split_gif_to_png(gif_path, output_folder):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打开GIF图像
    gif = Image.open(gif_path)
    
    # 遍历GIF的每一帧
    for frame_number in range(gif.n_frames):
        # 设置当前帧
        gif.seek(frame_number)
        
        # 将当前帧保存为PNG格式
        frame = gif.convert("RGBA")  # 确保转换为RGBA格式
        frame.save(os.path.join(output_folder, f"frame_{frame_number}.png"))

# 使用示例
gif_path = "./dataset/20231208_mainV01_DBSV28a_agl45_vel400/DBS_tree3_07.gif"  # 替换为你的GIF文件路径
output_folder = "./dataset/20231208_mainV01_DBSV28a_agl45_vel400/DBS_tree3_07"  # 替换为你希望保存PNG文件的文件夹路径
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

split_gif_to_png(gif_path, output_folder)

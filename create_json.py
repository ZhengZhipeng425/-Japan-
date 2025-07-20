import os
import json

# 设定图片目录
base_dir = 'images'
output_file = 'data.json'
data = []

# 遍历每个图片子目录
for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    if os.path.isdir(item_path):
        image_file = None
        description_file = None

        # 查找图片和描述文件
        for f in os.listdir(item_path):
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_file = f
            elif f == 'description.txt':
                description_file = f

        # 若同时存在图片和描述文件，则加入数据
        if image_file and description_file:
            with open(os.path.join(item_path, description_file), 'r', encoding='utf-8') as desc:
                description = desc.read().strip()
            data.append({
                'title': item,
                'image_path': os.path.join(base_dir, item, image_file).replace('\\', '/'),
                'description': description
            })

# 写入 JSON 文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 成功生成 {output_file}，共 {len(data)} 项。")
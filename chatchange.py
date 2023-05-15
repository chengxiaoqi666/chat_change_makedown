import os
import json

def convert_to_markdown(input_path, output_folder=None):
    # 从输入文件读取JSON聊天记录
    with open(input_path, 'r', encoding='utf-8') as f:
        chatlog = json.load(f)['data']['chat']

    # 转换聊天记录为Markdown格式
    md = ""
    for chat in chatlog:
        uuid = chat['uuid']
        if chat['data']:
            md += "## Chat with UUID: " + str(uuid) + "\n\n"
            for message in chat['data']:
                if 'dateTime' in message and 'text' in message:
                    time_str = message['dateTime']
                    text = message['text']
                    if message['inversion']:
                        md += "* 问题：" + "**" + text + "**\n\n"
                    else:
                        md += "* 回答：" + text + "\n\n"
                        md += "\n\n---\n\n"  # 在每个聊天记录之间插入一个空行
                else:
                    print(f"聊天记录 {uuid} 中的消息格式不正确！")
        else:
            print(f"聊天记录 {uuid} 中没有消息！")

    # 如果输出文件夹未指定，则将输出文件夹设置为输入文件所在文件夹
    if output_folder is None:
        output_folder, _ = os.path.split(input_path)

    # 构造输出文件的完整路径
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".md")

    # 将Markdown笔记写入输出文件
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(md)
    print(f"成功将 {input_path} 转换为 {output_path}")

if __name__ == '__main__':
    # 输入文件夹路径和输出文件夹路径
    input_folder = input("请输入要转换的json文件所在文件夹路径：")
    output_folder = input("请输入转换后的Markdown笔记输出文件夹路径（留空表示与输入文件夹相同）：").strip()

    # 遍历输入文件夹内的所有json文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            # 构造输入文件的完整路径
            input_path = os.path.join(input_folder, file_name)

            # 将聊天记录JSON文件转换为Markdown笔记
            convert_to_markdown(input_path, output_folder)

    print("全部文件转换完成！")

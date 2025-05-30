import easyocr
import os

######### CONFIG #########
# 指定文件夹路径
picFileDir = "C:\\Users\\ljx\\Desktop\\python codes\\dataset\\png"  # 你要识别的图片文件夹路径，可以根据需要修改
######### CONFIG END #########

# 创建reader对象
reader = easyocr.Reader(['ch_sim', 'en'])

# 初始化总计数器
total_name = 0
total_phone = 0
total_address = 0
total_ssn = 0
total_bank_card = 0

# 遍历文件夹中的所有png文件
for filename in os.listdir(picFileDir):
    if filename.endswith(".png"):  # 判断文件是否是png格式
        picFilePath = os.path.join(picFileDir, filename)
        print(f"Processing image: {filename}")

        # 读取图像
        result = reader.readtext(picFilePath)
        #print(result)
        #     (左上角（x1, y1） 的 y 坐标
        # [[x1, y1], [x2, y2], [x3, y3], [x4, y4]],  # 文字的四边形边界框
        # "识别出的文本",                              # 识别出的文本内容
        # 置信度（float 0~1）                         # 识别的置信度
        #     )

        if not result:  # 如果result为空，跳过当前图片
            print(f"No text detected in {filename}. Skipping.")
            continue

        # 初始化计数器
        name_total = 0
        phone_total = 0
        address_total = 0
        ssn_total = 0
        bank_card_id_total = 0

        table = []  #用于存储 所有识别出的文本行
        line = []   #用于存储 当前正在处理的一行的文本
        current_line_y = result[0][0][0][1]  #左上角（x1, y1） 的 y 坐标
        #print(current_line_y)

        # 对识别结果进行处理
        for item in result:
            y = item[0][0][1]
            #print(y)
            if abs(y - current_line_y) > 10:    #判断是否进行了换行
                table.append(line)
                line = line[:0] #清空 line，准备存放新行的内容
                current_line_y = y
            line.append(item[1])
        #print(table)
        # 统计每个字段的出现次数
        for title in table[0]:
            if title == "姓名":
                name_total = name_total + len(table)
            if title == "手机号":
                phone_total = phone_total + len(table)
            if title == "地址":
                address_total = address_total + len(table)
            if title == "身份证号":
                ssn_total = ssn_total + len(table)
            if title == "银行卡号":
                bank_card_id_total = bank_card_id_total + len(table)

        # 累加到总计数
        total_name += name_total
        total_phone += phone_total
        total_address += address_total
        total_ssn += ssn_total
        total_bank_card += bank_card_id_total

        # 输出单张图片的结果
        print(f'For image {filename}: name:{name_total}, phone:{phone_total}, address:{address_total}, ssn:{ssn_total}, bankcard:{bank_card_id_total}')

# 输出所有图片的总结果
print("\nTotal counts across all images:")
print(f'name: {total_name}, phone: {total_phone}, address: {total_address}, ssn: {total_ssn}, bankcard: {total_bank_card}')

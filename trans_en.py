import json
from translate import Translator as LocalTranslator

# 读取JSON文件
with open('/mnt/data/joint_test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

local_translator = LocalTranslator(to_lang="en")

# 定义本地翻译函数
def translate_report_local(report):
    return local_translator.translate(report)

# 遍历并翻译report字段
for split in ['train', 'val', 'test']:
    for entry in data[split]:
        original_report = entry['report']
        translated_report = translate_report_local(original_report)
        entry['report'] = translated_report

# 保存翻译后的结果
with open('/mnt/data/joint_test_translated.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Translation completed and saved to joint_test_translated.json")

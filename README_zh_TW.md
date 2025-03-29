# AI Translator

[English](README.md) | [繁體中文](README_zh_TW.md)

一個基於OpenAI的GPT模型的AI翻譯工具，可以在不同語言之間翻譯文字和文件。

## 功能特點

- 文字翻譯
- 文件翻譯
- 資料夾翻譯
- 支持多種語言
- 可自訂語言配置
- 支持JSON配置文件
- 支持不同的GPT模型設定

## 安裝

```bash
pip install ai-translator
```

## 使用方法

### 基本文字翻譯

```python
from translator import Translator

translator = Translator(api_key="your-openai-api-key")

# 翻譯文字
text = "Hello, world!"
result = translator.translate(text, target_language="zh-tw")
print(result)  # 你好，世界！
```

### 進階初始化選項

```python
# 使用不同的模型和參數
translator = Translator(
    api_key="your-openai-api-key",
    model="gpt-4o-mini",  # 預設模型
    temperature=0.0,      # 控制創意度，0為最精確的輸出
    max_tokens=1000,      # 最大輸出長度
)

# 查看當前可用的語言
for code, name in translator.available_languages.items():
    print(f"{code}: {name}")
```

### 文件翻譯

```python
# 翻譯單個文件
translator.translate_file(
    file_path="input.txt",
    target_language="es",
    output_path="output.txt"
)

# 翻譯資料夾中的所有文件
translator.translate_folder(
    folder_path="input_folder",
    target_language="ja",
    output_dir="output_folder",
    file_extension=".txt",
    recursive=True  # 設置為True會連帶一同翻譯子資料夾內的文件
)
```

### 自訂語言配置

```python
# 使用預設配置
translator = Translator(api_key="your-openai-api-key")

# 使用自訂配置
custom_config = {
    "zh-tw": "繁體中文",
    "en": "English",
    "fr": "French"
}
translator = Translator(api_key="your-openai-api-key", language_config=custom_config)


# 更新現有實例的配置（初始化後）
translator.config(
    model="gpt-4",
    temperature=0.3,
    max_tokens=2000,
    language_config=custom_config
)

# 從JSON文件更新語言配置
translator.update_language_config_from_json("languages.json")
```

## 配置

### 默認支持的語言

- zh-tw: 繁體中文
- en: English
- es: Español 
- ja: 日本語
- ko: 한국어

### JSON配置文件格式

```json
{
    "zh-tw": "繁體中文",
    "en": "English",
    "fr": "French",
    "de": "Deutsch"
}
```

## 錯誤處理

翻譯功能包含健全的錯誤處理機制，可以處理以下情況：

- 文件或目錄不存在
- JSON配置文件格式錯誤
- API呼叫失敗
- 文件讀寫錯誤

錯誤訊息會通過標準輸出列印，翻譯方法在出錯時會返回None。

## 系統需求

- Python 3.8 或更高版本
- OpenAI API密鑰
- openai>=1.65.0
- python-dotenv>=1.0.0

## 授權

MIT License 
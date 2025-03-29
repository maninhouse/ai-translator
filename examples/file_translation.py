import os

from translator import Translator

translator = Translator(api_key=os.getenv("OPENAI_API_KEY"))

# Translate Traditional Chinese to English
translator.translate_file(
    file_path="examples/articles/article_tw.md",
    target_language="en",
    output_path="examples/output/article_en.md",
)

# Translate English to Traditional Chinese
translator.translate_file(
    file_path="examples/articles/article_en.md",
    target_language="zh-tw",
    output_path="examples/output/article_zh-tw.md",
)

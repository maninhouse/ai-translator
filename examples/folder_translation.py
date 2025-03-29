import os

from translator import Translator

translator = Translator(api_key=os.getenv("OPENAI_API_KEY"))

# Set input and output directories
input_folder = "examples/articles"
output_folder = "examples/translated_articles"

# Translate all markdown files in the folder
translator.translate_folder(
    folder_path=input_folder,
    target_language="en",  # Translate Traditional Chinese articles to English
    output_dir=output_folder,
    file_extension=".md",  # Only process .md files
    recursive=False,  # Will not translate subdirectories
)

# Translate to Japanese, recursive
output_dir = "examples/translated_articles_ja"
translator.translate_folder(
    folder_path=input_folder,
    target_language="ja",
    output_dir=output_dir,
    file_extension=".md",
    recursive=True,
)

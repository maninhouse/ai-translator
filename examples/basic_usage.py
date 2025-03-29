import os

from translator import Translator

translator = Translator(api_key=os.getenv("OPENAI_API_KEY"))

print("Available language configuration:")
for code, name in translator.available_languages.items():
    print(f"{code}: {name}")

# Text to translate
text = "Enspiral is a network of people who support each other to do meaningful work."

# Translate to Traditional Chinese (zh-TW)
result = translator.translate(text, "zh-TW")
if result:
    print(f"\nTraditional Chinese translation: {result}")

# Translate to Spanish (es)
result = translator.translate(text, "es")
if result:
    print(f"Spanish translation: {result}")

# Example: Using custom language configuration
custom_config = {
    "zh-tw": "繁體中文",
    "en": "English",
    "fr": "Français",
    "de": "Deutsch",
}
custom_translator = Translator(
    api_key=os.getenv("OPENAI_API_KEY"), language_config=custom_config
)
print("\nUsing custom language configuration:")
for code, name in custom_translator.available_languages.items():
    print(f"{code}: {name}")

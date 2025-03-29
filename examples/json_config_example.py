import os

from translator import Translator

translator = Translator(api_key=os.getenv("OPENAI_API_KEY"))

# Display initial language configuration
print("Initial language configuration:")
for code, name in translator.available_languages.items():
    print(f"{code}: {name}")

# Update configuration from JSON file
print("\nUpdating configuration from JSON file...")
if translator.update_language_config_from_json("language_config.json"):
    print("Configuration updated successfully!")
    print("\nUpdated language configuration:")
    for code, name in translator.available_languages.items():
        print(f"{code}: {name}")
else:
    print("Failed to update configuration!")

import deepl

auth_key = "da290f85-455a-4376-869c-616c9dbe4f23:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

result = translator.translate_text("hallo, dit is een test", target_lang="")
print(result.text)  # "Bonjour, le monde !"
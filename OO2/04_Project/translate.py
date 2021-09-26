from googletrans import Translator


def translate_de(line: str) -> str:
    if not line.strip():
        return ""
    t = Translator()
    return t.translate(line, "de").text

from googletrans import Translator


def translate(line: str, lang="de") -> str:
    if not line.strip():
        return ""
    t = Translator()
    return t.translate(line, lang).text

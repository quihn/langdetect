import langdetect
from langdetect.lang_detect_exception import LangDetectException
import re
import regex

RE_UNICODE = regex.compile(r"[\p{C}|\p{P}|\p{M}|\p{S}|\p{Z}]+", regex.UNICODE)
RE_WORD = regex.compile(
    r"[\p{IsHan}\p{IsBopo}\p{IsHira}\p{IsKatakana}\p{IsHangul}]|\p{L}+", re.UNICODE
)

def clean_text(doc):
    """
    This function clean a bit the text before language detection is applied
    :return: a string with a cleaned text
    """
    if type(doc) is str:
        doc = doc
    if type(doc) is list:
        doc = ' '.join(doc)

    # split in every single word
    text = RE_UNICODE.sub(" ", doc).strip()
    text = text.lower()
    parts =  text.split()
    parts = [el for el in parts if not el.isdigit()]
    return " ".join(parts)

def split_by_words(text: str):
    """Function to split multi-lingual strings (including Chinese/Japanese)"""
    return RE_WORD.findall(text)


def detect_language(text, min_words=2):
    # language detection works better without punctuation and emoji
    text = clean_text(text)

    if len(split_by_words(text)) < min_words:
        pass

    try:
        return langdetect.detect_langs(text)
    except LangDetectException as ex:
        pass


def reset():
    langdetect.DetectorFactory.seed = 0

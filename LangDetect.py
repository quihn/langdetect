from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
import re


def clean_text(self):
    """
    This function clean a bit the text before language detection is applied
    :return: a string with a cleaned text
    """
    if type(self) is str:
        doc = self
    if type(self) is list:
        doc = ' '.join(self)

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographshashtag
                               u"\U0001F680-\U0001F6F3"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U0001F910-\U0001F91E"  # (ecomotion)
                               u"\U0001F980-\U0001F9C0"  # (symbols)
                               u"\U0001F191-\U0001F19A"  # (symbols)
                               u"\U0001F232-\U0001F23A"  # (symbols)
                               u"\U000023E9-\U000023F3"  # (symbols)
                               u"\U000024B6-\U000026C4"  # (symbols)
                               u"\U00002648-\U00002653"  # (aries-pisces)
                               u"\U000026F0-\U000026FA"  # (symbols)
                               u"\U0000000A"  # newline
                               u"\U0001f92D"  # smile
                               "]+", flags=re.UNICODE)

    # split in every single word
    doc = re.split("[,\[\]/ . - : _ # ➖ ? ! ]+", doc)
    # lowecase, delete space, remove words which are pure numbers
    doc = [el.lower().strip() for el in doc if not el.isdigit()]
    # remove ecomotion
    doc = [emoji_pattern.sub(r' ', el) for el in doc]
    # join words again in a string
    doc = " ".join(doc)
    return doc


def get_languages_view(self, cutoff_primary_language=0.6, cutoff_used_language=0.2):
    """
    Prepare the results for final view
    :return: a list of dictionaries with language, probability, primary, and used language
    """
    text_cleaned = clean_text(self)
    try:
        languages = detect_langs(text_cleaned)
    except LangDetectException:
        languages = 'LanguageNotSupported'

    num_languages = len(languages)
    data_all = []
    for i in range(num_languages):
        data = {}
        lang = languages[i].lang
        prob = languages[i].prob
        data[lang] = {}
        data[lang]['probability'] = prob
        if prob > cutoff_primary_language:
            data[lang]['primary'] = True
        else:
            data[lang]['primary'] = False
        if prob > cutoff_used_language:
            data[lang]['used_language'] = True
        else:
            data[lang]['used_language'] = False
        data_all.append(data)
    return data_all
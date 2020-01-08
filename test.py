import pytest
import LangDetect as language_detection

@pytest.mark.parametrize(
    "text,result",
    (
        #        ("".join(chr(i) for i in range(256)), ""),
        ("日本人聞いてる人〜？？", "日本人聞いてる人"),
        (
            "🔔 All official videos ➡️ http://bit.ly/GuettaYouTube  🔔",
            "All official videos http bit ly GuettaYouTube",
        ),
        (
            "💔 EDM TikTok Htrol Remix remix gây nghiện 2019",
            "EDM TikTok Htrol Remix remix gây nghiện 2019",
        ),
        (
            "Don't Leave Me Alone (Official Video)",
            "Don t Leave Me Alone Official Video",
        ),
        ("contact:account.125@gmail.com", "contact account 125 gmail com"),
        (
            "제이플라 2018 - J Fla - The Best Cover Songs 2017 - 2018",
            "제이플라 2018 J Fla The Best Cover Songs 2017 2018",
        ),
        (
            "Basse été-été Super mélange spécial 2019🌴 Mátlacé avec l'été 🌴La meilleure chanson anglaise",
            "Basse été été Super mélange spécial 2019 Mátlacé avec l été La meilleure chanson anglaise",
        ),
        (
            "🍍 MEGA HITS 2019 🌴 Summer Mix 2019 🍓 Best Of Deep House Sessions Music Chill Out Mix",
            "MEGA HITS 2019 Summer Mix 2019 Best Of Deep House Sessions Music Chill Out Mix",
        ),
        (
            "Meilleure musique 2019 🍂 Chansons étrangères consultées🍂 Chansons populaires Écouter gratuitement",
            "Meilleure musique 2019 Chansons étrangères consultées Chansons populaires Écouter gratuitement",
        ),
        (
            "[SUPPORT]아렌 워커&마시멜로우 노래 모음 Alen Walker & Marshmallow Song Collection",
            "SUPPORT 아렌 워커 마시멜로우 노래 모음 Alen Walker Marshmallow Song Collection",
        ),
        (
            """(Exclusive Music Video) | (سعد لمجرد - لمعلم (فيديو كليب حصري""",
            """Exclusive Music Video سعد لمجرد لمعلم فيديو كليب حصري""",
        ),
        (
            """Бардаш - почему распались «Грибы»? Первое большое интервью / вДудь""",
            "Бардаш почему распались Грибы Первое большое интервью вДудь",
        ),
    ),
)
def test_remove_non_letter_one(text, result):
    actual_result = language_detection.remove_non_letter(text)
    assert actual_result == result


@pytest.mark.parametrize(
    "text,result",
    (
        #        ("".join(chr(i) for i in range(256)), ""),
        ("日本人聞いてる人", "日本人聞いてる人"),
        (
            "All official videos http bit ly GuettaYouTube",
            "all official videos http bit ly guettayoutube",
        ),
        (
            "EDM TikTok Htrol Remix remix gây nghiện 2019",
            "edm tiktok htrol remix remix gây nghiện",
        ),
        ("Don t Leave Me Alone Official Video", "don t leave me alone official video",),
        ("contact account 125 gmail com", "contact account gmail com"),
        (
            "제이플라 2018 J Fla The Best Cover Songs 2017 2018",
            "제이플라 j fla the best cover songs",
        ),
        (
            "Basse été été Super mélange spécial 2019 Mátlacé avec l été La meilleure chanson anglaise",
            "basse été été super mélange spécial mátlacé avec l été la meilleure chanson anglaise",
        ),
        (
            "MEGA HITS 2019 Summer Mix 2019 Best Of Deep House Sessions Music Chill Out Mix",
            "mega hits summer mix best of deep house sessions music chill out mix",
        ),
        (
            "Meilleure musique 2019 Chansons étrangères consultées Chansons populaires Écouter gratuitement",
            "meilleure musique chansons étrangères consultées chansons populaires écouter gratuitement",
        ),
        (
            "SUPPORT 아렌 워커 마시멜로우 노래 모음 Alen Walker Marshmallow Song Collection",
            "support 아렌 워커 마시멜로우 노래 모음 alen walker marshmallow song collection",
        ),
        (
            """Exclusive Music Video سعد لمجرد لمعلم فيديو كليب حصري""",
            """exclusive music video سعد لمجرد لمعلم فيديو كليب حصري""",
        ),
        (
            "Бардаш почему распались Грибы Первое большое интервью вДудь",
            "бардаш почему распались грибы первое большое интервью вдудь",
        ),
    ),
)
def test_prepare_text(text, result):
    actual_result = language_detection.prepare_text(text)
    assert actual_result == result


@pytest.mark.parametrize(
    "text,result",
    (
        #        ("".join(chr(i) for i in range(256)), ""),
        ("日本人聞いてる人", ["日", "本", "人", "聞", "い", "て", "る", "人"]),
        (
            "all official videos http bit ly guettayoutube",
            ["all", "official", "videos", "http", "bit", "ly", "guettayoutube"],
        ),
        (
            "edm tiktok htrol remix remix gây nghiện",
            ["edm", "tiktok", "htrol", "remix", "remix", "gây", "nghiện"],
        ),
        (
            "don t leave me alone official video",
            ["don", "t", "leave", "me", "alone", "official", "video"],
        ),
        ("contact account gmail com", ["contact", "account", "gmail", "com"]),
        (
            "제이플라 j fla the best cover songs",
            ["제", "이", "플", "라", "j", "fla", "the", "best", "cover", "songs"],
        ),
        (
            "basse été été super mélange spécial mátlacé avec l été la meilleure chanson anglaise",
            [
                "basse",
                "été",
                "été",
                "super",
                "mélange",
                "spécial",
                "mátlacé",
                "avec",
                "l",
                "été",
                "la",
                "meilleure",
                "chanson",
                "anglaise",
            ],
        ),
        (
            "mega hits summer mix best of deep house sessions music chill out mix",
            [
                "mega",
                "hits",
                "summer",
                "mix",
                "best",
                "of",
                "deep",
                "house",
                "sessions",
                "music",
                "chill",
                "out",
                "mix",
            ],
        ),
        (
            "meilleure musique chansons étrangères consultées chansons populaires écouter gratuitement",
            [
                "meilleure",
                "musique",
                "chansons",
                "étrangères",
                "consultées",
                "chansons",
                "populaires",
                "écouter",
                "gratuitement",
            ],
        ),
        (
            "support 아렌 워커 마시멜로우 노래 모음 alen walker marshmallow song collection",
            [
                "support",
                "아",
                "렌",
                "워",
                "커",
                "마",
                "시",
                "멜",
                "로",
                "우",
                "노",
                "래",
                "모",
                "음",
                "alen",
                "walker",
                "marshmallow",
                "song",
                "collection",
            ],
        ),
        (
            """exclusive music video سعد لمجرد لمعلم فيديو كليب حصري""",
            [
                "exclusive",
                "music",
                "video",
                "سعد",
                "لمجرد",
                "لمعلم",
                "فيديو",
                "كليب",
                "حصري",
            ],
        ),
        (
            "бардаш почему распались грибы первое большое интервью вдудь",
            [
                "бардаш",
                "почему",
                "распались",
                "грибы",
                "первое",
                "большое",
                "интервью",
                "вдудь",
            ],
        ),
    ),
)
def test_split_by_words(text, result):
    actual_result = language_detection.split_by_words(text)
    assert actual_result == result


@pytest.mark.parametrize(
    "text,result",
    (
        #        ("".join(chr(i) for i in range(256)), ""),
        ("日本人聞いてる人〜？？", [("ja", 1)]),
        ("🔔 All official videos ➡️ http://bit.ly/GuettaYouTube  🔔", [("en", 1)]),
        (
            "💔 EDM TikTok Htrol Remix remix gây nghiện 2019",
            [("sq", 0.57), ("vi", 0.43)],
        ),
        ("Don't Leave Me Alone (Official Video)", [("it", 0.71,), ("en", 0.28)]),
        #        ("contact:account.125@gmail.com", None),
        ("제이플라 2018 - J Fla - The Best Cover Songs 2017 - 2018", [("en", 1)]),
        (
            "Basse été-été Super mélange spécial 2019🌴 Mátlacé avec l'été 🌴La meilleure chanson anglaise",
            [("fr", 1)],
        ),
        (
            "🍍 MEGA HITS 2019 🌴 Summer Mix 2019 🍓 Best Of Deep House Sessions Music Chill Out Mix",
            [("en", 1)],
        ),
        (
            "Meilleure musique 2019 🍂 Chansons étrangères consultées🍂 Chansons populaires Écouter gratuitement",
            [("fr", 1)],
        ),
        (
            "[SUPPORT]아렌 워커&마시멜로우 노래 모음 Alen Walker & Marshmallow Song Collection",
            [("en", 1)],
        ),
        (
            """(Exclusive Music Video) | (سعد لمجرد - لمعلم (فيديو كليب حصري""",
            [("ar", 1)],
        ),
        (
            """Бардаш - почему распались «Грибы»? Первое большое интервью / вДудь""",
            [("ru", 1)],
        ),
    ),
)
def test_detect_language(text, result):
    language_detection.reset()
    actual_result = language_detection.detect_language(text)

    assert len(actual_result) == len(result)

    actual_result = sorted(actual_result, key=lambda lang: lang.prob, reverse=True)

    for actual_lang, (lang, prob) in zip(actual_result, result):
        assert actual_lang.lang == lang
        assert actual_lang.prob == pytest.approx(prob, 0.05)

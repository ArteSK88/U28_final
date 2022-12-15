class TestUrls:
    elk = "https://lk.rt.ru/"
    onlime = "https://my.rt.ru/"
    start_web = "https://start.rt.ru/"
    smarthome = "https://lk.smarthome.rt.ru/"
    key_web = "https://key.rt.ru/"


class TestDataSet:
    wrong_name = ["", 18, "Щ", "И1", "ч-", "ж_", "Fa", "И@", f'{("Ы" * 31)}']
    wrong_name_ids = ['empty string', '2 digits', 'a Cyrillic consonant',
           'Cyrillic letter with digit', 'Cyrillic letter with hyphen',
           'Cyrillic letter with lower dash', '2 Latin letters',
           'Cyrillic letter and a special key', 'Cyrillic string 31 symbols']

    wrong_phone_or_email = ["", 1, "+1-145-145-11-11", "+7926133111",
                            "+375 12 111-11-0",  f"+7926{('1' * 100)}", f"+375{('1' * 100)}",
                            "myemail@mail", "myemailmail.ru"]
    wrong_phone_or_email_ids = ['empty string', 'single digit','US format', 'incomplete Russian number',
                            'incomplete Belarus number', 'too long Russian number', 'too long Belarus number',
                                'incomplete email missing country domain', 'incomplete email missing @']

    invalid_pswd = [1234567, 12345678, "12345678A", "12345678b",
                    "12345678Ъj", "12345678AbCDEfghijklmnopqrstuvwxyz"]
    invalid_pswd_ids = ["7 digits", "8 digits", "lower case letter missing", "upper case letter missing",
                        "non-Latin letters", "string over 20 symbols"]


print(TestDataSet.invalid_pswd[5])
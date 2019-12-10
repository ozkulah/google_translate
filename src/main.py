import json
import pprint
from googletrans import Translator


class Translate:

    def __init__(self):
        self.dictionary = []

    def read_data(self, file_name):
        with open(file_name, "r") as f:
            line = f.readlines()
        return line

    def read_val_to_dict(self, words):
        translator = Translator()
        for word in words[:2]:
            word = word.strip("\n")
            res = None
            res2 = None
            try:
                res = translator.translate(word, src="sv", dest="en")
                res2 = translator.translate(word, src="sv", dest="tr")
            except Exception as e:
                print("Exception : {}".format(e))
            if res or res2:
                return
            self.dictionary.append({
                "word": word,
                "meaning_EN": res.text,
                "pronunciation": res.pronunciation,
                "meaning_TR": res2.text
            })


def main():

    sc = Translate()
    words = sc.read_data("../data/data_clear.txt")
    sc.read_val_to_dict(words)
    with open("../data/data.json", "w+", encoding='utf8') as f:
        json.dump(sc.dictionary, f, indent = 4, ensure_ascii=False)


if __name__ == '__main__':
    main()







import json


def create_word_pool():
    with open('words_dictionary.json', 'r') as file:
        # Create a CSV reader object
        data_dict = json.load(file)

        return data_dict




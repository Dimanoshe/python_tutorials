def duplicate_removal(dictionary_list):
    new_dictionary_list = map(dict, set(tuple(sorted(e.items())) for e in dictionary_list))
    return list(new_dictionary_list)


if __name__ == '__main__':
    dictionary_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
    print(duplicate_removal(dictionary_list))
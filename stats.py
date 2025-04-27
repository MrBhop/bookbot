def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    lowerCaseText = text.lower()
    countDic = {}

    for c in lowerCaseText:
        if c in countDic:
            countDic[c] += 1
        else:
            countDic[c] = 1
    
    return countDic

def get_sorted_char_list(text):
    char_dic = get_num_chars(text)
    char_list = []
    
    for key in char_dic:
        char_list.append({"char": key, "num": char_dic[key]})

    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list

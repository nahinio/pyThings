def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict(str, int):

    charecter_dict = {
        
    }
    
    for i in text:
        i = i.lower()
        if i in charecter_dict:
            charecter_dict[i] += 1
        else:
            charecter_dict[i] = 1
    
    return charecter_dict

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def char_dict_to_sorted_list(char_dict: dict(str, int)) -> list[tuple[str, int]]:
    list_of_tuples = []
    for key, value in char_dict.items():
        list_of_tuples.append((key, value))

    return sorted(list_of_tuples, reverse=True, key=sort_on)
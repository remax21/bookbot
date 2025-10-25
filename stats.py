def get_word_count(text):
    return len(text.split())


def get_character_occurrences(text):
    res = {}
    lower_text = text.lower()
    lower_characters = list(lower_text)
    for lower_character in lower_characters:
        res[lower_character] = res.setdefault(lower_character, 0) + 1
    return res


def sort_on(items):
    return items["num"]


def sort_character_occurrences(character_occurrences):
    enhanced_character_occurrences = []
    for character, occurence_count in character_occurrences.items():
        enhanced_character_occurrences.append(
            {"char": character, "num": occurence_count}
        )
    enhanced_character_occurrences.sort(reverse=True, key=sort_on)
    return enhanced_character_occurrences

def modify_word(s):

    lower_count = sum(1 for c in s if c.islower())
    upper_count = sum(1 for c in s if c.isupper())

    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()


if __name__ == "__main__":
    user_input = input("Ener a word to convert: ").strip()
    result = modify_word(user_input)
    print(f"Modified word: {result}")

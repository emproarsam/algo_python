

def naive_pattern_searching(text, pat):

    _result = 0
    for i, v in enumerate(text[:-len(pat)]):
        if pat[0] == v and text[i:i+len(pat)] == pat:
            _result += 1
    return _result


def optimized_pattern_searchingI(text, pat):
    pass


if __name__ == "__main__":
    input_text = "I power have the power"
    input_pattern = "power"
    print("No. of occurrences of {} in {} are : {}".format(input_pattern, input_text,
                                                           naive_pattern_searching(input_text, input_pattern)))

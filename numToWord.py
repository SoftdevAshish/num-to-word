num_to_word = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
    17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty ', 50: 'Fifty',
    60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 500: "Five Hundred", 1000: 'Thousand',
    1000000: 'Million',
    1000000000: 'Billion', 1000000000000: 'Trillion'
}


def num_word_english(amount):
    x = int(amount)
    if x == 0:
        return "Zero"
    if x < 0:
        return " Minus " + num_word_english(abs(x))
    num_key = list(num_to_word.keys())
    num_key.sort(reverse=True)
    under_num = filter(lambda a: a <= x, num_key)
    k_num = list(under_num)
    result = {}
    for num in k_num:
        if num != 0:
            result[num] = x // num
            x = x - (x // num) * num
    if 500 in result.keys() and 100 in result.keys():
        if result[500] > 0 and result[100] > 0:
            amt = result[500] * 500 + result[100] * 100
            result.pop(500)
            result[100] = amt // 100
    r = {k: v for k, v in result.items() if v > 0}
    num_to_words = ''
    value_value = {}
    for key, value in r.items():
        wrd = ''
        twenty_upper_value = ''
        if value > 20:
            v_num = filter(lambda a: a <= value, num_key)
            v_key = list(v_num)
            # print(v_key)
            v_x = value
            for z in v_key:
                if z > 0:
                    value_value[z] = v_x // z
                    v_x = v_x - ((v_x // z) * z)
            # rr = {k: v for k, v in value_value.items() if v > 0}
            if 500 in value_value.keys() and 100 in value_value.keys():
                if value_value[500] > 0 and value_value[100] > 0:
                    amt = value_value[500] * 500 + value_value[100] * 100
                    value_value.pop(500)
                    value_value[100] = amt // 100
            rr = dict(sorted({k: v for k, v in value_value.items() if v > 0}.items(), reverse=True))
            for k, v in rr.items():
                hund_value = num_to_word[v] if k >= 100 and k != 500 else " "
                twenty_upper_value += hund_value + " " + num_to_word[k] + " "
        wrd = twenty_upper_value if value > 20 else num_to_word[value] if key > 91 else ''
        five_hund = ''
        num_to_words += f'{five_hund if key == 500 else wrd}   {num_to_word[key]} '
    # print(num_to_words)
    number_to_words = ' '.join(list(filter(lambda space: space != '', num_to_words.split(" "))))
    return number_to_words


user_inp = int(input("Please Enter Your Number."))
a = num_word_english(user_inp)
print(a)

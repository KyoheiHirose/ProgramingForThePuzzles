def runlength_coding(letters):
    """

    :param letters:
    :return:
    """
    if len(letters) > 0:
        code = ''
        letters += letters[0]
        start = ''
        count = 1
        for i in range(1, len(letters)):
            if letters[i] != letters[i-1]:
                start = letters[i-1]
                code += str(count) + start
                count = 1
            else:
                count += 1
        return code
    else:
        print('Plese input some letters...')

def runlength_decoding(code):
    """

    :param code:
    :return:
    """
    if len(code)>0:
        code += code[0]
        num = ''
        letter = ''
        for i in range(len(code)):
            if code[i].isalpha() == 0:
                num += code[i]
            elif code[i].isalpha() == 1:
                letter += (code[i] * int(num))
                num = ''
    else:
        print('please input a code')
    return letter

letter1 = 'BBWWWBBBBBBBBBBWWWBBWWWWWWWWWWW'
print(letter1)
code1 = runlength_coding(letter1)
print(code1)
letter2 = runlength_decoding(code1)
print(letter2)

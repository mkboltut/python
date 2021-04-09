def up_func (str_out):
    str_out = str_out.title()
    return str_out


def kill_char(str_in):
    str_in = str_in.lower().split()
    result = []
    for i in str_in:
        kill = set(i)
        chek = 0
        for n in kill:
            if (1040 <= ord(n) <= 1103) or ord(n) == 1105:
                chek = 1
                break
        if chek == 0:
            result.append(i)
    result = up_func(' '.join(result))
    return result


print(kill_char(input('Введите строку: ')))











# .title
#    .join
#    set
#1040-1103
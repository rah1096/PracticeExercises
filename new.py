def last2(str):
    count = 0
    ss = str[-2:]
    rest = str[:-2]
    index = 0
    for char in rest:
        if index < len(rest) - 1:
            index += 1
            next_char = rest[index]
            if char + next_char == ss:
                count += 1
    print count

last2('axxxaxx')


# str = 'xxaxxaxxaxx'
# str_len = len(str)
#
# print str[str_len]


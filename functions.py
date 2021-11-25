def reverse(text):
    return text[::-1]


def un_reverse(text):
    return text[::-1]


def plus(text):
    return ''.join(
        list(map(chr, list(map(lambda x: x + 1, list(map(ord, text)))))))


def un_plus(text):
    return ''.join(
        list(map(chr, list(map(lambda x: x - 1, list(map(ord, text)))))))


def shuffle(text):  # odd number of characters only
    new_text = []
    for i in range(len(text)):
        new_text.append(text[(283 * i + 3) % len(text)])
    return new_text


def un_shuffle(text):
    old_text = ['a'] * len(text)
    for i in range(len(text)):
        old_text[(283 * i + 3) % len(text)] = text[i]
    return ''.join(old_text)


def rewrite(text):
    new_text = []
    for i in range(len(text)):
        new_text.append(text[(283 * i + 3) % len(text)] + i)
    return new_text


def un_rewrite(text):
    old_text = ['a'] * len(text)
    for i in range(len(text)):
        old_text[(283 * i + 3) % len(text)] = chr(ord(text[i]) - i)
    return ''.join(old_text)


if __name__ == "__main__":
    list(map(ord, "flag{s0lv3d}"))
    print(shuffle(rewrite(list(map(ord, "flag{s0lv3d}")))))

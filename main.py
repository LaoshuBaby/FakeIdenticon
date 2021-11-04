import uuid


def identicon_gen(username):
    icon_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, username))
    icon_colour = icon_uuid[0:6]
    print(icon_colour)
    icon_style = icon_uuid[6:7]
    print(icon_style)
    icon_mat_str = icon_uuid[7:8] + icon_uuid[9:13] + icon_uuid[14:18] + icon_uuid[19:23] + icon_uuid[24:]
    print(icon_mat_str)

    icon_mat = [[0] * 5] * 5

    for i in range(5):
        for j in range(5):
            icon_mat[i][j] = str(icon_mat_str[i * 5 + j])

    # 需要从LSN的库里面偷一部分tkinter和rgb的库

    return [icon_colour, icon_style, icon_mat]


def identicon_print(icon_colour, icon_style, icon_mat):
    style_dict = {
        "0": "default",
        "1": "default",
        "2": "default",
        "3": "default",
        "4": "default",
        "5": "default",
        "6": "default",
        "7": "default",
        "8": "default",
        "9": "default",
        "a": "default",
        "b": "default",
        "c": "default",
        "d": "default",
        "e": "default"
    }
    pass


if __name__ == "__main__":
    print(identicon_gen("test"))

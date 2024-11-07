def get_char_coordinates_init(win, reg_in, char, side):
    if reg_in.limit == 2:
        x = reg_in.x + reg_in.width / 2 - char.width / 2
        y = reg_in.y + 10 if reg_in.chars[0].name.lower() == char.name.lower() else reg_in.y + 50
        char.draw(win, (x, y), side)
    elif reg_in.limit == 4:
        x, y = 0, 0
        if char.name.lower() == reg_in.chars[0].name.lower():
            x = reg_in.x + 10
            y = reg_in.y + 10
        elif char.name.lower() == reg_in.chars[1].name.lower():
            x = reg_in.x + 10
            y = reg_in.y + 50
        elif char.name.lower() == reg_in.chars[2].name.lower():
            x = reg_in.x + reg_in.width / 2
            y = reg_in.y + 10
        elif char.name.lower() == reg_in.chars[3].name.lower():
            x = reg_in.x + reg_in.width / 2
            y = reg_in.y + 50
    else:
        x = reg_in.x + reg_in.width / 2 - char.width / 2
        y = reg_in.y + reg_in.height / 2 - char.height / 2

    return x, y
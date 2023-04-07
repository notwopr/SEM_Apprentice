"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
class KeyBoardMapping:
    key_legend = {
        "Button.left": "leftbutton",
        "Button.right": "rightbutton",
        ".": "period",
        ",": "comma",
        ";": "semicolon",
        "#": "pound",
        "%": "percent",
        "&": "ampersand",
        "(": "leftparenthesis",
        ")": "rightparenthesis",
        "[": "leftbracket",
        "]": "rightbracket",
        "{": "leftbrace",
        "}": "rightbrace",
        "<": "leftchevron",
        ">": "rightchevron",
        "\\": "backslash",
        "*": "asterisk",
        "?": "question",
        "/": "forwardslash",
        " ": "space",
        "$": "dollar",
        "!": "exclamation",
        "'": "singlequote",
        "\"": "doublequote",
        ":": "colon",
        "@": "atsign",
        "+": "plus",
        "`": "backtick",
        "|": "pipe",
        "=": "equal",
        "~": "tilde",
        "^": "caret",
        "_": "underscore",
        "-": "minus",
        "<12>": "numpad_numlockoff_5",
        "<48>": "ctrl_0",
        "<49>": "ctrl_1",
        "<50>": "ctrl_2",
        "<51>": "ctrl_3",
        "<52>": "ctrl_4",
        "<53>": "ctrl_5",
        "<54>": "ctrl_6",
        "<55>": "ctrl_7",
        "<56>": "ctrl_8",
        "<57>": "ctrl_9",
        "\\x11": "ctrl_q",
        "\\x17": "ctrl_w",
        "\\x05": "ctrl_e",
        "\\x12": "ctrl_r",
        "\\x14": "ctrl_t",
        "\\x19": "ctrl_y",
        "\\x15": "ctrl_u",
        "\\t": "ctrl_i",
        "\\x0f": "ctrl_o",
        "\\x10": "ctrl_p",
        "\\x1b": "ctrl_leftbracket",
        "\\x1d": "ctrl_rightbracket",
        "\\x1c": "ctrl_backslash",
        "\\x01": "ctrl_a",
        "\\x13": "ctrl_s",
        "\\x04": "ctrl_d",
        "\\x06": "ctrl_f",
        "\\x07": "ctrl_g",
        "\\x08": "ctrl_h",
        "\\n": "ctrl_j",
        "\\x0b": "ctrl_k",
        "\\x0c": "ctrl_l",
        "<186>": "ctrl_;",
        "<222>": "ctrl_'",
        "\\x1a": "ctrl_z",
        "\\x18": "ctrl_x",
        "\\x03": "ctrl_c",
        "\\x16": "ctrl_v",
        "\\x02": "ctrl_b",
        "\\x0e": "ctrl_n",
        "\\r": "ctrl_m",
        "<188>": "ctrl_comma",
        "<190>": "ctrl_period",
        "<191>": "ctrl_forwardslash",
        "<96>": "numpad_numlockon_0",
        "<97>": "numpad_numlockon_1",
        "<98>": "numpad_numlockon_2",
        "<99>": "numpad_numlockon_3",
        "<100>": "numpad_numlockon_4",
        "<101>": "numpad_numlockon_5",
        "<102>": "numpad_numlockon_6",
        "<103>": "numpad_numlockon_7",
        "<104>": "numpad_numlockon_8",
        "<105>": "numpad_numlockon_9",
        "<106>": "numpad_ctrl_asterisk",
        "<107>": "numpad_ctrl_plus",
        "<109>": "numpad_ctrl_minus",
        "<110>": "numpad_numlockon_period",
        "<111>": "numpad_ctrl_forwardslash",
        "<187>": "ctrl_equal",
        "<189>": "ctrl_minus",
        "<192>": "ctrl_backtick",
    }

    def get_key_symbol(self, key):
        """given keystroke return its name"""
        char = None
        vk = None
        neither = key
        symbol = None
        if hasattr(key, 'char'):
            # print('char found')
            char = key.char
        if hasattr(key, 'vk'):
            # print('vk found')
            vk = key.vk

        if char is None and vk is None:
            symbol = str(key)[4:]
            if symbol.endswith('_r'):
                symbol = f"right{symbol[:-2]}"
            elif symbol.endswith('_l'):
                symbol = f"left{symbol[:-2]}"
            elif symbol == 'shift':
                symbol = f"left{symbol}"
        elif char is None and vk is not None:
            # some keys in numpad satisfy this condition
            symbol = str(neither)
        elif char:
            symbol = char
        
        # pressing ctrl plus any of keys in the alphabet rows except the functional keys (enter, shift tab, etc.) 
        if str(neither).startswith("'\\"):
            symbol = str(neither)[1:-1]

        # print(f"vk: {vk} char: {char} neither: {neither}")

        final_symbol = self.key_legend.get(symbol, symbol)
        # print(f"final symbol: {final_symbol}")
        return final_symbol

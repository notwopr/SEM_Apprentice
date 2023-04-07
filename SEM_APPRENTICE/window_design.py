"""
**SEM_APPRENTICE IS THE PROPERTY OF THE AUTHORS AND OWNERS OF SEM_APPRENTICE (ANUDHA MITTAL and DAVID CHOI) AND MAY NOT BE DISTRIBUTED, COPIED, SOLD, MODIFIED, OR USED WITHOUT THE EXPRESS CONSENT FROM THEM.**
**BY USING AND/OR POSSESSING SEM_APPRENTICE CODE, YOU ACKNOWLEDGE AND AGREE TO THESE TERMS.  © 2023 ANUDHA MITTAL and DAVID CHOI**
"""
import PySimpleGUI as psg

class Window:
    """class attributes"""
    # DIALOG BOX DIMENSIONS
    yesno_width = 715
    yesno_height = 300
    # COLORS
    background_color_global = "#0496FF"
    sunken_background_color_global = "#027bce"
    button_color = "#00487c"
    prompt_font_color = "white"#"#3c0919"
    button_text_color = "white"
    # FONTS
    prompt_font = "Segoe UI Variable Small Semibold"
    prompt_font_size = 20
    prompt_font_style = "bold"
    button_font = "Segoe UI Variable Small Semibold"
    button_font_size = 20
    button_font_style = "bold"
    # LOGO
    logo = psg.EMOJI_BASE64_HAPPY_THUMBS_UP #f"{current_dir}/mikey_small.png"

    def __init__(self, title, question):
        self.title = title
        self.question = question
 
        # WINDOW CONTENTS
        self.layout = [
            # TOP VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # ???
            [
                psg.Push(background_color=self.background_color_global),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE CONTENT
            [
                psg.Push(background_color=self.background_color_global),
                psg.Image(
                    self.logo,
                    pad=((5,35),(5,5)),
                    expand_x=False,
                    background_color=self.background_color_global,
                    ),
                psg.Text(
                    self.question,
                    font=(self.prompt_font, self.prompt_font_size, self.prompt_font_style),
                    text_color=self.prompt_font_color,
                    pad=((0,0),(0,0)), 
                    expand_x=False,
                    background_color=self.sunken_background_color_global,
                    ),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # YES OR NO BUTTON ROW
            [
                psg.Push(background_color=self.background_color_global),
                psg.Yes(
                    pad=((0,30),(0,0)),
                    button_color=(self.button_text_color, self.button_color),
                    font=(self.button_font, self.button_font_size, self.button_font_style),
                    ), 
                psg.No(
                    pad=((30,0),(0,0)),
                    button_color=(self.button_text_color, self.button_color),
                    font=(self.button_font, self.button_font_size, self.button_font_style),
                    ), 
                psg.Push(background_color=self.background_color_global)
            ],
            # BOTTOM VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
        ]

        self.window = psg.Window(
            title=self.title, 
            layout=self.layout,
            modal=True,
            no_titlebar=True,
            keep_on_top=True,
            finalize=True,
            grab_anywhere=False,
            grab_anywhere_using_control=False,
            disable_minimize=True,
            disable_close=True,
            size=(self.yesno_width, self.yesno_height),
            background_color=self.background_color_global,
            element_padding=None,
            margins=(0, 0, 0, 0),
            )
        
class Welcome(Window):
    def __init__(self, copyright):
        self.greeting = "Hi! I am SEM Apprentice.  Welcome :)"
        self.copyright = copyright
    
        # WINDOW CONTENTS
        self.layout = [
            # TOP VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # ???
            [
                psg.Push(background_color=self.background_color_global),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE CONTENT
            [
                psg.Push(background_color=self.background_color_global),
                psg.Image(
                    self.logo,
                    pad=((5,35),(5,5)),
                    expand_x=False,
                    background_color=self.background_color_global,
                    ),
                psg.Text(
                    self.greeting,
                    font=(self.prompt_font, self.prompt_font_size, self.prompt_font_style),
                    text_color=self.prompt_font_color,
                    pad=((0,0),(0,0)), 
                    expand_x=False,
                    background_color=self.sunken_background_color_global,
                    ),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # MAIN CONTENT
            [   
                psg.Push(background_color=self.background_color_global),
                psg.Text(
                    '\n'.join(self.copyright),
                    text_color=self.sunken_background_color_global,
                    background_color=self.background_color_global,
                    font=("default", 10, "bold"),
                    size=(70,9),
                    ),
                psg.Push(background_color=self.background_color_global),
                ],
            [psg.VPush(background_color=self.background_color_global)],
            [   psg.Push(background_color=self.background_color_global),
                psg.Multiline(
                    pad=((0,0),(5,0)),
                    size=(80,5),
                    autoscroll=True,
                    background_color=self.background_color_global,
                    text_color=self.sunken_background_color_global,
                    font=("default", 10, "bold"),
                    border_width=0,
                    auto_refresh=True,
                    reroute_stdout=True,
                    do_not_clear=True,
                    no_scrollbar=True,
                    ),
                psg.Push(background_color=self.background_color_global),
            ],
            # BOTTOM VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
        ]

        self.window = psg.Window(
            title="Welcome",
            layout=self.layout,
            modal=True,
            no_titlebar=True,
            keep_on_top=True,
            finalize=True,
            grab_anywhere=False,
            grab_anywhere_using_control=False,
            disable_minimize=True,
            disable_close=True,
            size=(self.yesno_width, 400),
            background_color=self.background_color_global,
            element_padding=None,
            margins=(0, 0, 0, 0),
            )

class Status(Window):
    
    def __init__(self, message):
        self.message = message
    
        # WINDOW CONTENTS
        self.layout = [
            # TOP VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # ???
            [
                psg.Push(background_color=self.background_color_global),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE CONTENT
            [
                psg.Push(background_color=self.background_color_global),
                psg.Image(
                    self.logo,
                    pad=((5,35),(5,5)),
                    expand_x=False,
                    background_color=self.background_color_global,
                    ),
                psg.Text(
                    self.message,
                    font=(self.prompt_font, self.prompt_font_size, self.prompt_font_style),
                    text_color=self.prompt_font_color,
                    pad=((0,0),(0,0)), 
                    expand_x=False,
                    background_color=self.sunken_background_color_global,
                    # relief='sunken',
                    ),
                psg.Push(background_color=self.background_color_global),
            ],
            # BOTTOM VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
        ]

        self.window = psg.Window(
            title="Status",
            layout=self.layout,
            modal=True,
            no_titlebar=True,
            keep_on_top=True,
            finalize=True,
            grab_anywhere=False,
            grab_anywhere_using_control=False,
            disable_minimize=True,
            disable_close=True,
            size=(self.yesno_width, self.yesno_height),
            background_color=self.background_color_global,
            element_padding=None,
            margins=(0, 0, 0, 0),
            auto_close=True,
            auto_close_duration=1.1,
            )    




    




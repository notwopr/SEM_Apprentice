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
    def __init__(self, current_dir):
        self.greeting = "Hi! I am SEM Apprentice.  Welcome :)"
    
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
                    # justification='center', 
                    background_color=self.sunken_background_color_global,
                    # relief='sunken',
                    ),
                psg.Push(background_color=self.background_color_global),
            ],
            # MIDDLE VERTICAL SPACER
            [psg.VPush(background_color=self.background_color_global)],
            # YES OR NO BUTTON ROW
            [   psg.Push(background_color=self.background_color_global),
                psg.Multiline(
                    size=(80,15),
                    autoscroll=True,
                    background_color='black',
                    text_color='white',
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
            icon=f"{current_dir}/mikey.ico",
            )

class Status(Window):
    
    def __init__(self, message, current_dir):
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
            icon=f"{current_dir}/mikey.ico",
            auto_close=True,
            auto_close_duration=1,
            )    




    



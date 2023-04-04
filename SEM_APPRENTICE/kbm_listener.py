from pynput import mouse, keyboard

class KBMListener:
    def __init__(self, sem_apprentice):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)#, on_release=self.on_release)
        self.mouse_listener = mouse.Listener(on_scroll=self.on_scroll, on_move=self.on_move, on_click=self.on_click)
        self.listener_pause = False
        self.sem_apprentice = sem_apprentice

    def on_scroll(self, x, y, dx, dy):
        # if listener not suspended...
        if not self.listener_pause:
            # print('scroll')
            self.sem_apprentice.gen_log_msg(f"SCROLLED ({x}, {y}) ({dx}, {dy})")

            # If user moves mouse to upperleft corner and scrolls
            if x<2 and y<2:
                # suspend all listener activity
                self.listener_pause = True
                self.sem_apprentice.pause_queue.put("pause")

    def on_press(self, key):
        # if listener not suspended...
        if not self.listener_pause:
            # print('press')
            self.sem_apprentice.snap_and_save('PRESSED', key, 'keyboard')

    def on_release(self, key):
        # if listener not suspended...
        if not self.listener_pause: 
            # print('release') 
            self.sem_apprentice.snap_and_save('RELEASED', key, 'keyboard')

    def on_move(self, x, y):
        # if listener not suspended...
        if not self.listener_pause:
            # print('moved')
            self.sem_apprentice.gen_log_msg(f"MOVED ({x}, {y})")  # coordinates are what mouse moved TO (according to pynput docs)

    def on_click(self, x, y, button, pressed):
        # if listener not suspended...
        if not self.listener_pause:
            if pressed:
                # print(f'clicked')  
                self.sem_apprentice.snap_and_save('CLICKED', [x, y, button], 'mouse')
            else:
                # print(f'unclicked') 
                self.sem_apprentice.snap_and_save('UNCLICKED', [x, y, button], 'mouse')
    
    def start(self):
        self.listener_pause = False
        self.mouse_listener.start()
        self.keyboard_listener.start()
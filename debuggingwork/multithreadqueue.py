import io
import sys
import threading
import queue
import pynput
import time


def on_press(key):
    return False

def on_release(key):
    return False

def on_move(x, y):
    return False

def on_click(x, y, button, pressed):
    return False

def on_scroll(x, y, dx, dy):
    return False

# Define a custom stream class that writes to the shared queue
class CustomStream(io.StringIO):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def write(self, *args, **kwargs):
        super().write(*args, **kwargs)
        self.queue.put(self.getvalue())
# Define a custom class for standard output and error output
class CustomOutput:
    def __init__(self, queue):
        self.queue = queue

    def write(self, s):
        self.queue.put(s)
        self.queue.task_done()

class CustomListener(pynput.mouse.Listener):
    def __init__(self, stdout, stderr, output_queue, allmessages):
        super().__init__()
        self.stdout = stdout
        self.stderr = stderr
        self.stdout = CustomOutput(output_queue)
        self.stderr = CustomOutput(output_queue)
        self.messages = allmessages

    def start(self, *args, **kwargs):
        super().write(*args, **kwargs)
        self.queue.put(self.getvalue())

# Define a function that listens for output from the shared queue
def add_new_messages(output_queue):
    while True:
        output = output_queue.get(block=True)
        # allmessages.append(output)
        print(output)
        output_queue.task_done()
        if output == 'last message':
            break



# Define a function that includes the keyboard and mouse listeners
def main():
    # Shared queue
    output_queue = queue.Queue()
    # print(threading.enumerate())
    output_thread = threading.Thread(target=add_new_messages, args=(output_queue,))
    output_thread.start()
    output_queue.put('msg 1')
    output_queue.put('msg 2')

    
    # time.sleep(1)
    # m_listener = pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener:
        # sys.stdout = CustomOutput(output_queue)
        # sys.stderr = CustomOutput(output_queue)
        # output_queue.put('msg 3')
        output_queue.put('last message')
        output_thread.join()
        exit()


if __name__ == '__main__':
    main()

    
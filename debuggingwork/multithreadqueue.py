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

# Shared queue
output_queue = queue.Queue()
# Save original stdout
original_stdout = sys.stdout
# Define a custom stream class that writes to the shared queue
class CustomStream(io.StringIO):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def write(self, *args, **kwargs):
        super().write(*args, **kwargs)
        self.queue.put(self.getvalue())
# Override stdout and stderr with custom streams
sys.stdout = CustomStream(output_queue)
sys.stderr = CustomStream(output_queue)
allmessages = []
# Define a function that listens for output from the shared queue
def listen_for_output(allmessages, output_queue):
    while True:
        try:
            output = output_queue.get()
            allmessages.append(output)
            output_queue.task_done()
        except output_queue.empty():
            break

# Start the output listener in a separate thread
output_thread = threading.Thread(target=listen_for_output, args=(allmessages, output_queue), daemon=True)
output_thread.start()

# Define a function that includes the keyboard and mouse listeners
def main():
    print('Main thread output')
    # time.sleep(1)
    with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as m_listener:
        
        print('Listener thread output')
        m_listener.join()
        
        # k_listener.join()
        
    
    # time.sleep(1)  # Add a delay to allow the daemon thread to run


if __name__ == '__main__':

    main()
    sys.stdout = original_stdout
    print(allmessages)
    # Revert stdout back to original
    
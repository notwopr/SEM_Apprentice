import win32clipboard

def print_available_formats():
    win32clipboard.OpenClipboard()
    try:
        formats = []
        format = win32clipboard.EnumClipboardFormats(0)
        while format:
            formats.append(format)
            format = win32clipboard.EnumClipboardFormats(format)
        print("Available clipboard formats:", formats)
    finally:
        win32clipboard.CloseClipboard()

print_available_formats()
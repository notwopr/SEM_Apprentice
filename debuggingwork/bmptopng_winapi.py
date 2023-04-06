import win32com.client

def bmp_to_png_winapi(bmp_filepath, png_filepath):
    # Create WIA image object
    wia_obj = win32com.client.Dispatch('WIA.ImageFile')
    
    # Load BMP file
    wia_obj.LoadFile(bmp_filepath)
    
    # Save as PNG file
    wia_obj.SaveAs(png_filepath, 23)
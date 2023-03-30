import winreg
import pythoncom

def get_wic_prog_id():
    try_CLSIDs = ['{CACAF262-9370-4615-A13B-9F5539DA4C0A}', '{BECF98FB-ECBD-4b5c-8C2E-5C5DEB4D882B}']
    for CLSID in try_CLSIDs:
        clsid_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f"CLSID\\{CLSID}")
        print(clsid_key)
        try:
            clsid_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f"CLSID\\{CLSID}")
            print(clsid_key)
            # with winreg.QueryInfoKey(clsid_key) as clsid_info:
            #     for i in range(clsid_info[1]):
            #         value_name, value_data, value_type = winreg.EnumValue(clsid_key, i)
            #         if value_name == "ProgID":
            #             return value_data
        except:
            pass
    raise Exception("Failed to get WIC ProgID")

print(get_wic_prog_id())
import winreg

def get_clsids():
    clsids = []
    with winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT) as root_key:
        with winreg.OpenKey(root_key, r"CLSID") as clsid_key:
            try:
                i = 0
                while True:
                    subkey_name = winreg.EnumKey(clsid_key, i)
                    subkey = winreg.OpenKey(clsid_key, subkey_name)
                    try:
                        with winreg.OpenKey(subkey, r"InProcServer32") as inproc_key:
                            value, _ = winreg.QueryValueEx(inproc_key, None)
                            if value.endswith(r"\windowscodecs.dll"):
                                clsids.append(subkey_name)
                    except FileNotFoundError:
                        pass
                    i += 1
            except OSError:
                pass
    return clsids

clsids = get_clsids()
print(clsids)

import win32api
import win32con
from pathlib import Path
import subprocess
import pprint


reg_root = win32con.HKEY_LOCAL_MACHINE
reg_paths=[
    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
    r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall',
    r'Software\Microsoft\Windows\CurrentVersion\Uninstall'
]


def get_all_installed_software():
    rst_dict = {}
    for path in reg_paths:
        pkey = win32api.RegOpenKeyEx(reg_root, path)
        for item in win32api.RegEnumKeyEx(pkey):
            value_paths = path + '\\' + item[0]
            try:
                vkey = win32api.RegOpenKeyEx(reg_root, value_paths)
                display_name, key_type = win32api.RegQueryValueEx(vkey, "DisplayName")
                uninstall_string, key_type = win32api.RegQueryValueEx(vkey, "UninstallString")
                rst_dict[display_name] = uninstall_string.replace('"', '')
                win32api.RegCloseKey(vkey)
            except:
                pass
        win32api.RegCloseKey(pkey)
    return rst_dict


def uninstall_software(software_name):
    uninstall_string = rst_dict.get(software_name, '')
    if uninstall_string == '':
        print('Not found installed program.')
        return
    print('uninstall ' + software_name)
    p = Path(uninstall_string)
    subprocess.Popen(p.name, cwd=p.parent)

if __name__ == '__main__':
    rst_dict = get_all_installed_software()
    # 所有软件名称列表
    softwares = list(rst_dict.keys())
    # uninstall_software('JPEXS Free Flash Decompiler')

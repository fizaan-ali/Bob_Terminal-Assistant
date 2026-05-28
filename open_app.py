import subprocess

APPS = {
    "notepad": r"notepad",
    "calculator": r"calc",
    "paint": r"mspaint",
    "file explorer": r"explorer",
    "task manager": r"taskmgr",
    "vs code": r"code",
    "winrar": r"C:\Program Files\WinRAR\WinRAR.exe",
    "media player": r"C:\Program Files\Windows Media Player\wmplayer.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "git": r"C:\Program Files\Git\git-cmd.exe",
    "idm": r"C:\Program Files (x86)\Internet Download Manager\IDMan.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "vlc": r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
}


def main():

    open_app("file explorer")


def open_app(app):
    """
    Function to open app for user if provided in dictionary
    """
    if app in APPS:
        print(f"Opening {app}....")
        subprocess.run([APPS[app]], shell=True)
    else:
        print("There is no such app like this here!!")


if __name__ == "__main__":
    main()

# used black module for reformatting

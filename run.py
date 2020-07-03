import pywinauto
from pywinauto.keyboard import send_keys
import time
if __name__ == '__main__':
    while True:
        try:
            browser = pywinauto.application.Application(backend="uia")
            apps = pywinauto.findwindows.find_elements(title_re=".*Netflix - Google Chrome")
            browser.connect(handle=apps[0].handle)
            browser_window = browser[apps[0].name]
            # browser_window.print_control_identifiers()
            try:
                button = browser_window.child_window(title="Skip Intro", control_type="Hyperlink")
                button.wait('visible', timeout=5)
                button.click_input()
                print("found")
                
            except:
                print("not found")
            time.sleep(1)
        except Exception as e:
            print("App doesn't found")

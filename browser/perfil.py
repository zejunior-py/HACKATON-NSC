import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# from helpers.environment_variables import FIREFOX_PROFILE_PATH
FIREFOX_PROFILE_PATH = '/home/datize/.mozilla/firefox/wd1flohx.default'


def perfil_browser(path_download=os.path.dirname(os.path.abspath(__file__)),
                   perfil=FIREFOX_PROFILE_PATH):
    fp = webdriver.FirefoxProfile(perfil)

    # Set to disable prompt.
    mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", path_download)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
    fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
    fp.set_preference("pdfjs.disabled", True)

    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(firefox_profile=fp, firefox_options=options)
    driver = webdriver.Firefox(firefox_profile=fp)

    return driver

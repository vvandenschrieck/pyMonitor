import os
import sys
import threading
import logging

os.environ["KIVY_NO_CONSOLELOG"] = "1"

from Presenter import Presenter
from gui.GUIView import GUIView
from shell.ShellView import PyMonitorShell
from website import website


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':

    # Log settings

    logger = logging.getLogger("pymonitor")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s -- %(name)s -- %(message)s")

    handler1 = logging.handlers.TimedRotatingFileHandler(
        "logs/info.log", when="s", interval=20, encoding="utf-8")
    handler1.setLevel(logging.INFO)
    handler1.setFormatter(formatter)
    logger.addHandler(handler1)
    handler2 = logging.handlers.TimedRotatingFileHandler(
        "logs/error.log", when="s", interval=5, encoding="utf-8")
    handler2.setLevel(logging.ERROR)
    handler2.setFormatter(formatter)
    logger.addHandler(handler2)
    handler3 = logging.handlers.TimedRotatingFileHandler(
        "logs/debug.log", when="s", interval=5, encoding="utf-8")
    handler3.setLevel(logging.DEBUG)
    handler3.setFormatter(formatter)
    logger.addHandler(handler3)


    # Load model

    sites = website.WebsitesList(resource_path("data/sites.txt"))

    # Launch view and presenter for ConsoleUI
    shell_pres = Presenter(sites)
    shell_view = PyMonitorShell(shell_pres, True)
    shell_pres.set_view(shell_view)
    x = threading.Thread(target=shell_view.cmdloop, args=(1,))
    x.start()
    # shell_view.cmdloop()
    # Launch view and presenter for GUI
    gui_pres = Presenter(sites)
    gui_view = GUIView(gui_pres)
    gui_pres.set_view(gui_view)
    gui_view.run()

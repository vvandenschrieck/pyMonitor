import os
import sys
import threading

from Presenter import Presenter
from gui.GUIView import GUIView
from shell.ShellView import PyMonitorShell
from website import website


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    # # Use parseargs to get params and options
    # parser = argparse.ArgumentParser(description='Easy Websites Monitoring.')
    # # File argument
    # parser.add_argument('file', metavar='FILE',
    #                     help="file containing the list of websites to monitor, one per line.", )
    # # Activate text coloring
    # parser.add_argument("-c", "--color", help="display colored test result",
    #                     action="store_true")
    # args = parser.parse_args()

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

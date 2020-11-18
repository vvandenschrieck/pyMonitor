#!python3

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
from termcolor import colored

from probes.state_probes import test_status_with_ping
from website.utils import load_sites


def check_websites(filename, color=False):
    """Extracts website from file and run a probe on it.  Results are immediately displayed. """
    # Extract list of sites from file given in parameters
    sites = load_sites(filename)
    for site in sites:
        site.test()
        if color:
            result = colored("Accessible", "green") if site.status == "OK" else colored("Inaccessible", "red")
        else:
            result = "Accessible" if site.status == "OK" else "Inaccessible"
        print(f"{site.name} \t\t: \t\t {result}")


if __name__ == '__main__':
    # Use parseargs to get params and options
    parser = argparse.ArgumentParser(description='Easy Websites Monitoring.')
    # File argument
    parser.add_argument('file', metavar='FILE', help="file containing the list of websites to monitor, one per line.", )
    # Activate text coloring
    parser.add_argument("-c", "--color", help="display colored test result", action="store_true")
    args = parser.parse_args()
    if args.color:
        check_websites(args.file, color=True)
    else:
        check_websites(args.file)

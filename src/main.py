import pyfiglet
import socket
import sys
import getopt


def port_scan(domain):
    for i in range(1, 65389):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            if s.connect_ex((domain,i)) == 0:
                print(f"[+] Porta {i} [TCP] aberta")

        except:
            print("Error in domain.")


if __name__ == "__main__":
    print(pyfiglet.figlet_format("PORT SCAN", font='cybermedium'))

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "domain="])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("Help Needed")

            elif opt in ("-d", "--domain"):
                port_scan(arg)

    except getopt.GetoptError as err:
        print(err)


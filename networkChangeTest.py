import socket
import sys
import subprocess
import osascript


def get_network_name():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8,1'))
        network_name = s.getsockname()[0]
    except:
        network_name = 'Baglanti Basarisiz!'
    finally:
        s.close()
    return network_name

def main():
    old_network_name = get_network_name()
    while True:
        new_network_name = get_network_name()
        if new_network_name != old_network_name:
            subprocess.call(['osascript','-e',f'display nofication "ağ değişikliği aldılandi: {new_network_name}" with title "ağ Değişikliği"'])
        old_network_name = new_network_name

    if __name__ == '__main__':
        main()
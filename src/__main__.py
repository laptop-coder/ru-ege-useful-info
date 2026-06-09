import signal
from handle_signals import receive_signal
from time import sleep


def main():
    signal.signal(signal.SIGUSR1, receive_signal)
    while True:
        sleep(1)


if __name__ == "__main__":
    main()

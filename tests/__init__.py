import sys
import signal


def cleanup(*args):
    print("The program is stopping")
    sys.exit(0)


def main():
    pass


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        main()
    except KeyboardInterrupt:
        cleanup()

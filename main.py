import clv
import threading, time

def sample_clv(stop_event):
    print("Self destruct in progress", end="")
    strings = ["...."]
    while not stop_event.is_set():
        clv.writeToStdOut(strings, delay=0.2)

def do_sth():
    time.sleep(5)

def main():
    clv.cout(5, "Self destruct in: ", False)
    print()

    stop_event = threading.Event()
    a = threading.Thread(target=sample_clv, args=(stop_event,))
    a.start()

    b = threading.Thread(target=do_sth)
    b.start()

    b.join() # wait until b is done
    stop_event.set() # stop a

    print(f"\nSelf destruct complete")

if __name__ == "__main__":
    main()

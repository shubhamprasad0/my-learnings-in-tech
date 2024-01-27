import threading
import time

def read_big_file_1():
    print("Reading Big File 1: STARTED")
    time.sleep(2)
    print("Reading Big File 1: DONE")

def read_big_file_2():
    print("Reading Big File 2: STARTED")
    time.sleep(3)
    print("Reading Big File 2: DONE")

def main():
    start = time.perf_counter()
    t1 = threading.Thread(target=read_big_file_1)
    t2 = threading.Thread(target=read_big_file_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    # The two files get read in ~3 seconds 
    print(f"Done in {end - start:.4f} secs")

if __name__ == "__main__":
    main()
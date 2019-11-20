import os
from multiprocessing import Process, current_process

def square(num):
    result = num * num
    process_id = os.getpid()
    print(f"process Id: {process_id}")
    print(f"The number {num} squares to {result}")

processes = []

if __name__ == '__main__':

    for n in range(1,5):
        process = Process(target=square, args=(n,))
        processes.append(process)

        # processes are spawned by creating an object
        process.start()

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        # executor.map(download_image, img_urls)
    
import logging

from fastapi import FastAPI
import time
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def thread_function(name):
    logger.info("Thread %s: starting", name)
    time.sleep(2)
    logger.info("Thread %s: finishing", name)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/process")
def process():
    threads = list()
    for index in range(3):
        logger.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logger.info("Main    : before joining thread %d.", index)
        thread.join()
        logger.info("Main    : thread %d done", index)

    return {"Done": "Process Completed"}
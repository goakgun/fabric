import threading


class ThreadHandler(object):
    def __init__(self, name, callable, *args, **kwargs):
        # Set up exception handling
        self.exception = None
        def wrapper(*args, **kwargs):
            try:
                callable(*args, **kwargs)
            except BaseException, e:
                self.exception = e
        # Kick off thread
        thread = threading.Thread(None, wrapper, name, args, kwargs)
        thread.setDaemon(True)
        thread.start()
        # Make thread available to instantiator
        self.thread = thread

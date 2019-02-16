from threading import Thread


class Producer(Thread):
    """
    Produce integers into buffer
    """
    def __init__(self, _buffer_):
        Thread.__init__(self)
        self._buffer_ = _buffer_

    def run(self):

        # place values from 1 to 10
        for i in range(1, 11):
            self._buffer_._produce_(i)

        print "Producer has finished"
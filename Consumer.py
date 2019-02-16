from threading import Thread, Lock


class Consumer(Thread):
    """
    Consumes integers
    """
    _ans_ = []
    _global_index_ = 0
    _mutexC_ = Lock()

    def __init__(self, _limit_, _buffer_):
        Thread.__init__(self)
        self._limit_ = _limit_
        self._buffer_ = _buffer_
        self._mutex_ = Lock()

    @staticmethod
    def _count_extractions_():
        Consumer._mutexC_.acquire()
        _aux_ = Consumer._global_index_
        Consumer._global_index_ += 1
        Consumer._mutexC_.release()

    def run(self):

        while True:
            # Extracted at _aux_ moment
            Consumer._count_extractions_()
            if Consumer._global_index_ > self._limit_:
                break
            _val_ = self._buffer_._consume_()
            self._mutex_.acquire()
            Consumer._ans_.append(_val_)
            self._mutex_.release()
from threading import Semaphore, Lock


class Buffer:
    """
    Buffer with a certain size
    """
    # Moment of extraction
    _time_ = 0

    def __init__(self, _size_):
        self._produce_index_ = 0
        self._consume_index_ = 0

        self._buffer_ = []
        # Limited buffer
        for i in range(_size_):
            self._buffer_.append(0)

        self._add_ = Semaphore(_size_)
        self._take_ = Semaphore(0)
        self._mutexP_ = Lock()
        self._mutexC_ = Lock()
        self._check_ans_ = []

    def _produce_(self, val):
        self._add_.acquire()

        self._mutexP_.acquire()
        self._buffer_[self._produce_index_] = val
        self._produce_index_ = (self._produce_index_ + 1) % len(self._buffer_)
        self._check_ans_.append(val)
        self._mutexP_.release()

        self._take_.release()

    def _consume_(self):
        self._take_.acquire()

        self._mutexC_.acquire()
        _aux_ = Buffer._time_
        Buffer._time_ += 1
        aux = self._buffer_[self._consume_index_]
        self._consume_index_ = (self._consume_index_ + 1) % len(self._buffer_)
        self._mutexC_.release()

        self._add_.release()
        return aux, _aux_

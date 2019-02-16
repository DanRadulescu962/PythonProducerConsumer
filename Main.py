import Buffer, Producer, Consumer


def main():
    """"
    Test functionality
    """
    _buffer_ = Buffer.Buffer(4)

    threads = []

    for i in range(3):
        _aux_ = Producer.Producer(_buffer_)
        threads.append(_aux_)

    for i in range(5):
        _aux_ = Consumer.Consumer(30, _buffer_)
        threads.append(_aux_)

    for i in range(8):
        threads[i].start()

    for i in range(8):
        threads[i].join()

    Consumer.Consumer._ans_.sort(key=lambda x: x[1])
    print map(lambda x: x[0], Consumer.Consumer._ans_)
    print _buffer_._check_ans_


if __name__ == "__main__":
    main()

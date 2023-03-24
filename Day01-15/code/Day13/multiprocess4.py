from time import time


def main():
    number_list = list(range(1, 100000001))
    start = time()
    total = sum(number_list)
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
from argparse import ArgumentParser
from .fibonacci import fibonacci

parser = ArgumentParser()
parser.add_argument('N', type=int)


def main():
    args = parser.parse_args()

    for n in range(args.N):
        print(fibonacci(n))


if __name__ == '__main__':
    main()

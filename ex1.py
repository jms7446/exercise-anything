
from dataclasses import dataclass


@dataclass
class LoginEvent:
    username: str
    ip: str


def main():
    le = LoginEvent('a', 'b')
    print(le)


if __name__ == '__main__':
    main()

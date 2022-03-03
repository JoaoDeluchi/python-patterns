from dataclasses import dataclass
from handlers.handlers import handlers_list


@dataclass
class Request:
    request_type: str
    request_detail: str


REQUESTS = [
    Request('dogs', 'walk twice a day'),
    Request('cats', 'see how pretty they are'),
    Request('fish', 'keep the tank clean'),
    Request('parrot', 'check for signs of life'),
    Request('tarantula', 'who keeps a tarantula as a pet?')
]


def main():
    for req in REQUESTS:
        handlers_list.handle(req)


if __name__ == '__main__':
    main()

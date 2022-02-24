from .command_abc import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, args) -> None:
        self._command = args[0]
        pass

    def execute(self):
        print(f'No Command named {self._command}')

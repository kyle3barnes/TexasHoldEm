from Input import Input


class ConsoleInput(Input):
    def get_string(self, message):
        return input(message)

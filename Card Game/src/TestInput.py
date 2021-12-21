from Input import Input


class TestInput(Input):
    test_inputs = []

    def set_test_inputs(self, test_inputs):
        self.test_inputs = test_inputs

    def get_string(self):
        return self.test_inputs.pop(0)

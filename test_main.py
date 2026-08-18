
import main 

class TestCaluladora:

    def test_add(self):
        assert 4 == main.add(2, 2)

    def test_subtraction(self):
        assert 2 == main.subtract(4,2)

    def test_multiplication(self):
        assert 100 == main.multiply(10, 10)
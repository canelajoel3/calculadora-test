
import main 

class TestCaluladora:

    def test_add(self):
        assert 4 == main.add(2, 2)

    def test_subtraction(self):
        assert 2 == main.subtract(4,2)
        
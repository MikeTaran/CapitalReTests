import pytest


class TestOne:
    data = []

    @pytest.mark.parametrize('num', [1, 5, 4, 5, 2, 11])
    def test_one(self, num):
        if num < 5:
            TestOne.data.append(num)
        if num == 11:
            print(TestOne.data)


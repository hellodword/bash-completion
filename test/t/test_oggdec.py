import pytest


class Test(object):

    @pytest.mark.complete("oggdec ")
    def test_(self, completion):
        assert completion.list

    @pytest.mark.complete("oggdec --")
    def test_dash(self, completion):
        assert completion.list
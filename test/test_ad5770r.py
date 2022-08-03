import pytest

hardware = "ad5770r"
classname = "adi.ad5770r"

#########################################
@pytest.mark.iio_hardware(hardware)
@pytest.mark.parametrize("classname", [(classname)])
@pytest.mark.parametrize("channel", [0, 1, 2, 3, 4, 5, 6])
def test_ad5593_test(iio_uri, classname, channel):
    test_ad5593_test(iio_uri, classname, channel)
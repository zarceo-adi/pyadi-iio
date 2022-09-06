import pytest

hardware = ["ad7768-4"]
classname = "adi.cn0579"

#########################################
@pytest.mark.iio_hardware(hardware)
@pytest.mark.parametrize("classname", [(classname)])
@pytest.mark.parametrize("channel", [0, 1, 2, 3])
def test_cn0579_rx_data(test_dma_rx, iio_uri, classname, channel):
    test_dma_rx(iio_uri, classname, channel)


#########################################
@pytest.mark.iio_hardware(hardware)
@pytest.mark.parametrize("classname", [(classname)])
@pytest.mark.parametrize(
    "attr, val",
    [
        (
            "sample_rate",
            [
                1000,
                2000,
                4000,
                8000,
                16000,
                32000,
                64000,
                128000,
                256000,
                16000,
            ],  # End on a rate compatible with all power modes
        ),
        ("filter_type", ["WIDEBAND", "SINC5"],),
        ("power_mode", ["LOW_POWER_MODE", "MEDIAN_MODE", "FAST_MODE"],),
    ],
)
def test_ad4630_attr(test_attribute_multipe_values, iio_uri, classname, attr, val):
    test_attribute_multipe_values(iio_uri, classname, attr, val, 0)

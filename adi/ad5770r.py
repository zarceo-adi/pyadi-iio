# Copyright (C) 2022 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from numpy import outer
from adi.attribute import attribute
from adi.context_manager import context_manager
from adi.rx_tx import tx

from calendar import c
from decimal import Decimal

class ad5770r(context_manager, tx):

    channel = []  # type: ignore
    _device_name = ""

    def __init__(self, uri = "", device_index=0):
        context_manager.__init__(self, uri, self._device_name)
        self._device_name = "ad5770r"

        self._ctrl = self._ctx.find_device("ad5770r")
        self._txdac = self._ctx.find_device("ad5770r")

        for ch in self._ctrl.channels:
            name = ch.id
            output = ch._output
            self._tx_channel_names.append(name)
            self.channel.append(self._channel(self._ctrl, name, output))

        self.ctrl = None
        tx.__init__(self)

    class _channel(attribute):
        # AD5770r current channel
        def __init__(self, ctrl, channel_name, output):
            self.name = channel_name
            self._ctrl = ctrl
            self._output = output

        @property
        # AD5770r channel 3dB low pass filter frequency
        def filter_low_pass_3db_frequency(self):
            return self._get_iio_attr(self.name, "filter_low_pass_3db_frequency", self._output)

        @property
        # AD5770r channel 3dB low pass filter frequency available
        def filter_low_pass_3db_frequency_available(self):
            return self._get_iio_attr(self.name, "filter_low_pass_3db_frequency_available", self._output)

        @property
        #AD5770r channel offset value
        def offset(self):
            return self._get_iio_attr(self.name, "offset", self._output)

        @property
        #AD5770r channel powerdown value
        def powerdown(self):
            return self._get_iio_attr(self.name, "powerdown", self._output)

        @property
        #AD5770r channel raw value
        def raw(self):
            return self._get_iio_attr(self.name, "raw", self._output)

        @property
        # AD5770r channel scale (gain)
        def scale(self):
            return float(self._get_iio_attr_str(self.name, "scale", self._output))

        @filter_low_pass_3db_frequency.setter
        def filter_low_pass_3db_frequency(self, value):
            filter_low_pass_3db_frequency_available = self._get_iio_attr(self.name, "filter_low_pass_3db_frequency_available", self._output)
            for set_filter_value in filter_low_pass_3db_frequency_available:
                if set_filter_value == value:
                    self._set_iio_attr(self.name, "filter_low_pass_3db_frequency", self._output, value)

        @powerdown.setter
        def powerdown(self, value):
            if self._output == True:
                self._set_iio_attr(self.name, "powerdown", self._output, value)

        @raw.setter
        def raw(self, value):
            if self._output == True:
                self._set_iio_attr(self.name, "raw", True, str(int(value)))

        @scale.setter
        def scale(self, value):
            scale_available = self._get_iio_attr(self.name, "scale_available", self._output)
            for set_scale_available in scale_available:
                if set_scale_available == value:
                    self._set_iio_attr(self.name, "scale", self._output, str(Decimal(value).real))


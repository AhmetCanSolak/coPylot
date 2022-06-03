from time import sleep

import nidaqmx


class NIDaq:
    """
    NI DAQ card adapter.
    """
    def __init__(self):
        pass

    @staticmethod
    def run(value):
        ch_ao0 = "cDAQ1AO/ao0"
        ch_ctr0_internal_output = "/cDAQ1/Ctr0InternalOutput"

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(ch_ao0)
            task.timing.cfg_samp_clk_timing(
                rate=2,
                sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS
            )
            task.write(value)
            task.start()
            sleep(len(value) / 2)
            task.stop()


if __name__ == '__main__':
    nidaq = NIDaq()
    nidaq.run([0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5, 0.1, 0.5])
    nidaq.run([0.5, 0.9])

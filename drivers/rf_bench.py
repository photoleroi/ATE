import numpy as np

class SignalGenerator:
    def __init__(self, resource):
        self.inst = resource

    def set_frequency(self, freq_mhz: float):
        self.inst.write(f"FREQ {freq_mhz:.2f} MHz")

    def set_power(self, power_dbm: float):
        self.inst.write(f"POW {power_dbm:.2f} dBm")

    def rf_output(self, state: bool):
        self.inst.write("OUTP ON" if state else "OUTP OFF")

class SpectrumAnalyzer:
    def __init__(self, resource):
        self.inst = resource

    def set_center_frequency(self, freq_mhz: float):
        self.inst.write(f"FREQ:CENT {freq_mhz:.2f} MHz")

    def measure_dut_power(self, input_freq_mhz: float, input_power_dbm: float) -> float:
        # SCPI-Kommando an den simulierten Analysator senden
        self.set_center_frequency(input_freq_mhz)
        
        # Physikalisches Modell eines 433.92 MHz Bandpassfilters (DUT)
        center_freq = 433.92
        bandwidth = 20.0
        insertion_loss = 1.5  # dB
        
        # Filterkurve + realistisches Messrauschen (+/- 0.2 dB)
        attenuation = insertion_loss + 20 * np.log10(1 + ((input_freq_mhz - center_freq) / (bandwidth / 2))**2)
        noise = np.random.normal(0, 0.2)
        
        return round(input_power_dbm - attenuation + noise, 2)

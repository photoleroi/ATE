import numpy as np
import matplotlib.pyplot as plt

def test_bandpass_filter_sweep(rf_setup):
    sig_gen, spec_an = rf_setup
    input_power = 0.0  # dBm
    frequencies = np.linspace(380.0, 490.0, 50)
    measured_powers = []

    sig_gen.set_power(input_power)
    sig_gen.rf_output(True)

    for freq in frequencies:
        sig_gen.set_frequency(freq)
        power = spec_an.measure_dut_power(freq, input_power)
        measured_powers.append(power)

    # Diagramm generieren
    plt.figure(figsize=(8, 4))
    plt.plot(frequencies, measured_powers, label="DUT Frequenzgang")
    plt.axhline(-3.0, color="r", linestyle="--", label="-3 dB Grenze")
    plt.title("Automatisierter HF-Bandpassfilter Sweep (433.92 MHz)")
    plt.xlabel("Frequenz [MHz]")
    plt.ylabel("Ausgangsleistung [dBm]")
    plt.grid(True)
    plt.legend()
    plt.savefig("filter_response.png")

    # Prüfung 1: Einfügedämpfung bei Mittenfrequenz (index 24 liegt nahe 433.92 MHz)
    center_power = max(measured_powers)
    assert -2.5 <= center_power <= -1.0, f"Einfügedämpfung fehlerhaft: {center_power} dBm"

    # Prüfung 2: Sperrdämpfung an den Bandgrenzen (380 MHz und 490 MHz)
    assert measured_powers[0] < -25.0, f"Sperrdämpfung bei 380 MHz zu gering: {measured_powers[0]} dBm"
    assert measured_powers[-1] < -25.0, f"Sperrdämpfung bei 490 MHz zu gering: {measured_powers[-1]} dBm"

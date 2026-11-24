# RF Automated Test Equipment (ATE) – Bandpass Filter Characterization

An automated RF test bench built with **Python**, **PyVISA**, and **Pytest**. This project demonstrates how to remotely control RF laboratory instruments via SCPI commands, perform automated frequency sweeps, and validate a Device Under Test (DUT) against hardware specifications.

Using `pyvisa-sim`, the test bench simulates a real-world hardware setup (Signal Generator + Spectrum Analyzer), making the entire suite reproducible without physical lab equipment.

---

## 🎯 Project Highlights & Architecture

* **Hardware Abstraction Layer (HAL):** Clean separation between instrument SCPI drivers (`drivers/`) and test logic (`tests/`).
* **Safe Instrument Teardown:** Uses `pytest` fixtures (`yield`) to guarantee that the RF output is switched `OFF` after test execution—even if a test fails or aborts—protecting sensitive RF frontends.
* **Automated Specification Verification:** Validates insertion loss in the passband (433.92 MHz) and attenuation in the stopbands (380 MHz / 490 MHz).
* **Automated Reporting & Visualization:** Generates a frequency response plot (`filter_response.png`) after every sweep.

---

## 📁 Project Structure

```text
ATE/
├── drivers/
│   └── rf_bench.py             # SCPI instrument wrappers & DUT response model
├── sim/
│   └── rf_instruments.yaml     # PyVISA-sim definitions (R&S SMB100A & Keysight N9020B)
├── tests/
│   └── test_filter_sweep.py    # Automated frequency sweep & Pass/Fail assertions
├── conftest.py                 # Pytest fixtures for VISA resource management & safety teardown
├── requirements.txt            # Project dependencies
└── README.md
```

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Instrument Control:** `PyVISA` & `PyVISA-sim` (SCPI over virtual USB-TMC)
* **Test Framework:** `Pytest`
* **Data Analysis & Plotting:** `NumPy`, `Matplotlib`

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com<your-username>/ATE.git](https://github.com/photoleroi/ATE.git)
cd ATE
```

### 2. Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 4. Run the automated test suite
```bash
python3 -m pytest -v
```

---

## 📊 Example Output

Running the test suite executes a 50-point frequency sweep from **380 MHz to 490 MHz** on a simulated 433.92 MHz bandpass filter:

1. **Passband Check (433.92 MHz):** Verifies insertion loss is within `-2.5 dBm` to `-1.0 dBm`.
2. **Stopband Rejection (380 MHz & 490 MHz):** Verifies out-of-band attenuation exceeds `25 dB`.
3. **Plot Generation:** Saves the measured frequency response curve as `filter_response.png` in the root directory.

---

## 🔮 Future Improvements

* [ ] Add cable loss calibration offset table (CSV/JSON) to de-embed test fixture losses.
* [ ] Integrate `pytest-html` to embed the generated frequency plots directly into an HTML test report.
* [ ] Add GitHub Actions CI workflow to automatically run the simulated hardware tests on every push.

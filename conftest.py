import pytest
import pyvisa
from drivers.rf_bench import SignalGenerator, SpectrumAnalyzer

@pytest.fixture(scope="session")
def rf_setup():
    rm = pyvisa.ResourceManager("sim/rf_instruments.yaml@sim")
    
    gen_res = rm.open_resource("USB0::0x0AAD::0x0054::100001::INSTR")
    sa_res = rm.open_resource("USB0::0x2A8D::0x1B0B::200002::INSTR")
    
    sig_gen = SignalGenerator(gen_res)
    spec_an = SpectrumAnalyzer(sa_res)
    
    yield sig_gen, spec_an
    
    # Sicherheits-Teardown: HF-Ausgang immer abschalten
    sig_gen.rf_output(False)
    gen_res.close()
    sa_res.close()
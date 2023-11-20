import pytest
from contoh4_19 import *

def test_inputPengguna(monkeypatch):
    # Simulate user input "10.5"
    monkeypatch.setattr('builtins.input', lambda _: "10.5")
    assert inputPengguna("Masukkan harga kos RM ") == 10.5

def test_kiraPeratus(capsys):
    h1 = 10.0
    h2 = 15.0
    kiraPeratus(h1, h2)
    captured = capsys.readouterr()
    assert "Keuntungan ialah 50.0 %" in captured.out

    h1 = 15.0
    h2 = 10.0
    kiraPeratus(h1, h2)
    captured = capsys.readouterr()
    assert "Kerugian ialah 33.33 %" in captured.out

    h1 = 10.0
    h2 = 10.0
    kiraPeratus(h1, h2)
    captured = capsys.readouterr()
    assert "Tiada keuntungan" in captured.out


# if __name__ == "__main__":
#     pytest.main()








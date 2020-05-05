from .calc import PocketCalculator


def test_init():
    calc = PocketCalculator()
    assert calc.value == 0


def test_set():
    calc = PocketCalculator()
    calc.set(12345)
    assert calc.value == 12345
    calc.set(42)
    assert calc.value == 42


def test_add():
    calc = PocketCalculator()
    calc.set(42)
    calc.add(42)
    assert calc.value == 84
    calc.add(42)
    assert calc.value == 126


def test_sub():
    calc = PocketCalculator()
    calc.set(126)
    calc.sub(62)
    assert calc.value == 64


def test_mul():
    calc = PocketCalculator()
    calc.set(64)
    calc.mul(2)
    assert calc.value == 128


def test_div():
    calc = PocketCalculator()
    calc.set(128)
    calc.div(16)
    assert calc.value == 8


def test_reset():
    calc = PocketCalculator()
    calc.set(8)
    calc.reset()
    assert calc.value == 0

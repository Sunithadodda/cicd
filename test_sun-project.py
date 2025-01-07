# test_sun_project.py

def test_addition(a, b):
    return a + b

def test_addition_valid():
    assert test_addition(1, 3) == 4  # Passes
    assert test_addition(1, 4) == 5 

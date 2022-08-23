def my_add(a, b):
    result = a + b
    return result

def my_mul(a, b):
    result = a * b
    return result

def test_my_add():
    assert my_add(3, 2) ==  5

def test_my_mul():
    assert my_mul(3, 2) == 6 

# (py3_venv) [cucurullo@pylab28a test_ex3]$ py.test -s -v test_simple.py
# ==================================================================== test session starts =====================================================================
# platform linux -- Python 3.7.10, pytest-7.0.1, pluggy-1.0.0 -- /home/cucurullo/VENV/py3_venv/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/cucurullo/Bonus2/test_ex3
# plugins: pylama-8.3.7
# collected 2 items                                                                                                                                            
# 
# test_simple.py::test_my_add PASSED
# test_simple.py::test_my_mul PASSED
# 
# ===================================================================== 2 passed in 0.01s ======================================================================
# 

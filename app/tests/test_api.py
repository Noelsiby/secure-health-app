def test_minimize():
<<<<<<< HEAD
    from app.compliance import data_minimize
=======
    from compliance import data_minimize
>>>>>>> c0b70c8a3a8ec317e248fdce5463bffa3cd1cac8
    p = {'id':'1','name':'A','dob':'2000-01-01','consent':True,'ssn':'X'}
    m = data_minimize(p)
    assert 'ssn' not in m and 'name' in m
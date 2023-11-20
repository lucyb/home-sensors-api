from src import database

def test_write_successful():
    assert database.write({})
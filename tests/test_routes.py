def test_hello_world(client_fixture):
    rv = client_fixture.get("/")
    assert b"Hello World!" == rv.data

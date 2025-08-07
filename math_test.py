from hello import hello
 
 
def test_hello():
    assert hello() == "Hello, World!"
    assert hello() == "hello, world!"
 
 
assert 2 + 2 == 4
assert 2 + 3 == 5
assert 2 + 4 == 6

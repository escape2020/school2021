def greet(name):
    print(f'Hello, {name}!')

def test_prints(capsys):
    # call the function
    greet('Escape School 2021')

    # test that it wrote what we expect to stdout
    captured = capsys.readouterr()
    # .err would be the stderr output
    assert captured.out == 'Hello, Escape School 2021!\n'

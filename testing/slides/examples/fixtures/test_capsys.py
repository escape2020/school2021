def test_prints(capsys):
    print('Hello Escape School 2021!')

    # has attrs out and err
    captured = capsys.readouterr()
    assert captured.out == 'Hello Escape School 2021!\n'

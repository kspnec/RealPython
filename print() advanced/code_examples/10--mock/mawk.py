def greet(name):
    print('Hello ', name)


from unittest.mock import patch

@patch('builtins.print')
def test_greet(mock_print):
    # the actual test
    greet('John')
    mock_print.assert_called_with('Hello ', 'John')
    greet('Eric')
    mock_print.assert_called_with('Hello ', 'Eric')

    # showing what is in mock
    import sys
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')

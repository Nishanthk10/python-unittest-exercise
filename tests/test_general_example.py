from src.general_example import GeneralExample
from unittest import mock

general_example_instance = GeneralExample()

def test_flatten_dictionary():

    expected = [0, 1, 2, 3, 10, 22, 42, 55]
    actual = general_example_instance.flatten_dictionary({'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]})

    assert expected == actual

@mock.patch("src.general_example.GeneralExample.load_employee_rec_from_database")
def test_fetch_emp_details(mock_load_employee_rec_from_database):

    mock_load_employee_rec_from_database.return_value = ['emp001', 'Sam', '100000']
    #mock_load_employee_rec_from_database = mock.Mock(name = 'load_employee_rec_from_database', return_value = ['emp001', 'Sam', '100000'])
    expected = {
        'empId': 'emp001',
        'empName': 'Sam',
        'empSalary': '100000'
    }

    actual = general_example_instance.fetch_emp_details()
    assert expected == actual

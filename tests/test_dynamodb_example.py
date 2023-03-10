import boto3
import pytest
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
from botocore.exceptions import ClientError



@mock_dynamodb2
def test_create_dynamo_table():
    '''
        Implement the test logic here for testing create_dynamo_table method
    
    '''
    expected = None

    obj = DynamodBExample()
    actual = obj.create_movies_table()
    assert actual == expected

@mock_dynamodb2
def test_table_attributes():

    # expected1 = [{'AttributeName': 'year', 'AttributeType': 'N'}, {'AttributeName': 'title', 'AttributeType': 'S'}]
    # expected2 = [{'AttributeName': 'year', 'KeyType': 'HASH'}, {'AttributeName': 'title', 'KeyType': 'RANGE'}]

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    obj = DynamodBExample()
    obj.create_movies_table()
    table = dynamodb.Table('Movies')
    attrs = table.attribute_definitions
    key = table.key_schema

    # assert attrs == expected1
    # assert key == expected2

    assert attrs[0]['AttributeName'] == 'year'
    assert attrs[0]['AttributeType'] == 'N'
    assert attrs[1]['AttributeName'] == 'title'
    assert attrs[1]['AttributeType'] == 'S'



@mock_dynamodb2
def test_add_dynamo_record_table():
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    obj = DynamodBExample()
    obj.create_movies_table()
    
    obj.add_dynamo_record('Movies',{'year' : 2023, 'title' : 'Sherlock Holmes'})
    table = dynamodb.Table('Movies')
    item = table.scan()

    assert item['Items'][0]['year'] ==2023
    assert item['Items'][0]['title'] == 'Sherlock Holmes'

    

@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    '''
        Implement the test logic here test_add_dynamo_record_table method for failures
    '''

    with pytest.raises(ClientError):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        obj = DynamodBExample()
        obj.create_movies_table()
        
        obj.add_dynamo_record('Movies',{'year' : '2023', 'title' : 'Sherlock Holmes'})


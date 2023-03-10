import pytest
import boto3
from moto import mock_dynamodb2
from boto3_example import DynamodBExample
from botocore.exceptions import ClientError




@mock_dynamodb2
def test_add_dynamo_record_table():
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    with pytest.raises(ClientError):
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        obj = DynamodBExample()
        obj.create_movies_table()
        
        obj.add_dynamo_record('Movies',{'year' : '2023', 'title' : 'Sherlock Holmes'})





    

test_add_dynamo_record_table()

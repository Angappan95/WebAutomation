import pytest
import requests
from jsonpath import jsonpath


@pytest.fixture(scope='session')
def url():
    return 'https://jsonplaceholder.typicode.com/'


@pytest.fixture(scope='module')
def get_user_id(url):
    path = 'users'
    name = 'Samantha'
    response = requests.get(f'{url}{path}')
    username = jsonpath(response.json(), '$..username')
    assert name in username, f'{name} is not present in the response| {username}'
    user_id = jsonpath(response.json(), '$.[?(@.username=="Samantha")].id')[0]
    return user_id


def test_get_post(url, get_user_id):
    path = 'posts'
    response = requests.get(f'{url}{path}', params={'userId': get_user_id})
    posts = jsonpath(response.json(), '$..body')
    assert len(posts) > 0, f'No posts mapped to the user| {posts}'

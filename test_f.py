from main import app
from main import Singleton
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
    


def test1(client):
    """Start with a blank database."""

    response = client.get('/')

    assert response.data.decode('utf-8') == 'hola'
    assert response.status_code == 200
    # assert 1 == 1

def test2(client):
    """Start with a blank database."""

    response = client.get('/hola')
    assert response.json['vamos a ver']  == 3
    # assert 1 == 1

def test3(client):
    """Start with a blank database."""

    response = client.post('/adios',json = {
        "2": 'no',
    })
    assert response.json['no vamos a ver']  == 'si' 

def test4(client):
    """Start with a blank database."""

    response = client.post('/adios',json = {
        "2": 'si',
    })
    assert response.json['no vamos a ver']  == 'no' 

def test5(client):
    """Start with a blank database."""

    response = None
    data = ['1324','31412','23141']
    for i in data: 
        response = client.post('/singleton',json = {
            "data": i,
        })
    assert int(response.json['len'])  == len(data) 


def test5(client):
    """Start with a blank database."""
    s =Singleton()
    assert s == Singleton.getInstance()



# def test5(client):
    # """Start with a blank database."""
    # s =Singleton()
    # with pytest.raises(Exception) as e:
        # Singleton()
    # assert e.value.args[0] == 'This class is a singleton!' 
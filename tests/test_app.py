import pytest
from ecarton_code_challenge.lib.app import create_app

testdata = [
  [['a'], [970]],
  [['alarm'], [970]],
  [['1'], [0]],
  [[None], [0]],
  [['z'], [0]],
  [['h'], [0]],
  [['a', 'h'], [970, 0]],
]

@pytest.fixture
def app():
    test_app = create_app()
    return test_app

@pytest.mark.parametrize('testvalues, expected',testdata)
def test_app_basic(app, testvalues, expected):

    response = app.test_client().post('/convert', json=testvalues)

    assert response.json == expected

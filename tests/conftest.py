import pytest
from model.model import read_dataset


@pytest.fixture()
def data():
    return read_dataset()

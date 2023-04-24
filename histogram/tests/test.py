import pytest
import os

TEMP_OUT='../out.txt'

TEST_TASK_PATH='../task.py'


@pytest.fixture()
def test_1():
    test_dir = './1/'

    
from skip_commit import data_prep, ml_training


def test_example():
    assert 1 == 1


def test_basic_working():
    print("test_basic_working**")
    print(data_prep.api_token)
    ml_training.do()
    assert 1 == 1

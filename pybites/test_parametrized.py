import pytest

def string_lengths(string: str):
    return len(string)

# the 'id' helps with identifying failing cases, or selecting only that test with pytest -k 'substring'
@pytest.mark.parametrize("output, expected", [
    pytest.param("four", 4, id="passes ok"),
    pytest.param("five", 5, id="fails assertion for test with 'five'")
])
def test_string_lengths(output, expected):
    assert string_lengths(output) == expected

from remove import remove_dups
import pytest

@pytest.mark.parametrize("input_list, list_no_dup", [
  (['a', 1, 3, 'b', 1], ['a', 1, 3, 'b']), 
  ([],[]),
  ("hello", ['h','e','l','o'])
])

def test_remove_dups(input_list, list_no_dup):
  assert (remove_dups(input_list) == list_no_dup)



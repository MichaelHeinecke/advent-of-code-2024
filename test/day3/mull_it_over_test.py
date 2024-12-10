from src.day3.mull_it_over import calculate_uncorrupted_memory_instructions_with_toggle


def test_instructions_with_toggle_are_calculated_correctly():
    memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected_result = 48

    actual_result = calculate_uncorrupted_memory_instructions_with_toggle(memory)

    assert expected_result == actual_result

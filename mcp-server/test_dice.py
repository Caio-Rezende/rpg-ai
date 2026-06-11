from dice_cli import roll_dice


def test_roll_4d6():
    """Test rolling four 6-sided dice."""
    print("Testing 4d6...")
    result = roll_dice("4d6")
    print(f"Result: {result}")
    assert len(result) == 4
    for val in result:
        assert 1 <= val <= 6


def test_roll_1d20():
    """Test rolling one 20-sided die."""
    print("Testing 1d20...")
    result = roll_dice("1d20")
    print(f"Result: {result}")
    assert len(result) == 1
    assert 1 <= result[0] <= 20


def test_roll_d20():
    """Test rolling d20 (omitted count defaults to 1)."""
    print("Testing d20...")
    result = roll_dice("d20")
    print(f"Result: {result}")
    assert len(result) == 1
    assert 1 <= result[0] <= 20


def test_roll_2d6_sum():
    """Test that 2d6 results are in valid range and sum is correct."""
    print("Testing 2d6...")
    result = roll_dice("2d6")
    print(f"Result: {result}")
    assert len(result) == 2
    for val in result:
        assert 1 <= val <= 6
    assert 2 <= sum(result) <= 12


def test_invalid_notation():
    """Test that invalid notation raises ValueError."""
    print("Testing invalid notation...")
    try:
        roll_dice("abc")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("Correctly raised ValueError for 'abc'")


def test_invalid_sides():
    """Test that 0 or negative sides raises ValueError."""
    print("Testing 0d6 (invalid sides)...")
    try:
        roll_dice("0d6")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("Correctly raised ValueError for '0d6'")


def test_roll_multiple_notations():
    """Test rolling multiple dice types in sequence."""
    print("Testing multiple rolls (3d8, 1d4)...")
    result_3d8 = roll_dice("3d8")
    result_1d4 = roll_dice("1d4")
    print(f"3d8 Result: {result_3d8}")
    print(f"1d4 Result: {result_1d4}")
    assert len(result_3d8) == 3
    for val in result_3d8:
        assert 1 <= val <= 8
    assert len(result_1d4) == 1
    assert 1 <= result_1d4[0] <= 4


def test_roll_dice():
    """Run all dice tests."""
    test_roll_4d6()
    test_roll_1d20()
    test_roll_d20()
    test_roll_2d6_sum()
    test_invalid_notation()
    test_invalid_sides()
    test_roll_multiple_notations()

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_roll_dice()

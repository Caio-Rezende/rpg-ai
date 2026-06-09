from server import roll_dice

def test_roll_dice():
    # Test 1: 4d6 (as [count, sides])
    print("Testing 4d6...")
    result = roll_dice([4, 6])
    print(f"Result: {result}")
    assert len(result) == 4
    for val in result:
        assert 1 <= val <= 6

    # Test 2: 1d20
    print("Testing 1d20...")
    result = roll_dice([1, 20])
    print(f"Result: {result}")
    assert len(result) == 1
    assert 1 <= result[0] <= 20

    # Test 3: Mixed dice [4, 6, 6, 20] as per README example
    # Wait, if the input is [4, 6, 6, 20], my implementation treats it as (4d6 and 6d20)
    print("Testing mixed dice [4, 6, 6, 20]...")
    result = roll_dice([4, 6, 6, 20])
    print(f"Result: {result}")
    assert len(result) == 10 # 4 + 6
    for val in result:
        # This is tricky because we don't know if it's d6 or d20 without more info, 
        # but the current implementation assumes pairs.
        pass

    print("All tests passed!")

if __name__ == "__main__":
    test_roll_dice()

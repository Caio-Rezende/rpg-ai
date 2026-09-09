import pytest
from logic import roll_dice

def test_roll_dice_empty():
    """Test rolling with an empty dice set."""
    assert roll_dice([]) == []

def test_roll_dice_single_set():
    """Test rolling a single set of dice (e.g., 4d6)."""
    count, sides = 4, 6
    result = roll_dice([count, sides])
    assert len(result) == count
    for val in result:
        assert 1 <= val <= sides

def test_roll_dice_mixed_sets():
    """Test rolling multiple sets of dice (e.g., 4d6 and 1d20)."""
    dice_set = [4, 6, 1, 20]
    result = roll_dice(dice_set)
    assert len(result) == 4 + 1
    for val in result:
        assert 1 <= val <= 20

def test_roll_dice_invalid_length():
    """Test that odd-length dice_set raises ValueError."""
    with pytest.raises(ValueError, match="dice_set must contain pairs of \(count, sides\)."):
        roll_dice([4, 6, 1])

def test_roll_dice_non_positive_values():
    """Test that non-positive counts or sides raise ValueError."""
    with pytest.raises(ValueError, match="Dice count and sides must be positive"):
        roll_dice([0, 6])
    with pytest.raises(ValueError, match="Dice count and sides must be positive"):
        roll_dice([4, -1])

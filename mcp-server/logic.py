import random

def roll_dice(dice_set: list[int]) -> list[int]:
    """
    Rolls multiple sets of dice and returns the individual results.

    Args:
        dice_set (list[int]): A list of integers where each pair represents (count, sides).
            Example: [4, 6, 1, 20] rolls 4d6 and 1d20.

    Returns:
        list[int]: A list containing the result of every individual die roll.

    Raises:
        ValueError: If the dice_set contains an odd number of elements or non-positive values.
    """
    if not dice_set:
        return []

    if len(dice_set) % 2 != 0:
        raise ValueError("dice_set must contain pairs of (count, sides).")

    results = []
    for i in range(0, len(dice_set), 2):
        count = dice_set[i]
        sides = dice_set[i+1]

        if count <= 0 or sides <= 0:
            raise ValueError(f"Dice count and sides must be positive. Got count={count}, sides={sides}")

        for _ in range(count):
            results.append(random.randint(1, sides))

    return results

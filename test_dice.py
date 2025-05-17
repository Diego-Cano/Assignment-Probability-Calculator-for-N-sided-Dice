"""
Test cases for the dice probability calculator.
"""

import unittest
from dice_calculator import roll_dice, simulate_multiple_rolls, calculate_probability_distribution


class TestDiceCalculator(unittest.TestCase):
    
    def test_roll_dice_range(self):
        """Test that roll_dice returns values within the expected range."""
        # Normal case 1: 2d6 (two six-sided dice)
        for _ in range(100):
            result = roll_dice(2, 6)
            self.assertTrue(2 <= result <= 12)
        
        # Normal case 2: 3d4 (three four-sided dice)
        for _ in range(100):
            result = roll_dice(3, 4)
            self.assertTrue(3 <= result <= 12)
        
        # Normal case 3: 1d20 (one twenty-sided die)
        for _ in range(100):
            result = roll_dice(1, 20)
            self.assertTrue(1 <= result <= 20)
    
    def test_simulate_multiple_rolls_length(self):
        """Test that simulate_multiple_rolls returns the expected number of results."""
        # Edge case 1: 1 simulation
        results = simulate_multiple_rolls(2, 6, 1)
        self.assertEqual(len(results), 1)
        
        # Normal case: 100 simulations
        results = simulate_multiple_rolls(2, 6, 100)
        self.assertEqual(len(results), 100)
        
        # Edge case 2: 0 simulations (returns empty list)
        results = simulate_multiple_rolls(2, 6, 0)
        self.assertEqual(len(results), 0)
    
    def test_probability_distribution_sum(self):
        """Test that probability distribution sums to approximately 1."""
        # Edge case 3: 1d1 (one one-sided die, always returns 1)
        probs = calculate_probability_distribution(1, 1, 1000)
        self.assertEqual(list(probs.keys()), [1])
        self.assertAlmostEqual(probs[1], 1.0)
        
        # Normal cases
        for dice, sides in [(2, 6), (3, 4), (1, 20)]:
            probs = calculate_probability_distribution(dice, sides, 10000)
            self.assertAlmostEqual(sum(probs.values()), 1.0, places=1)
            
            # Check that min and max values are within expected range
            min_sum = dice  # Minimum possible sum (all 1's)
            max_sum = dice * sides  # Maximum possible sum (all max values)
            self.assertTrue(all(min_sum <= sum_val <= max_sum for sum_val in probs.keys()))


if __name__ == '__main__':
    unittest.main()
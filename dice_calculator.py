"""
Dice Probability Calculator

This module contains functions for simulating dice rolls and calculating
probability distributions.
"""

import random
from collections import Counter


def roll_dice(num_dice, num_sides):
    """
    Task 1: Implementing the Dice Roll Function
    
    Simulates rolling a specified number of dice with a specified number of sides.
    
    Args:
        num_dice: Number of dice to roll
        num_sides: Number of sides on each die
        
    Returns:
        Sum of the dice roll outcomes
    """
    # Roll each die and sum the results
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    
    return total


def simulate_multiple_rolls(num_dice, num_sides, num_simulations):
    """
    Task 2: Simulating Multiple Rolls
    
    Simulates rolling dice multiple times and records the results.
    
    Args:
        num_dice: Number of dice to roll
        num_sides: Number of sides on each die
        num_simulations: Number of times to roll the dice
        
    Returns:
        List containing the sum result of each simulation
    """
    results = []
    
    for _ in range(num_simulations):
        roll_result = roll_dice(num_dice, num_sides)
        results.append(roll_result)
    
    return results


def calculate_probability_distribution(num_dice, num_sides, num_simulations):
    """
    Task 3: Calculating Probability Distribution
    
    Calculates the probability of each possible sum when dice are rolled.
    
    Args:
        num_dice: Number of dice to roll
        num_sides: Number of sides on each die
        num_simulations: Number of simulations to run
        
    Returns:
        Dictionary mapping each possible sum to its probability
    """
    # Get simulation results
    results = simulate_multiple_rolls(num_dice, num_sides, num_simulations)
    
    # Count occurrences of each sum
    counter = Counter(results)
    
    # Calculate probabilities
    probabilities = {}
    for sum_value, count in counter.items():
        probability = count / num_simulations
        probabilities[sum_value] = probability
    
    return probabilities


if __name__ == "__main__":
    # Simple test
    print(roll_dice(2, 6))
    print(simulate_multiple_rolls(2, 6, 10))
    print(calculate_probability_distribution(2, 6, 1000))
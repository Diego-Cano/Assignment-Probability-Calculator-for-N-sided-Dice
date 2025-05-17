"""
Main program for the dice probability calculator.
Provides a command-line interface for the user to interact with.
"""

from dice_calculator import calculate_probability_distribution


def display_probabilities(probabilities):
    """
    Display the probability distribution in a user-friendly way.
    
    Args:
        probabilities: Dictionary of sum -> probability
    """
    print("\nProbability Distribution:")
    print("-" * 30)
    print("Sum\tProbability\tPercentage")
    print("-" * 30)
    
    # Get sorted list of sums
    sorted_sums = sorted(probabilities.keys())
    
    for sum_val in sorted_sums:
        prob = probabilities[sum_val]
        percentage = prob * 100
        print(f"{sum_val}\t{prob:.6f}\t{percentage:.2f}%")


def main():
    """
    Task 4: User Interface
    
    Allow the user to input values and display the probability distribution.
    """
    print("=" * 50)
    print("Dice Probability Calculator")
    print("=" * 50)
    
    # Get user input
    try:
        num_sides = int(input("\nEnter the number of sides on each die (N): "))
        if num_sides <= 0:
            print("Number of sides must be positive!")
            return
            
        num_dice = int(input("Enter the number of dice to roll (M): "))
        if num_dice <= 0:
            print("Number of dice must be positive!")
            return
            
        num_simulations = int(input("Enter the number of simulations to run (K): "))
        if num_simulations <= 0:
            print("Number of simulations must be positive!")
            return
    
    except ValueError:
        print("Please enter valid numbers!")
        return
    
    print(f"\nCalculating probabilities for {num_dice} dice with {num_sides} sides each...")
    print(f"Running {num_simulations} simulations...")
    
    # Calculate probability distribution
    probabilities = calculate_probability_distribution(num_dice, num_sides, num_simulations)
    
    # Display results
    display_probabilities(probabilities)
    
    # Show expected range
    min_sum = num_dice  # All 1's
    max_sum = num_dice * num_sides  # All maximum values
    print(f"\nPossible sums range from {min_sum} to {max_sum}")
    
    # Ask if user wants to run again
    again = input("\nWould you like to run another calculation? (y/n): ")
    if again.lower() == 'y':
        main()
    else:
        print("\nThank you for using the Dice Probability Calculator!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
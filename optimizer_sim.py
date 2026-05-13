import random

def gradient_descent_game():
    # 1. Scenario: Landing in the Fog
    # We want to reach the lowest point (Error = 0)
    print("--- ✈️ THE GRADIENT GLIDER: OPTIMIZER SIM ✈️ ---")
    print("Mission: Find the lowest point in the valley (Global Minimum).")
    print("Goal: Adjust your position based on the slope to minimize Error.")

    # 2. Starting State
    current_pos = random.randint(-10, 10)
    target_pos = 0 # The bottom of the valley
    iterations = 5
    
    # 3. Hyperparameter: Learning Rate (Alpha)
    print("\n--- STEP 1: SET THE LEARNING RATE (α) ---")
    print("How fast should the pilot react to the slope?")
    print("Small α (e.g. 0.1): Very cautious, might take forever.")
    print("Large α (e.g. 0.9): Aggressive, might overshoot the target.")
    
    try:
        learning_rate = float(input("Enter Learning Rate (0.1 - 1.0): "))
    except ValueError:
        learning_rate = 0.3

    # 4. The Optimization Loop (Gradient Descent)
    print(f"\n--- 🖥️ STARTING DESCENT FROM POSITION {current_pos}... ---")
    
    for i in range(1, iterations + 1):
        # Calculate Gradient (Slope of the function y = x^2)
        # Gradient is the derivative: 2x
        gradient = 2 * current_pos
        
        # Update Rule: New_Pos = Old_Pos - (Learning_Rate * Gradient)
        change = learning_rate * gradient
        current_pos = current_pos - change
        
        error = current_pos ** 2 # Mean Squared Error (MSE)
        
        print(f"Iteration {i}: Gradient={gradient:.2f} | Move={-change:.2f} | New Position={current_pos:.2f} | Error={error:.4f}")
        
        if error < 0.01:
            print("\n✨ TOUCHDOWN! You reached the global minimum.")
            break
    else:
        if error > 10:
            print("\n💥 CRASH! Your learning rate was too high and you overshot the valley.")
        else:
            print(f"\n☁️ STILL IN THE FOG: Final Error is {error:.4f}. You need more iterations!")

if __name__ == "__main__":
    gradient_descent_game()

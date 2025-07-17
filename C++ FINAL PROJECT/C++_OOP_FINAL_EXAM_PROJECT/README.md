# ATM Cash Machine Simulator

## Project Overview

This C++ program implements an ATM Cash Machine Simulator, The simulator allows users to manage denominations and withdraw money smoothly.

## Task Description

The assigned task was to create a cash dispensing system that:
- Manages different currency denominations
- Implements two withdrawal algorithms (Greedy and Optimal)
- Provides a menu-driven interface for user interaction
- Handles denomination addition/removal dynamically

## How the Task Was Completed

### 1. **Object-Oriented Design**
- Used inheritance with an abstract base class `CashMachine`
- Implemented two derived classes: `GreedyDispenser` and `OptimalDispenser`
- Employed polymorphism for different dispensing strategies

### 2. **Data Structure Design**
- Created a `Denomination` struct to hold value and count
- Used dynamic memory allocation for flexible denomination management

### 3. **Algorithm Implementation**
- **Greedy Strategy**: Always uses the largest denomination first
- **Optimal Strategy**: Uses dynamic programming to find minimum number of notes

## Annotated Code Explanation

### Core Data Structures

```cpp
struct Denomination {
    int value;      // Face value of the denomination (e.g., 100, 50, 20)
    int* count;     // Pointer to count - allows shared state between objects
};
```

### Base Class - CashMachine

```cpp
class CashMachine {
protected:
    Denomination* denoms;   // Array of available denominations
    int size;              // Number of different denominations

public:
    // Constructor takes shared denominations array
    CashMachine(Denomination* sharedDenoms, int sharedSize) {
        denoms = sharedDenoms;  // Share reference, don't copy
        size = sharedSize;
    }

    // Pure virtual function - must be implemented by derived classes
    virtual bool withdraw(int amount) = 0;

    // Display all available denominations and their counts
    void showDenominations() {
        cout << "Available denominations:\n";
        for (int i = 0; i < size; ++i) {
            cout << denoms[i].value << " x " << *denoms[i].count << "\n";
        }
    }
};
```

### Greedy Algorithm Implementation

```cpp
class GreedyDispenser : public CashMachine {
public:
    GreedyDispenser(Denomination* denoms, int size) : CashMachine(denoms, size) {}

    bool withdraw(int amount) {
        cout << "Using Greedy Strategy:\n";
        int* used = new int[size];           // Track denominations used
        for (int i = 0; i < size; ++i) used[i] = 0;  // Initialize to zero

        // Greedy approach: use largest denominations first
        for (int i = 0; i < size; ++i) {
            while (amount >= denoms[i].value && *denoms[i].count > 0) {
                amount -= denoms[i].value;    // Reduce remaining amount
                (*denoms[i].count)--;         // Decrease available count
                used[i]++;                    // Track usage
            }
        }

        // Check if exact amount could be dispensed
        if (amount > 0) {
            cout << "Cannot dispense the exact amount.\n";
            // Rollback changes if unsuccessful
            for (int i = 0; i < size; ++i) {
                *denoms[i].count += used[i];
            }
            delete[] used;
            return false;
        }

        // Display dispensed denominations
        for (int i = 0; i < size; ++i) {
            if (used[i] > 0) {
                cout << denoms[i].value << " x " << used[i] << "\n";
            }
        }

        delete[] used;
        return true;
    }
};
```

### Optimal Algorithm Implementation

```cpp
class OptimalDispenser : public CashMachine {
public:
    OptimalDispenser(Denomination* denoms, int size) : CashMachine(denoms, size) {}

    bool withdraw(int amount) {
        cout << "Using Optimal Strategy:\n";

        const int INF = 1e9;                    // Infinity value for DP
        int* dp = new int[amount + 1];          // DP array: min notes needed
        int** used = new int*[amount + 1];     // Track which denominations used

        // Initialize DP arrays
        for (int i = 0; i <= amount; ++i) {
            dp[i] = INF;                        // Initially impossible
            used[i] = new int[size];
            for (int j = 0; j < size; ++j)
                used[i][j] = 0;                 // No denominations used initially
        }

        dp[0] = 0;  // Base case: 0 amount needs 0 notes

        // Dynamic Programming: for each amount and each denomination
        for (int i = 0; i <= amount; ++i) {
            for (int j = 0; j < size; ++j) {
                int val = denoms[j].value;
                int max_use = *denoms[j].count;

                // If we can use this denomination and it improves the solution
                if (i + val <= amount && used[i][j] < max_use && dp[i] + 1 < dp[i + val]) {
                    // Copy current state to new amount
                    for (int k = 0; k < size; ++k)
                        used[i + val][k] = used[i][k];
                    used[i + val][j]++;         // Use one more of this denomination
                    dp[i + val] = dp[i] + 1;    // One more note total
                }
            }
        }

        // Check if solution exists
        if (dp[amount] == INF) {
            cout << "Cannot dispense the exact amount optimally.\n";
            // Clean up memory
            for (int i = 0; i <= amount; ++i)
                delete[] used[i];
            delete[] used;
            delete[] dp;
            return false;
        }

        // Dispense the optimal solution
        for (int j = 0; j < size; ++j) {
            if (used[amount][j] > 0) {
                cout << denoms[j].value << " x " << used[amount][j] << "\n";
                *denoms[j].count -= used[amount][j];  // Update available count
            }
        }

        // Clean up memory
        for (int i = 0; i <= amount; ++i)
            delete[] used[i];
        delete[] used;
        delete[] dp;

        return true;
    }
};
```

### Main Function - Dynamic Memory Management

```cpp
int main() {
    Denomination* denoms = NULL;    // Dynamic array of denominations
    int size = 0;                   // Current number of denominations
    CashMachine* machines[2];       // Array to hold both dispenser types
    int choice;

    while (true) {
        // Create fresh instances sharing the same denomination data
        machines[0] = new GreedyDispenser(denoms, size);
        machines[1] = new OptimalDispenser(denoms, size);

        menu();
        cin >> choice;

        if (choice == 6) break;     // Exit condition

        switch (choice) {
            case 1: // Add Denominations
                // Dynamic array expansion logic
                cout << "Enter how many different denominations you want to add: ";
                int num;
                cin >> num;
                for (int n = 0; n < num; ++n) {
                    // Create new larger array
                    Denomination* newDenoms = new Denomination[size + 1];
                    // Copy existing data
                    for (int i = 0; i < size; ++i) {
                        newDenoms[i] = denoms[i];
                    }
                    // Add new denomination
                    cout << "Enter denomination value: ";
                    cin >> value;
                    cout << "Enter count for " << value << ": ";
                    cin >> count;
                    newDenoms[size].value = value;
                    newDenoms[size].count = new int(count);  // Allocate count on heap
                    // Replace old array
                    delete[] denoms;
                    denoms = newDenoms;
                    size++;
                }
                break;

            case 2: // Remove Denomination
                // Find and remove denomination, resize array
                cout << "Enter denomination value to remove: ";
                cin >> value;
                {
                    int index = -1;
                    // Find denomination to remove
                    for (int i = 0; i < size; ++i) {
                        if (denoms[i].value == value) {
                            index = i;
                            break;
                        }
                    }
                    if (index != -1) {
                        // Create smaller array
                        Denomination* newDenoms = new Denomination[size - 1];
                        for (int i = 0, j = 0; i < size; ++i) {
                            if (i == index) {
                                delete denoms[i].count;  // Free the count memory
                                continue;
                            }
                            newDenoms[j++] = denoms[i];
                        }
                        delete[] denoms;
                        denoms = newDenoms;
                        size--;
                    }
                }
                break;

            case 3: // Show Denominations
                machines[0]->showDenominations();
                break;

            case 4: // Withdraw using Greedy
                cout << "Enter amount to withdraw (Greedy): ";
                cin >> amount;
                machines[0]->withdraw(amount);
                break;

            case 5: // Withdraw using Optimal
                cout << "Enter amount to withdraw (Optimal): ";
                cin >> amount;
                machines[1]->withdraw(amount);
                break;
        }

        // Clean up instances after each operation
        delete machines[0];
        delete machines[1];
    }

    // Final cleanup: free all denomination counts and array
    for (int i = 0; i < size; ++i) {
        delete denoms[i].count;
    }
    delete[] denoms;

    cout << "Exited ATM Simulator.\n";
    return 0;
}
```

## Key Features

### 1. **Memory Management**
- Dynamic array resizing for denominations
- Proper cleanup to prevent memory leaks
- Shared state between dispenser objects

### 2. **Algorithm Comparison**
- **Greedy**: Fast, simple, but may not always find optimal solution
- **Optimal**: Uses dynamic programming, guarantees minimum notes but more complex

### 3. **Error Handling**
- Validates if exact amount can be dispensed
- Rollback mechanism for failed transactions

## Compilation and Execution

```bash
g++ -o atm_simulator atm_simulator.cpp
./atm_simulator
```

## Sample Program Flow

1. **Add Denominations**: Add currency notes (e.g., 100, 50, 20, 10)
2. **View Available Cash**: Check current inventory
3. **Withdraw Money**: Choose between Greedy or Optimal strategy
4. **Compare Results**: See difference in note distribution between algorithms

## Algorithm Complexity

- **Greedy Algorithm**: O(n) where n is number of denominations
- **Optimal Algorithm**: O(amount × n) using dynamic programming

## Memory Complexity

- **Greedy**: O(n) for tracking used denominations
- **Optimal**: O(amount × n) for DP table storage

---

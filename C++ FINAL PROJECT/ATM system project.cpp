#include <iostream>
using namespace std;

struct Denomination {
    int value;
    int* count;
};

class CashMachine {
protected:
    Denomination* denoms;
    int size;

public:
    CashMachine(Denomination* sharedDenoms, int sharedSize) {
        denoms = sharedDenoms;
        size = sharedSize;
    }

    virtual bool withdraw(int amount) = 0;

    void showDenominations() {
        cout << "Available denominations:\n";
        for (int i = 0; i < size; ++i) {
            cout << denoms[i].value << " x " << *denoms[i].count << "\n";
        }
    }
};

class GreedyDispenser : public CashMachine {
public:
    GreedyDispenser(Denomination* denoms, int size) : CashMachine(denoms, size) {}

    bool withdraw(int amount) {
        cout << "Using Greedy Strategy:\n";
        int* used = new int[size];
        for (int i = 0; i < size; ++i) used[i] = 0;

        for (int i = 0; i < size; ++i) {
            while (amount >= denoms[i].value && *denoms[i].count > 0) {
                amount -= denoms[i].value;
                (*denoms[i].count)--;
                used[i]++;
            }
        }

        if (amount > 0) {
            cout << "Cannot dispense the exact amount.\n";
            for (int i = 0; i < size; ++i) {
                *denoms[i].count += used[i];
            }
            delete[] used;
            return false;
        }

        for (int i = 0; i < size; ++i) {
            if (used[i] > 0) {
                cout << denoms[i].value << " x " << used[i] << "\n";
            }
        }

        delete[] used;
        return true;
    }
};

class OptimalDispenser : public CashMachine {
public:
    OptimalDispenser(Denomination* denoms, int size) : CashMachine(denoms, size) {}

    bool withdraw(int amount) {
        cout << "Using Optimal Strategy:\n";

        const int INF = 1e9;
        int* dp = new int[amount + 1];
        int** used = new int*[amount + 1];
        for (int i = 0; i <= amount; ++i) {
            dp[i] = INF;
            used[i] = new int[size];
            for (int j = 0; j < size; ++j)
                used[i][j] = 0;
        }

        dp[0] = 0;

        for (int i = 0; i <= amount; ++i) {
            for (int j = 0; j < size; ++j) {
                int val = denoms[j].value;
                int max_use = *denoms[j].count;

                if (i + val <= amount && used[i][j] < max_use && dp[i] + 1 < dp[i + val]) {
                    for (int k = 0; k < size; ++k)
                        used[i + val][k] = used[i][k];
                    used[i + val][j]++;
                    dp[i + val] = dp[i] + 1;
                }
            }
        }

        if (dp[amount] == INF) {
            cout << "Cannot dispense the exact amount optimally.\n";
            for (int i = 0; i <= amount; ++i)
                delete[] used[i];
            delete[] used;
            delete[] dp;
            return false;
        }

        for (int j = 0; j < size; ++j) {
            if (used[amount][j] > 0) {
                cout << denoms[j].value << " x " << used[amount][j] << "\n";
                *denoms[j].count -= used[amount][j];
            }
        }

        for (int i = 0; i <= amount; ++i)
            delete[] used[i];
        delete[] used;
        delete[] dp;

        return true;
    }
};

void menu() {
    cout << "\n--- ATM CASH MACHINE SIMULATOR ---\n";
    cout << "1. Add Denomination(s)\n";
    cout << "2. Remove Denomination\n";
    cout << "3. Show Denominations\n";
    cout << "4. Withdraw (Greedy)\n";
    cout << "5. Withdraw (Optimal)\n";
    cout << "6. Exit\n";
    cout << "Choose an option: ";
}

int main() {
    Denomination* denoms = NULL;
    int size = 0;
    CashMachine* machines[2];
    int choice;

    while (true) {
        machines[0] = new GreedyDispenser(denoms, size);
        machines[1] = new OptimalDispenser(denoms, size);

        menu();
        cin >> choice;

        if (choice == 6) break;

        int value, count, amount;

        switch (choice) {
            case 1:
                cout << "Enter how many different denominations you want to add: ";
                int num;
                cin >> num;
                for (int n = 0; n < num; ++n) {
                    cout << "Enter denomination value: ";
                    cin >> value;
                    cout << "Enter count for " << value << ": ";
                    cin >> count;

                    Denomination* newDenoms = new Denomination[size + 1];
                    for (int i = 0; i < size; ++i) {
                        newDenoms[i] = denoms[i];
                    }
                    newDenoms[size].value = value;
                    newDenoms[size].count = new int(count);
                    delete[] denoms;
                    denoms = newDenoms;
                    size++;
                }
                break;

            case 2:
                cout << "Enter denomination value to remove: ";
                cin >> value;
                {
                    int index = -1;
                    for (int i = 0; i < size; ++i) {
                        if (denoms[i].value == value) {
                            index = i;
                            break;
                        }
                    }
                    if (index != -1) {
                        Denomination* newDenoms = new Denomination[size - 1];
                        for (int i = 0, j = 0; i < size; ++i) {
                            if (i == index) {
                                delete denoms[i].count;
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

            case 3:
                machines[0]->showDenominations();
                break;

            case 4:
                cout << "Enter amount to withdraw (Greedy): ";
                cin >> amount;
                machines[0]->withdraw(amount);
                break;

            case 5:
                cout << "Enter amount to withdraw (Optimal): ";
                cin >> amount;
                machines[1]->withdraw(amount);
                break;

            default:
                cout << "Invalid option!\n";
        }

        delete machines[0];
        delete machines[1];
    }

    for (int i = 0; i < size; ++i) {
        delete denoms[i].count;
    }
    delete[] denoms;

    cout << "Exited ATM Simulator.\n";
    return 0;
}


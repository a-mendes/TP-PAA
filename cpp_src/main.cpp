#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <ctime>

using namespace std;

struct Item {
    int weight, value;
};

// Função para ler os itens do arquivo
vector<Item> readFile(const string &filename, int &capacity) {
    ifstream file(filename);
    vector<Item> items;
    if (!file) {
        cerr << "Erro ao abrir o arquivo!" << endl;
        exit(1);
    }

    file >> capacity; // Lê a capacidade da mochila
    int w, v;
    while (file >> w >> v) {
        items.push_back({w, v});
    }
    file.close();
    return items;
}

// 1. Algoritmo Backtracking
int knapsackBacktrack(vector<Item> &items, int index, int remainingWeight) {
    if (index == items.size() || remainingWeight == 0) return 0;
    if (items[index].weight > remainingWeight) return knapsackBacktrack(items, index + 1, remainingWeight);
    
    int include = items[index].value + knapsackBacktrack(items, index + 1, remainingWeight - items[index].weight);
    int exclude = knapsackBacktrack(items, index + 1, remainingWeight);
    
    return max(include, exclude);
}

// 2. Algoritmo Branch and Bound
struct Node {
    int level, value, weight, bound;
};

int bound(Node u, int n, int capacity, vector<Item> &items) {
    if (u.weight >= capacity) return 0;
    int profitBound = u.value;
    int j = u.level + 1, totalWeight = u.weight;
    
    while (j < n && totalWeight + items[j].weight <= capacity) {
        totalWeight += items[j].weight;
        profitBound += items[j].value;
        j++;
    }
    
    if (j < n)
        profitBound += (capacity - totalWeight) * (items[j].value / (double)items[j].weight);
    
    return profitBound;
}

int knapsackBranchBound(vector<Item> &items, int capacity) {
    sort(items.begin(), items.end(), [](Item a, Item b) {
        return (double)a.value / a.weight > (double)b.value / b.weight;
    });
    
    int maxProfit = 0;
    vector<Node> Q;
    Q.push_back({-1, 0, 0, 0});
    
    while (!Q.empty()) {
        Node u = Q.back(); Q.pop_back();
        
        if (u.level == (int)items.size() - 1) continue;
        
        Node v = {u.level + 1, u.value + items[u.level + 1].value, u.weight + items[u.level + 1].weight, 0};
        
        if (v.weight <= capacity && v.value > maxProfit)
            maxProfit = v.value;
        
        v.bound = bound(v, items.size(), capacity, items);
        if (v.bound > maxProfit)
            Q.push_back(v);
        
        v = {u.level + 1, u.value, u.weight, bound(u, items.size(), capacity, items)};
        if (v.bound > maxProfit)
            Q.push_back(v);
    }
    return maxProfit;
}

// 3. Algoritmo de Programação Dinâmica
int knapsackDP(vector<Item> &items, int capacity) {
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (items[i - 1].weight <= w)
                dp[i][w] = max(items[i - 1].value + dp[i - 1][w - items[i - 1].weight], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][capacity];
}

void executeAllInstaces(int experiment) {
    for (int i = 1; i <= 20; i++) {
        int capacity;
        vector<Item> items = readFile("../src/instances/experiment_" + to_string(experiment) + "/" + to_string(i) + ".txt", capacity);
        
        cout << "Instancia " << i << endl;
        double start = clock();
        cout << "Branch and Bound: " << knapsackBranchBound(items, capacity) << endl;
        cout << "Tempo: " << (clock() - start) / CLOCKS_PER_SEC << endl;
        cout << "Programacao Dinamica: " << knapsackDP(items, capacity) << endl;
        cout << "Tempo: " << (clock() - start) / CLOCKS_PER_SEC << endl;
        cout << "Backtracking: " << knapsackBacktrack(items, 0, capacity) << endl;
        cout << "Tempo: " << (clock() - start) / CLOCKS_PER_SEC << endl;
        cout << endl;
    }
}

int main() {
    executeAllInstaces(1);
    executeAllInstaces(2);

    return 0;
}
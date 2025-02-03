#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <vector>
using namespace std;
vector<int> visited;
vector<int> calc;
vector<int> array;
int n;
int result = INT_MIN;

void recursive(int idx) {
    // basis part
    if (idx == n) {
        int res = 0;
        for (int i = 0; i < n - 1; i++) {
            res += abs(array[calc[i]] - array[calc[i + 1]]);
        }
        result = max(result, res);
    }
    
    // inductive part
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = 1;
            calc.push_back(i);
            recursive(idx + 1);
            visited[i] = 0;
            calc.pop_back();
        }
    }
}

int main() {
    cin >> n;
    visited.resize(n, 0);
    array.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }
    recursive(0);
    cout << result;
}
#include <iostream>
#include <vector>
using namespace std;
int n;
vector<int> visited;
vector<int> result;

void recursive(int idx) {
    // basis part
    if (idx == n) {
        for (int i = 0; i < n; i++) {
            cout << result[i] << " ";
        }
        cout << "\n";
        return;
    }
    
    // inductive part
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = 1;
            result.push_back(i + 1);
            recursive(idx + 1);
            visited[i] = 0;
            result.pop_back();
        }
    }
       
}

int main() {
    cin >> n;
    visited.resize(n,0);
    recursive(0);
}
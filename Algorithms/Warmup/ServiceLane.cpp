#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
     int t, n, i, j, init, ti;
     cin>>n;
     cin>>t;
     string tmp;
     cin.ignore();
     getline(cin,tmp);
     vector<int> nums;
     stringstream ss(tmp);
     while(ss >> ti) {
        nums.push_back(ti);
     }
    for (int iter=0; iter<t;iter++){
        cin>>i;
        cin>>j;
        int min = nums[i];
        for (init = i;init <j+1; init++){
            if (nums[init]< min){
                min = nums[init];
            }
        }
        cout<<min<<endl;
    }
    return 0;
}

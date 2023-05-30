#include <iostream>
#include <vector>

using namespace std;

int najw_elem(vector<int>& v, int l, int p)
{
    if(l==p) return v[l];
    else {
        int s = (l+p)/2;
        int max_el1 = najw_elem(v,l,s);
        int max_el2 = najw_elem(v,s+1,p);
        int max_el = max_el1>max_el2 ? max_el1 : max_el2;
        return max_el;
    }
}

int main()
{
    vector<int> V = {5, 13, 7, 1, 9, 2, 8};
    cout << najw_elem(V, 0, V.size() - 1);
    return 0;
}

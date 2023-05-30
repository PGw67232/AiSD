#include <iostream>

using namespace std;

int suma_elem(int t[], int l, int n)
{
    if(l==n) return t[l];
    else {
        int s = (l+n)/2;
        int suma1 = suma_elem(t,l,s);
        int suma2 = suma_elem(t,s+1,n);
        return suma1 + suma2;
    }
}

int main()
{
    int n = 5;
    int tab[n] = {2,3,-5,6,-2};
    cout << suma_elem(tab,0,n-1);
    return 0;
}

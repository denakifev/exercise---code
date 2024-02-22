#include <iostream>
using namespace std;

const long MAXVAL = 10000000500;
const int MAXN = 300500;
long n, q;
long arr[MAXN];
long prep_s[MAXN];
long res[MAXN];

int main(){
    ios_base :: sync_with_stdio(0);
    cout.tie(0);
    cin >> n >> q;
    for (int i = 0; i < n ; ++i){
        cin >> arr[i];

    }
    prep_s[0] = 0;
    for (int i = 1; i < n + 1; ++i ){
        prep_s[i] = prep_s[i-1] + arr[i-1];
    
    }
    for (int i = 0; i < q; ++i){
        int l,r ;
        cin >> l >> r ;
        cout << prep_s[r] - prep_s[l-1] << "\n";
    }
    return 0;
}

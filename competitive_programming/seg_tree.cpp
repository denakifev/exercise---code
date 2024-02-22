#include <iostream>
#include <bits/stdc++.h>
#define ll long long
#define fori(i, start, end) \
    for (int i = start; i < end; ++i)
using namespace std;

struct seg_tree{
    vector <ll> tree;
    int size;
    
    void init(int n){
        size = 1;
        while (size < n) {
            size *= 2;
        }
        tree.assign(2 * size - 1, 0);

    }

    void set(int i, int v, int x, int lx, int rx){
        if (rx - lx == 1){
            tree[x] = v;
            return;
        }
        int mid = (lx + rx) / 2;
        if (i < mid){
            set(i, v, 2 * x + 1, lx, mid);
        } else{
            set(i, v, 2 * x + 2, mid, rx);
        }
        tree[x] = tree[2 * x + 1] + tree[2 * x + 2];

    }

    void set(int i, int v){
        set(i, v, 0, 0, size);
    }

    ll sum(int l, int r, int x, int lx, int rx){
        if (rx <= l || r <= lx){
            return 0;
        }
        if (l <= lx && rx <= r){
            return tree[x];
        }
        int mid = (lx + rx) / 2;
        ll sl = sum(l, r, 2 * x + 1, lx, mid);
        ll sr = sum(l, r, 2 * x + 2, mid, rx);
        return sl + sr;
    }
 

    ll sum(int l, int r){
        return sum(l, r, 0, 0, size);
    }
};

int main(){
    ios :: sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    seg_tree st;
    st.init(n);
    fori(i, 0, n){
        int x;
        cin >> x;
        st.set(i, x);
    }
    
    fori(op, 0, m){
        int des;
        cin >> des;
        if (des == 1){
            int i, v;
            cin >> i >> v;
            st.set(i, v);
        } else{
            int l, r;
            cin >> l >> r;
            cout << st.sum(l, r) << endl;
        }
    }
}





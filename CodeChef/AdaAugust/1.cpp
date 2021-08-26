#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // your code goes here
    int t;
    cin >> t;
    while (t--)
    {
        char inp;
        cin >> inp;
        if (inp == 'B' or inp == 'b')
        {
            cout << "BattleShip" << endl;
            continue;
        }
        if (inp == 'C' or inp == 'c')
        {
            cout << "Cruiser" << endl;
            continue;
        }
        if (inp == 'D' or inp == 'd')
        {
            cout << "Destroyer" << endl;
            continue;
        }
        if (inp == 'F' or inp == 'f')
        {
            cout << "Frigate" << endl;
            continue;
        }
    }
    return 0;
}

/*
ID: jessica41
PROG: ride
LANG: C++11
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    ofstream fout ("ride.out");
    ifstream fin ("ride.in");
    string comet_name, group_name;
    int comet_prod = 1;
    int group_prod = 1;
    fin >> comet_name >> group_name;
    //cin >> comet_name >> group_name;
    cout << "comet_name: " << comet_name << endl;
    cout << "group_name: " << group_name << endl;
    string outcome;
    transform(comet_name.begin(), comet_name.end(), comet_name.begin(), ::tolower);
    transform(group_name.begin(), group_name.end(), group_name.begin(), ::tolower);
    for (int i = 0; i < group_name.size(); ++i) {
        group_prod *= int(group_name[i])%96;
    }
    for (int i = 0; i < comet_name.size(); ++i) {
        comet_prod *= int(comet_name[i])%96;
    }
    cout << "comet_prod: " << comet_prod << endl;
    cout << "group_prod: " << group_prod << endl;
    if (group_prod % 47 == comet_prod % 47) {
        outcome = "GO";
    }
    else {
        outcome = "STAY";
    }
    fout << outcome << endl;
    cout << outcome << endl;
    return 0;
}


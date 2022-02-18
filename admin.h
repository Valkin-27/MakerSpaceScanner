//
// Created by marco on 2/17/22.
//

#ifndef MAKERSPACESCANNER_ADMIN_H
#define MAKERSPACESCANNER_ADMIN_H

#include "string"
using namespace std;

class admin{
    string name;
    string CWID;
    string phoneNumber;
    int prints;
    int aborts;
public:
    admin();
    admin(string name, string phoneNumber, string CWID);
};

#endif //MAKERSPACESCANNER_ADMIN_H
//
// Created by marco on 2/17/22.
//

#ifndef MAKERSPACESCANNER_STUDENT_H
#define MAKERSPACESCANNER_STUDENT_H

#include <string>
using namespace std;
class student {
    string name;
    string phoneNumber;
    string CWID;
    int prints;
    int aborts;
    string status;
public:
    student();
    student(string name, string phoneNumber, string CWID);
    string getStatus();
    void updateStatus();
};

#endif //MAKERSPACESCANNER_STUDENT_H

//
// Created by marco on 2/17/22.
//

//the following are UBUNTU/LINUX, and MacOS ONLY terminal color codes.
#define RESET   "\033[0m"
#define BLACK   "\033[30m"      /* Black */
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */

#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

#include "student.h"
#include "admin.h"
#include "splash.h"

#pragma clang diagnostic push
#pragma ide diagnostic ignored "EndlessLoop"

ifstream fileIO;

int main(){
    char usrChoice = '0';

    splash welcome;
    welcome.welcome(); // prints the welcome splash screen

    // ***************************************************
    //              Initializing Software
    // ***************************************************
    cout << BLUE << "Reading Students \r\n\n";
    fileIO.open("files\\students.csv");

    // make sure file opened
    if(fileIO.fail()){
        cout << RED << "files\\students.csv could not be opened." << endl;
        return -1;
    }

    // if file opens successfully, then start importing data.


    // once file content has been read and imported, close the file
    cout << GREEN << "Students read" << endl;
    fileIO.close();

    // ***************************************************
    //                  Welcome Screen
    // ***************************************************
    printf("Colorado School of Mines Blaster Card Scanner\r\n");
    printf("Written in Spring of 2022");
    printf("\r\n");


    // ***************************************************
    //                      Main Loop
    // ***************************************************
    for(;;){

        printf("---------------------------\r\n");
        printf("\r\n");
        printf("?:  Help Menu\r\n");
        printf("s:  Start a 3D Print\r\n");
        printf("a:  Abort a 3D print\r\n");
        printf("A:  Admin Commands\r\n");
        printf("");

        // setup switch statement for chosing an option for the system
        cout << ">>";
        cin >> usrChoice;

        switch(usrChoice){
            case '?':
                printf("s: anyone can select s to start a new 3D print, will prompt for:\n"
                       "\t- print time\n"
                       "\t- asked to complete the survey\r\n");
                printf("a: in order to abort a 3D print you will be asked,\n"
                       "\t- reason for aborting (failing, other\r\n");
                printf("A: view admin commands\r\n");
                break;

            case 'A':
                printf("---------------------------\r\n");
                printf("Welcome to the admin portal\r\n");
                printf("---------------------------\r\n");
                printf("Please choose one of the following options\r\n");
                printf("?:  Help\r\n");
                printf("Z:  Restart application\r\n");
                printf("U:  Unlock all 3D printers\r\n");
                printf("B:  Backup logs immediately\r\n");
                printf("A:  Add a new user to the system\r\n");
                printf("x:  exit menu, return to main menu\r\n\n");

                cout << ">>";
                cin >> usrChoice;

                switch(usrChoice){
                    case '?':
                        printf("Z:  Will safely reboot the application, saving logs, and restarting\r\n\n");
                        printf("U:  Will unlock every 3D printer for some reason\r\n\n");
                        printf("B:  Create a backup of current logs to file sharing service (Drive, Outlook, etc.)\r\n\n");
                        printf("A:  Add a new user to system, requires student to have blaster card on hand\r\n\n");
                        continue;

                    case 'Z':

                        continue;

                    case 'U':

                        continue;

                    case 'B':

                        continue;

                    case 'x':

                        break;

                    case 'A':

                        continue;

                    default:
                        printf("Invalid choice, please choose a valid option\r\n\n");
                        break;
                }

            case 's':

                break;

            case 'a':

                break;

            default:
                cout << "Selected option was not valid, please choose a valid option";
                break;
        }
    }

}
#pragma clang diagnostic pop
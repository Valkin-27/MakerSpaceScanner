cmake_minimum_required(VERSION 3.21)
project(MakerSpaceScanner)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(MakerSpaceScanner
        main.cpp
        student.cpp
        student.h
        admin.cpp
        admin.h
        splash.cpp
        splash.h
        init.cpp
        init.h)

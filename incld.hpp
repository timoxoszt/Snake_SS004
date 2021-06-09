#ifndef _incld_h_
#define _incld_h_

#include <iostream>
#include <windows.h>
#include <cstdlib>
#include <conio.h>
using namespace std;

struct Point{
    int x,y;
};

void gotoxy( int column, int line )
  {
  COORD coord;
  coord.X = column;
  coord.Y = line;
  SetConsoleCursorPosition(
    GetStdHandle( STD_OUTPUT_HANDLE ),
    coord
    );
  }

#endif
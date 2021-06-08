#include <incld.hpp>
#include <coord.hpp>
#include <classes.hpp>

int main()
{
    MIENGMOI m;
	CONRAN r;
    int Huong = 0;
    char t;
    while (1){
        if (kbhit()){
            t = getch();
            if (t=='a') Huong = 2;
            if (t=='w') Huong = 3;
            if (t=='d') Huong = 0;
            if (t=='s') Huong = 1;
        }
        system("cls");
		m.Ve();
        r.Ve();
        r.DiChuyen(Huong);
        Sleep(300);
    }

    return 0;
}
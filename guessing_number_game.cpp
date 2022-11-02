#include <iostream>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

bool winner=false;
int player_number;
int random_number;
int attempts=5;
int generate_random_number()
{ 
    srand (time(NULL));
    int random_number=rand()%100;
    return random_number;
}
int guess_number()
{ 
    int player_number;
    cout<<"guess a number between 1 and 100"<<endl;
    cin>>player_number;
    while (player_number<1 || player_number>100)
    { 
        cout<<"not valid number"<<endl;
        cin>>player_number; 
    }
    return player_number;
}
bool check_win(int player_number,int random_number)
{  
    if (player_number==random_number)
    { 
        cout<<"you win"<<endl;
        return true;
    }
    else if (player_number>random_number)
    { 
        cout<<"too high"<<endl;
        ::attempts=attempts-1;
        cout<<"you still have "<<::attempts<<"  attempts"<<endl;
        return false;
    }
    else if (player_number<random_number)
    { 
        cout<<"too low"<<endl;
        ::attempts=attempts-1;
        cout<<"attempts : "<<::attempts<<endl;
        return false;
    }
}
bool check_gamover(int random_number)
{ 
    if (::attempts==0)
    { 
        cout<<"you have no attempts left\n";
        cout<<"the number was "<<random_number<<endl;
    }
}
void play_Game()
{ 
    cout<<"welcome to the number guessing Game\n";
    random_number=generate_random_number();
    while (::attempts>0 && ::winner==false)
    { 
        player_number=guess_number();
        winner=check_win(player_number,random_number);
    }
    check_gamover(random_number);
}
int main()
{
    play_Game();   
    system("pause");
    return 0;
}
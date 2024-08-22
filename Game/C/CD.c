#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <stdbool.h>


void resetBoard(int board[3][3]);
void printBoard(int board[3][3]);
int checkFreeSpaces(int board[3][3]);
void playerMove();
void computerMove();
char checkWinner();
void printWinner(char);


int main(){
    int board[3][3];
    int run = true;
    resetBoard(board);
    while (run){
        printBoard(board);
    }
}


void resetBoard(int board[3][3]){
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            board[i][j] = ' ';
        }
    }
}


void printBoard(int board[3][3]){
    printf("+---+---+---+");
    for (int i = 0; i < 3; i++){
        printf("\n|");
        for (int j = 0; j < 3; j++){
            printf(" %c |", board[i][j]);
        }
        printf("\n+---+---+---+");
    }
    printf("\n"); // To jump to next line after done printing.
}


int checkFreeSpaces(int board[3][3]){
    int count = 0;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (board[i][j] == ' '){
                count++;
            }
        }
    }
    return count;
}


void playerMove(){

}


void computerMove(){

}


char checkWinner(){

}


void printWinner(char winner){

}
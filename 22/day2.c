#include <stdio.h>
#include <string.h>

void main()
{
    FILE* fp = fopen("day2.txt", "r");
    char line[6];
    int score_1 = 0;

    while( fgets(line, sizeof(line), fp) )
    {
        printf("Opponent: \"%c\"\nYourself: \"%c\"\n", line[0], line[2]);

        if( line[2] == 'X' )
        {
            score_1 += 1;
            if( line[0] == 'B' )
            {
                printf("Loss: 1\n");
            }
            else if( line[0] == 'A' )
            {
                printf("Draw: 4\n");
                score_1 += 3;
            }
            else
            {
                printf("Win: 7\n");
                score_1 += 6;
            }
        }
        else if( line[2] == 'Y')
        {
            score_1 += 2;
            if( line[0] == 'C' )
            {
                printf("Loss: 2\n");
            }
            else if( line[0] == 'B' )
            {
                printf("Draw: 5\n");
                score_1 += 3;
            }
            else
            {
                printf("Win: 8\n");
                score_1 += 6;
            }
        }
        else
        {
            score_1 += 3;
            if( line[0] == 'A' )
            {
                printf("Loss: 3\n");
            }
            else if( line[0] == 'C' )
            {
                printf("Draw: 6\n");
                score_1 += 3;
            }
            else
            {
                printf("Win: 9\n");
                score_1 += 6;
            }
        }
        printf("Running Total: %d\n\n", score_1);
    }

    printf("Solution 1: %d\n", score_1);
}
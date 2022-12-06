#include <stdio.h>
#include <string.h>

void main()
{
    FILE* fp = fopen("day2.txt", "r");
    char line[6];
    int score_1 = 0;
    int score_2 = 0;

    while( fgets(line, sizeof(line), fp) )
    {
        if( line[2] == 'X' )
        {
            score_1 += 1;

            if( line[0] == 'B' )
            {
                score_2 += 1;
            }
            else if( line[0] == 'A' )
            {
                score_1 += 3;
                score_2 += 3;
            }
            else
            {
                score_1 += 6;
                score_2 += 2;
            }
        }
        else if( line[2] == 'Y')
        {
            score_1 += 2;
            score_2 += 3;

            if( line[0] == 'C' )
            {
                score_2 += 3;
            }
            else if( line[0] == 'B' )
            {
                score_1 += 3;
                score_2 += 2;
            }
            else
            {
                score_1 += 6;
                score_2 += 1;
            }
        }
        else
        {
            score_1 += 3;
            score_2 += 6;

            if( line[0] == 'A' )
            {
                score_2 += 2;
            }
            else if( line[0] == 'C' )
            {
                score_1 += 3;
                score_2 += 1;
            }
            else
            {
                score_1 += 6;
                score_2 += 3;
            }
        }
    }

    printf("Solution 1: %d\nSoltuion 2: %d\n", score_1, score_2);
}
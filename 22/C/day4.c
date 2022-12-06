#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int answer(FILE* fp, int solution);

void main()
{
    FILE* fp = fopen("day4.txt", "r");
    printf("Solution 1: %d\n", answer(fp, 1));
    fclose(fp);

    fp = fopen("day4.txt", "r");
    printf("Solution 2: %d\n", answer(fp, 2));
    fclose(fp);
}

int answer(FILE* fp, int solution)
{
    char line[50];
    int contain_sum = 0;
    int token1;
    int token2;
    int token3;
    int token4;

    while( fgets(line, sizeof(line), fp) )
    {
        token1 = atoi(strtok(line, "-"));
        token2 = atoi(strtok(NULL, ","));
        token3 = atoi(strtok(NULL, "-"));
        token4 = atoi(strtok(NULL, "\n"));

        if( (solution == 1) && ((token1 <= token3 && token2 >= token4) || (token3 <= token1 && token4 >= token2)) )
        {
            contain_sum += 1;
        }
        else if( (solution == 2) && ((token1 >= token3 && token1 <= token4) || (token2 >= token3 && token2 <= token4) || (token3 >= token1 && token3 <= token2) || (token4 >= token1 && token4 <= token2)) )
        {
            contain_sum += 1;
        }

    }

    return contain_sum;
}
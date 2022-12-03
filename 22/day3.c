#include <stdio.h>
#include <string.h>
#include <ctype.h>

void string_split(char* s, int index, char* first, char* second);
int solution_1(FILE* fp);

void main()
{
    FILE* fp = fopen("day3.txt", "r");
    printf("Solution 1: %d\n", solution_1(fp));
}

void string_split(char* s, int index, char* first, char* second)
{
    int length = strlen(s);
    for (int i = 0; i < index; i++)
    {
        first[i] = s[i];
    }
    first[index] = '\0';
    for (int i = index; i <= length; i++)
    {
        if( s[i] != '\n' )
        {
            second[i - index] = s[i];
        }
        else
        {
            second[i - index] = '\0';
        }
    }
}

int solution_1(FILE* fp)
{
    char line[50];
    int priority;
    int priority_sum = 0;
    while( fgets(line, sizeof(line), fp) )
    {
        char first[100], second[100];
        int halflen = strlen(line)/2;
        char item;
        string_split(line, halflen, first, second);
        for( int i = 0; i < strlen(first); i++)
        {
            for( int j = 0; j < strlen(second); j++ )
            {
                if( first[i] == second[j])
                {
                    item = first[i];
                }
            }
        }
        if( isupper(item) )
        {
            priority = ((int)item - 38);
        }
        else
        {
            priority = ((int)item - 96);
        }
        priority_sum += priority;
    }
    return priority_sum;
}
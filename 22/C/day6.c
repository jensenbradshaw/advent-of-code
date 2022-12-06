#include <stdio.h>
#include <string.h>

int solution(FILE* fp);

void main()
{
    FILE* fp = fopen("day6.txt", "r");
    printf("Solution 1: %d\n", solution(fp));
    fclose(fp);

    //fp = fopen("day6.txt", "r");
    //printf("Solution 2: %d\n", solution(fp, 14));
    //fclose(fp);
}

int solution(FILE* fp)
{
    char line[5000];
    char marker[4];

    fgets(line, sizeof(line), fp);

    for( int i = 0; i < strlen(line); i++ )
    {
        if( strlen(marker) == 4 )
        {
            int unique = 1;
            for( int j = 0; j < 4; j++ )
            {
                for( int k = j + 1; k < 4; k++ )
                {
                    if( marker[j] != marker[k] )
                    {
                        unique = 0;
                    }
                }
            }
            if( unique == 1 )
            {
                return i;
            }
            for ( int j = 0; j < 3; j++ )
            {
                marker[j] = marker[j+1];
            }
        }
        marker[3] = line[i];
    }
}
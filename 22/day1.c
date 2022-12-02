#include <stdio.h>

void main()
{
    FILE* fp = fopen("day1.txt", "r");

    int current_calories = 0;
    int top[] = {0, 0, 0};
    char line[10];
    
    while(fgets(line, 10, fp))
    {
        if( line[0] == '\n' || line[0] == '\r' )
        {
            if( top[0] < current_calories )
            {
                top[2] = top[1];
                top[1] = top[0];
                top[0] = current_calories;
            }
            else if( top[1] < current_calories )
            {
                top[2] = top[1];
                top[1] = current_calories;
            }
            else if( top[2] < current_calories )
            {
                top[2] = current_calories;
            }
            current_calories = 0;
        }
        else
        {
            current_calories += atoi(line);
        }
    }

    printf("Part 1 Solution: %d\n", top[0]);
    printf("Part 2 Solution: %d\n", top[0] + top[1] + top[2]);

    fclose(fp);

}
#include <stdio.h>

void main()
{
    FILE* fp = fopen("day1.txt", "r");

    int current_calories = 0;
    int highest_calories = 0;
    int second_highest_calories = 0;
    int third_highest_calories = 0;

    char line[10];
    while(fgets(line, 10, fp))
    {
        if( line[0] == '\n' )
        {
            if( highest_calories < current_calories )
            {
                third_highest_calories = second_highest_calories;
                second_highest_calories = highest_calories;
                highest_calories = current_calories;
            }
            else if( second_highest_calories < current_calories )
            {
                third_highest_calories = second_highest_calories;
                second_highest_calories = current_calories;
            }
            else if( third_highest_calories < current_calories )
            {
                third_highest_calories = current_calories;
            }
            current_calories = 0;
        }
        else
        {
            current_calories += atoi(line);
        }
    }

    printf("Part 1 Solution: %d\n", highest_calories);
    printf("Part 2 Solution: %d\n", highest_calories + second_highest_calories + third_highest_calories);

    fclose(fp);

}
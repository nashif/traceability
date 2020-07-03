
#include <stdio.h>
#include "mylib.h"

int say_hello(int count)
{
        int i;
        for (i = 1; i <= count; ++i) {
                printf("Hello %d\n", i);
        }
        return 0;
}

int say_goodbye(int count)
{
        int i;
        for (i = count; i > 0; --i) {
                printf("Goodbye %d\n", i);
        }
        return 0;
}
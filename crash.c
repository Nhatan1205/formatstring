#include <stdio.h>

void fmtstr()
{
    char input[100];
    int var = 0x11223344;

    /* print out information for experiment purpose */
    printf("Target address: %x\n", (unsigned) &var);
    printf("Data at target address: 0x%x\n", var);

    printf("Please enter a string: ");
    fgets(input, sizeof(input), stdin);

    printf(input);  // The vulnerable place

    printf("Data at target address: 0x%x\n", var);
}

int main()
{
    fmtstr();
    return 0;
}

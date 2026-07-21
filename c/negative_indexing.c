/**
 * negative_indexing.c
 * ===================
 * WHAT IS THIS?
 * A demonstration of legal negative array indexing in standard C.
 * While high-level languages like Python support negative indexing relative
 * to the end of an array (e.g., arr[-1]), C supports negative indexing
 * relative to ANY pointer offset in memory.
 *
 * HOW DOES IT WORK?
 * In C, array subscript notation `a[i]` is purely syntactic sugar for pointer
 * arithmetic:
 *
 *     a[i]  <===>  *(a + i)
 *
 * Because addition is commutative, `a[i]` is identical to `*(a + i)`.
 * If `i` is negative (e.g., -1), the expression becomes:
 *
 *     ptr[-1]  <===>  *(ptr + (-1))  <===>  *(ptr - 1)
 *
 * As long as `(ptr - 1)` points to a valid memory address previously allocated
 * within the bounds of your array, reading or writing to `ptr[-1]` is 100%
 * valid, defined C behavior!
 */

#include <stdio.h>

int main() {
    // Declare a contiguous array of 5 integers in memory
    int numbers[5] = {10, 20, 30, 40, 50};

    // =========================================================================
    // MEMORY LAYOUT DIAGRAM
    // =========================================================================
    // Address Offset:  -2 * sizeof(int)   -1 * sizeof(int)    +0            +1            +2
    // Array Index:         numbers[0]        numbers[1]    numbers[2]    numbers[3]    numbers[4]
    // Values:             [    10    ]      [    20    ]  [    30    ]  [    40    ]  [    50    ]
    //                                                      ^
    //                                                      |
    //                                             ptr = &numbers[2]
    // =========================================================================

    // Create a pointer pointing directly to element index 2 (value 30)
    int *ptr = &numbers[2];

    printf("====================================================================\n");
    printf("                  LEGAL NEGATIVE INDEXING IN C                      \n");
    printf("====================================================================\n");
    printf("Base Pointer Address (ptr points to numbers[2]): %p\n", (void *)ptr);
    printf("Value at *ptr (ptr[0]):                          %d\n\n", ptr[0]);

    // Reading backward using negative indices
    printf("--- READING BACKWARD ---\n");
    printf("ptr[-1] (Equivalent to *(ptr - 1) -> numbers[1]): %d\n", ptr[-1]); // 20
    printf("ptr[-2] (Equivalent to *(ptr - 2) -> numbers[0]): %d\n", ptr[-2]); // 10

    // Reading forward using positive indices from the offset pointer
    printf("\n--- READING FORWARD ---\n");
    printf("ptr[1]  (Equivalent to *(ptr + 1) -> numbers[3]): %d\n", ptr[1]);  // 40
    printf("ptr[2]  (Equivalent to *(ptr + 2) -> numbers[4]): %d\n", ptr[2]);  // 50

    // =========================================================================
    // WRITING VIA NEGATIVE INDEXING
    // =========================================================================
    // Negative indices can also be lvalues (used for writing/modifying memory)
    ptr[-1] = 999; // Modifies numbers[1] directly through ptr

    printf("\n--- AFTER MODIFYING ptr[-1] = 999 ---\n");
    printf("numbers[1] value in original array:               %d\n", numbers[1]); // 999

    // =========================================================================
    // THE ULTIMATE CURSED SYNTAX: (-1)[ptr]
    // =========================================================================
    // Since `ptr[-1]` is `*(ptr - 1)`, commutative law means `(-1)[ptr]`
    // expands to `*(-1 + ptr)`, which is identical!
    printf("\n--- CURSED SYNTAX: (-1)[ptr] ---\n");
    printf("(-1)[ptr] evaluates to:                          %d\n", (-1)[ptr]); // 999

    printf("====================================================================\n");

    return 0;
}

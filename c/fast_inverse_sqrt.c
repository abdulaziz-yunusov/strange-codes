/**
 * fast_inverse_sqrt.c
 * ===================
 * WHAT IS THIS?
 * The famous Fast Inverse Square Root algorithm (1/sqrt(x)), popularized by
 * John Carmack and ID Software in the 1999 game source code for Quake III Arena.
 *
 * WHY WAS IT NEEDED?
 * In 3D graphics engines, calculating light reflections and vector normalization
 * requires computing 1 / sqrt(x) millions of times per second. In 1999, standard
 * floating-point division and square roots were extremely slow on CPUs.
 *
 * HOW DOES THE MATH WORK?
 * 1. Logarithmic Approximation via IEEE 754:
 *    An IEEE 754 32-bit floating-point number represents a value as:
 *       x = (1 + M) * 2^E
 *    In memory, the bit pattern contains exponent 'E' and mantissa 'M'.
 *    Taking log2(x) gives: log2(x) = E + log2(1 + M) ≈ E + M.
 *    Because of this structure, treating the bit pattern of a float as an
 *    INTEGER approximates log2(x) scaled by a large constant!
 *
 * 2. Solving y = x^(-1/2) in Log Space:
 *    log2(y) = -1/2 * log2(x)
 *    By converting the float bits to an integer, shifting right by 1 bit
 *    (dividing log2 by 2), and subtracting from a magic constant (0x5f3759df),
 *    we obtain an insanely accurate initial guess for x^(-1/2) in just 4 CPU cycles!
 *
 * 3. Newton-Raphson Refinement:
 *    A single iteration of the Newton-Raphson root-finding method boosts the
 *    accuracy of the approximation to within 0.1% error.
 */

#include <stdio.h>
#include <stdint.h>
#include <math.h>

float fast_inverse_sqrt(float number) {
    uint32_t i;
    float x2, y;
    const float threehalfs = 1.5F;

    // x2 store half the input value for the Newton-Raphson step
    x2 = number * 0.5F;
    y  = number;

    // =========================================================================
    // STEP 1: BIT-CAST FLOAT TO INTEGER
    // =========================================================================
    // We treat the raw 32-bit float memory layout directly as a 32-bit integer.
    // (Note: Modern C uses union or memcpy to comply with strict-aliasing rules)
    i = *(uint32_t *) &y;

    // =========================================================================
    // STEP 2: THE MAGIC BITWISE COMPUTATION
    // =========================================================================
    // 1. (i >> 1) : Bit-shifting right by 1 divides the exponent in log-space
    //               by 2, executing the square root step (x^(1/2)).
    // 2. 0x5f3759df - (i >> 1) : Subtraction flips the sign in log-space,
    //                            executing the reciprocal step (1 / x).
    // The constant 0x5f3759df is mathematically derived to minimize total
    // relative error across all IEEE 754 floating-point values.
    i = 0x5f3759df - (i >> 1);

    // =========================================================================
    // STEP 3: BIT-CAST INTEGER BACK TO FLOAT
    // =========================================================================
    // Reinterpret the modified bits back into a floating-point representation.
    y = *(float *) &i;

    // =========================================================================
    // STEP 4: NEWTON-RAPHSON ITERATION
    // =========================================================================
    // Formula: y_new = y * (1.5 - (x/2 * y * y))
    // Refinement step increases accuracy exponentially without slow division.
    // 1st iteration (reduces error to ~0.17%):
    y = y * (threehalfs - (x2 * y * y));

    // 2nd iteration (optional in original Quake code, omitted for speed):
    // y = y * (threehalfs - (x2 * y * y));

    return y;
}

int main() {
    float test_values[] = { 4.0f, 16.0f, 25.0f, 100.0f, 0.15625f };
    int num_tests = sizeof(test_values) / sizeof(test_values[0]);

    printf("====================================================================\n");
    printf("        FAST INVERSE SQUARE ROOT vs STANDARD C <math.h>             \n");
    printf("====================================================================\n");
    printf("%-12s | %-16s | %-16s | %-10s\n", "Input (x)", "Fast InvSqrt", "1.0 / sqrt(x)", "Error %");
    printf("--------------------------------------------------------------------\n");

    for (int i = 0; i < num_tests; i++) {
        float x = test_values[i];
        float fast_res = fast_inverse_sqrt(x);
        float std_res = 1.0f / sqrtf(x);
        float error_percent = fabsf((fast_res - std_res) / std_res) * 100.0f;

        printf("%-12.4f | %-16.6f | %-16.6f | %-10.4f%%\n",
               x, fast_res, std_res, error_percent);
    }

    printf("====================================================================\n");
    return 0;
}

/*
 C fundamental data types
*/

#include <stdbool.h>
#include <stdio.h>
#include <limits.h>
#include <float.h>

int main()
{
	printf("***** The size of fundamental data types *****\n\n");

	printf("               char: %2lu byte  min: %d  max: %d\n", sizeof(char), CHAR_MIN, CHAR_MAX);
	printf("        signed char: %2lu byte  min: %d  max: %d\n", sizeof(signed char), SCHAR_MIN, SCHAR_MAX);
	printf("      unsigned char: %2lu byte  max: %u\n\n", sizeof(unsigned char), UCHAR_MAX);

	printf("              short: %2lu bytes  min: %d  max: %d\n", sizeof(short), SHRT_MIN, SHRT_MAX);
	printf("                int: %2lu bytes  min: %d  max: %d\n", sizeof(int), INT_MIN, INT_MAX);
	printf("               long: %2lu bytes  min: %ld  max: %ld\n", sizeof(long), LONG_MIN, LONG_MAX);
	printf("          long long: %2lu bytes  min: %lld  max: %lld\n\n", sizeof(long long), LLONG_MIN, LLONG_MAX);

	printf("     unsigned short: %2lu bytes  max: %u\n", sizeof(unsigned short), USHRT_MAX);
	printf("           unsigned: %2lu bytes  max: %u\n", sizeof(unsigned), UINT_MAX); // unsigned int
	printf("      unsigned long: %2lu bytes  max: %lu\n", sizeof(unsigned long), ULONG_MAX);
	printf(" unsigned long long: %2lu bytes  max: %llu\n\n", sizeof(unsigned long long), ULLONG_MAX);

	printf("              float: %2lu bytes  min: %E  max: %E\n", sizeof(float), FLT_MIN, FLT_MAX);
	printf("             double: %2lu bytes  min: %E  max: %E\n", sizeof(double), DBL_MIN, DBL_MAX);
	printf("        long double: %2lu bytes  min: %LE  max: %LE\n\n", sizeof(long double), LDBL_MIN, LDBL_MAX);

	printf("               bool: %2lu byte  true: %d  false: %d\n", sizeof(bool), true, false);
}


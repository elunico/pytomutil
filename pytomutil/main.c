#include <stdlib.h>

long shmult(long a, long b) {
    if (b == 0) {
        return 0;
    }
    if (b == 1) {
        return a;
    }
    if (b % 2 == 0) {
        a <<= 1;
        return shmult(a, b >> 1);
    }
    if (b % 2 == 1) {
        a += a;
        return shmult(a, b - 1);
    }
    abort();
}
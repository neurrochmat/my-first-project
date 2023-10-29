#include <stdio.h>
#define PI 3.14

int main() {
    float radius, luas, keliling;
    //Masukkan jari-jari lingkaran
    printf("Masukan jari-jari Lingkaran: ");
    scanf("%f", &radius);
    //Hitung luas lingkaran menggunakan rumus: L = pi * r^2
    //Hitung keliling lingkaran menggunakan rumus: K = 2 * pi * r
    luas = PI * radius * radius;
    keliling = 2 * PI * radius;
    //Tampilkan luas dan keliling lingkaran
    printf("Luas Lingkaran = %.2f\n", luas);
    printf("Keliling Lingkaran = %.2f", keliling);

    return 0;
}

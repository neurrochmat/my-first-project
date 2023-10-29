#include <stdio.h>

int main() {
    float celsius, fahrenheit;
    // Langkah 2: Masukan nilai suhu dalam Celsius
    printf("Masukkan suhu dalam Celsius: ");
    scanf("%f", &celsius);
    // Langkah 3: Hitung suhu Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32;
    // Langkah 4: Tampilkan hasil
    printf("%.2f Celsius = %.2f Fahrenheit", celsius, fahrenheit);
    // Langkah 5: Selesai
    return 0;
}

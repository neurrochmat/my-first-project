/*
Nama    : Nur Rahmat Hidayat
NIM     : 3.34.23.0.19
Kelas   : IK-1A

Program input nilai
*/
#include<stdio.h>

int main() {
    int n, i;
    char nama[30][30];
    int nilai[30];
    char *nilai_huruf[30];

    printf("Masukan Jumlah Mahasiswa: ");
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        printf("Masukan Nama %d: ", i+1);
        scanf("%s", nama[i]);
        printf("Masukan Nilai %d: ", i+1);
        scanf("%d", &nilai[i]);
        if (nilai[i] >= 80 && nilai[i] <= 100) {
            nilai_huruf[i] = "A";
        } else if (nilai[i] >= 75 && nilai[i] < 80) {
            nilai_huruf[i] = "AB";
        } else if (nilai[i] >= 70 && nilai[i] < 75) {
            nilai_huruf[i] = "B";
        } else if (nilai[i] >= 66 && nilai[i] < 70) {
            nilai_huruf[i] = "BC";
        } else if (nilai[i] >= 60 && nilai[i] < 66) {
            nilai_huruf[i] = "C";
        } else if (nilai[i] >= 40 && nilai[i] < 60) {
            nilai_huruf[i] = "D";
        } else if (nilai[i] >= 1 && nilai[i] < 40) {
            nilai_huruf[i] = "E";
        }
    }
    printf("\n+----------------+-------------+-------------+\n");
    printf("| Nama Mahasiswa | Nilai Angka | Nilai Huruf |\n");
    printf("+----------------+-------------+-------------+\n");
    for(i = 0; i <n; i++) {
        printf("| %-14s | %-11d | %-11s |\n", nama[i], nilai[i], nilai_huruf[i]);
    }
    printf("+----------------+-------------+-------------+\n");

    return 0;
}

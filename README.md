# README

📌 **Kelompok A06**
| NRP         | Name                               |
|-------------|------------------------------------|
| 5025241019  | Jahhaza Assiqooyah Nurul Hidayah   |
| 5025241039  | Yasmina Fitri Azizah               |
| 5025241041  | Salwa Nadia Maharani               |
| 5025241042  | Naura Rossa Azalia                 |
| 5025241047  | Kinanti Ayu Caesandria             |
---

## Program Komputasi Numerik 

11. Diketahui f(x) = x3+ 6x2 - 19x - 84. Dimulai dari x0 = 5. Cari akar x dengan menggunakan metoda iterasi satu titik dengan cara memindahkan variabel x2 ke sebelah kiri [Lakukan iterasi hingga iterasi ke-5. Print semua iterasinya]

    Step:
    - Pindahkan variabel x2 ke kiri, maka didapatkan -6x2 = (x3 - 19x - 84)
    - Jadikan sebagai fungsi x, maka didapatkan x = (x3 - 19x - 84) / -6x
    - f(x) baru akan digunakan sebagai fungsi perhitungan untuk mencari akar x (iterasi 1 - 5)
    - Menghitung EA(_Error Approximation_) berdasarkan nilai akar x yang didapat pada setiap iterasinya

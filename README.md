# latihan_OOP
Nama : Doni Alvero <p>
Nim : 312410663 <p>
Kelas : TI.24.A.5 <P>
Jurusan : Teknik Informatika <P>

## Program Python

## clas_mahasiswa
![gambar3](https://github.com/user-attachments/assets/45a34131-9a4b-4b86-a55c-dae052829e2b)
## Penjelasan clas_mahasiswa
1. kelas mahasiswa
- Atribut:
  - nim: Nomor Induk Mahasiswa.
  - nama: Nama mahasiswa.
  - tugas: Nilai tugas mahasiswa.
  - uts: Nilai Ujian Tengah Semester.
  - uas: Nilai Ujian Akhir Semester.
  - akhir: Nilai akhir yang dihitung dari nilai tugas, uts, dan uas.
- Metode:
  - __init__: Konstruktor untuk menginisialisasi atribut-atribut mahasiswa dan menghitung nilai akhir.
  - calculate_final_grade: Metode untuk menghitung nilai akhir berdasarkan bobot nilai tugas (30%), uts (35%), dan uas (35%).
2. Kelas DataMahasiswa
- Atribut:
  - students: Daftar (list) yang menyimpan objek-objek Mahasiswa.
- Metode:
  - tambah_mahasiswa: Menambahkan objek Mahasiswa ke dalam daftar students.
  - hapus_mahasiswa: Menghapus objek Mahasiswa dari daftar students berdasarkan nama.
  - ubah_mahasiswa: Mengubah data objek Mahasiswa dalam daftar students berdasarkan nama.
  - cari_mahasiswa: Mencari indeks dari objek Mahasiswa dalam daftar students berdasarkan nama.
  - tampilkan_mahasiswa: Mengembalikan daftar objek Mahasiswa yang ada dalam students.

## Penjelasan Input_form
![gambar4](https://github.com/user-attachments/assets/9e70e124-e75b-4f2b-972f-3e5058cedeea)
1. Kelas InputForm
- Deklarasi Kelas:

  
      class InputForm:
  - Ini mendefinisikan kelas InputForm.
- Metode Statis input_data:

  
      @staticmethod
      def input_data():
  - Metode Statis: Metode ini ditandai dengan dekorator @staticmethod, yang berarti metode ini tidak membutuhkan akses ke instance kelas dan dapat dipanggil langsung dari kelasnya.
- Pengambilan Input:

  
      nim = input("NIM: ")
      nama = input("Nama: ")
      tugas = int(input("Nilai Tugas: "))
      uts = int(input("Nilai UTS: "))
      uas = int(input("Nilai UAS: "))
  - nim: Mengambil input Nomor Induk Mahasiswa dari pengguna.
  - nama: Mengambil input Nama mahasiswa dari pengguna
  - tugas: Mengambil input Nilai Tugas dari pengguna, dan mengkonversi input tersebut ke tipe integer.
  - uts: Mengambil input Nilai Ujian Tengah Semester dari pengguna, dan mengkonversi input tersebut ke tipe integer.
  - uas: Mengambil input Nilai Ujian Akhir Semester dari pengguna, dan mengkonversi input tersebut ke tipe integer.




![gambar5](https://github.com/user-attachments/assets/3e561722-e7e3-4fb9-a84d-4ab6468cd5c5)
![gambar6](https://github.com/user-attachments/assets/a861c2b7-6733-4628-b115-06d4d45b219f)

## Hasil Python
![gambar1](https://github.com/user-attachments/assets/077dc94f-f323-4df0-9b21-80a559614b31)
![gambar2](https://github.com/user-attachments/assets/d1eb8df3-f17f-44bc-bada-5140b9c73891)

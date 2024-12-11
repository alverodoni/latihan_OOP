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

## input_form
![gambar4](https://github.com/user-attachments/assets/9e70e124-e75b-4f2b-972f-3e5058cedeea)
## Penjelasan input_form
1. Kelas InputForm
- Deklarasi Kelas:

  
        class InputForm:
  - Ini mendefinisikan kelas InputForm.
- Metode Statis input_data:

2. Metode Statis input_data:

     
        @staticmethod
        def input_data():
  - Metode Statis: Metode ini ditandai dengan dekorator @staticmethod, yang berarti metode ini tidak membutuhkan akses ke instance kelas dan dapat dipanggil langsung dari kelasnya.
- Pengambilan Input:

3. Pengambilan Input:

     
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
- Mengembalikan Nilai:

4. Mengembalikan Nilai:
   

        return nim, nama, tugas, uts, uas
  - Metode ini mengembalikan nilai-nilai yang telah diinput sebagai tuple.
 
## mahasiswa 
![gambar5](https://github.com/user-attachments/assets/3e561722-e7e3-4fb9-a84d-4ab6468cd5c5)
## Penjelasan tampilmahasiswa
1. Deklarasi Kelas:


        class TampilMahasiswa:
   - Ini mendefinisikan kelas TampilMahasiswa.
     
2. Metode Statis tampilkan_list_mahasiswa:


       @staticmethod
       def tampilkan_list_mahasiswa(mahasiswa_list):
   - Metode Statis: Metode ini ditandai dengan dekorator @staticmethod, yang berarti metode ini tidak membutuhkan akses ke instance kelas dan dapat dipanggil langsung dari kelasnya.
   - Parameter: mahasiswa_list yang merupakan daftar (list) objek Mahasiswa.

3. Fungsi tampilkan_list_mahasiswa:


       print("\nDaftar Mahasiswa")
       print("=" * 50)
       print(f"{'NIM':<10} {'Nama':<20} {'Tugas':<6} {'UTS':<4} {'UAS':<4} {'Akhir':<5}")
       print("=" * 50)
       for mahasiswa in mahasiswa_list:
       print(f"{mahasiswa.nim:<10} {mahasiswa.nama:<20} {mahasiswa.tugas:<6} {mahasiswa.uts:<4} {mahasiswa.uas:<4} {mahasiswa.akhir:<5}")
       print("=" * 50)
   - Menampilkan Header: Menampilkan judul dan header tabel yang memuat kolom NIM, Nama, Tugas, UTS, UAS, dan Akhir.
   - Looping Melalui Daftar Mahasiswa: Menggunakan loop for untuk menampilkan setiap mahasiswa dalam daftar dengan format yang rapi.
   - Menutup Tabel: Menampilkan garis bawah untuk menutup tampilan tabel.

4. Metode Statis tampilkan_detail_mahasiswa:


       @staticmethod
       def tampilkan_detail_mahasiswa(mahasiswa):
   - Metode Statis: Sama seperti metode sebelumnya, metode ini juga tidak membutuhkan akses ke instance kelas.
   - Parameter: mahasiswa yang merupakan objek Mahasiswa.

5. Fungsi tampilkan_detail_mahasiswa:


       print("\nDetail Mahasiswa")
       print("=" * 50)
       print(f"NIM    : {mahasiswa.nim}")
       print(f"Nama   : {mahasiswa.nama}")
       print(f"Tugas  : {mahasiswa.tugas}")
       print(f"UTS    : {mahasiswa.uts}")
       print(f"UAS    : {mahasiswa.uas}")
       print(f"Akhir  : {mahasiswa.akhir}")
       print("=" * 50)
   - Menampilkan Detail: Menampilkan detail dari satu mahasiswa tertentu dengan format terstruktur dan rapi. Setiap informasi (NIM, Nama, Tugas, UTS, UAS, dan Akhir) ditampilkan dengan label dan nilai yang sesuai.
   - Menutup Tampilan Detail: Menampilkan garis bawah untuk menutup tampilan detail.

## main
![gambar6](https://github.com/user-attachments/assets/a861c2b7-6733-4628-b115-06d4d45b219f)
## Penjelasan main 
1. Impor Modul:


       from data.clas_mahasiswa import Mahasiswa, DataMahasiswa
       from view.input_form import InputForm
       from view.mahasiswa import TampilMahasiswa
   - Mahasiswa: Kelas yang merepresentasikan data individual mahasiswa.
   - DataMahasiswa: Kelas yang mengelola daftar mahasiswa.
   - InputForm: Kelas yang digunakan untuk mengambil input data mahasiswa dari pengguna.
   - TampilMahasiswa: Kelas yang digunakan untuk menampilkan data mahasiswa di konsol.

2. Fungsi main:


       def main():
   - Fungsi ini adalah fungsi utama yang akan dijalankan ketika program dimulai.

3. Membuat Instance DataMahasiswa:


       data_mahasiswa = DataMahasiswa()
   - Membuat instance DataMahasiswa yang akan digunakan untuk mengelola data mahasiswa.

4. Loop Menu Utama:


       while True:
        print("\nMenu:")
        print("(T)ambah")
        print("(L)ihat")
        print("(U)bah")
        print("(H)apus")
        print("(K)eluar")
        pilihan = input("Pilih: ").lower()
   -Menampilkan menu utama dan meminta input pilihan dari pengguna.

5. Menangani Pilihan Pengguna:
- Pilihan Tambah Mahasiswa:


      if pilihan == 't':
          nim, nama, tugas, uts, uas = InputForm.input_data()
          mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
          data_mahasiswa.tambah_mahasiswa(mahasiswa)
  - Mengambil data mahasiswa baru dari pengguna dan menambahkannya ke dalam daftar.
- Pilihan Lihat Daftar Mahasiswa:


      elif pilihan == 'l':
        mahasiswa_list = data_mahasiswa.tampilkan_mahasiswa()
        TampilMahasiswa.tampilkan_list_mahasiswa(mahasiswa_list)
  - Menampilkan daftar mahasiswa yang ada di dalam daftar.
- Pilihan Ubah Data Mahasiswa:


      elif pilihan == 'u':
          nama = input("Masukkan nama mahasiswa yang akan diubah: ")
          index = data_mahasiswa.cari_mahasiswa(nama)
          if index is not None:
              print("Data baru:")
              nim, nama_baru, tugas, uts, uas = InputForm.input_data()
              mahasiswa_baru = Mahasiswa(nim, nama_baru, tugas, uts, uas)
              data_mahasiswa.ubah_mahasiswa(nama, mahasiswa_baru)
        else:
              print("Mahasiswa dengan nama tersebut tidak ditemukan.")
  - Mengubah data mahasiswa yang ada di dalam daftar berdasarkan nama.
- Pilihan Hapus Data Mahasiswa:


      elif pilihan == 'h':
          nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
          if data_mahasiswa.hapus_mahasiswa(nama):
              print("Data mahasiswa berhasil dihapus.")
          else:
              print("Mahasiswa dengan nama tersebut tidak ditemukan.")
  - Menghapus data mahasiswa dari daftar berdasarkan nama.
- Pilihan Keluar Program:


      elif pilihan == 'k':
          break
  - Keluar dari program.
- Pilihan Tidak Valid:


      else:
          print("Pilihan tidak valid!")
  - Menangani input yang tidak valid dari pengguna.

6. Menjalankan Program:


       if __name__ == "__main__":
           main()
   - Memastikan bahwa fungsi main hanya akan dipanggil jika skrip dijalankan langsung, bukan diimpor sebagai modul.

## Hasil Python
![gambar1](https://github.com/user-attachments/assets/077dc94f-f323-4df0-9b21-80a559614b31)
![gambar2](https://github.com/user-attachments/assets/d1eb8df3-f17f-44bc-bada-5140b9c73891)

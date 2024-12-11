from data.clas_mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("(T)ambah")
        print("(L)ihat")
        print("(U)bah")
        print("(H)apus")
        print("(K)eluar")
        pilihan = input("Pilih: ").lower()

        if pilihan == 't':
            nim, nama, tugas, uts, uas = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, tugas, uts, uas)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
        elif pilihan == 'l':
            mahasiswa_list = data_mahasiswa.tampilkan_mahasiswa()
            TampilMahasiswa.tampilkan_list_mahasiswa(mahasiswa_list)
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
        elif pilihan == 'h':
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            if data_mahasiswa.hapus_mahasiswa(nama):
                print("Data mahasiswa berhasil dihapus.")
            else:
                print("Mahasiswa dengan nama tersebut tidak ditemukan.")
        elif pilihan == 'k':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

class TampilMahasiswa:
    @staticmethod
    def tampilkan_list_mahasiswa(mahasiswa_list):
        print("\nDaftar Mahasiswa")
        print("=" * 50)
        print(f"{'NIM':<10} {'Nama':<20} {'Tugas':<6} {'UTS':<4} {'UAS':<4} {'Akhir':<5}")
        print("=" * 50)
        for mahasiswa in mahasiswa_list:
            print(f"{mahasiswa.nim:<10} {mahasiswa.nama:<20} {mahasiswa.tugas:<6} {mahasiswa.uts:<4} {mahasiswa.uas:<4} {mahasiswa.akhir:<5}")
        print("=" * 50)

    @staticmethod
    def tampilkan_detail_mahasiswa(mahasiswa):
        print("\nDetail Mahasiswa")
        print("=" * 50)
        print(f"NIM    : {mahasiswa.nim}")
        print(f"Nama   : {mahasiswa.nama}")
        print(f"Tugas  : {mahasiswa.tugas}")
        print(f"UTS    : {mahasiswa.uts}")
        print(f"UAS    : {mahasiswa.uas}")
        print(f"Akhir  : {mahasiswa.akhir}")
        print("=" * 50)

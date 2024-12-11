class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = self.calculate_final_grade()

    def calculate_final_grade(self):
        return round((self.tugas * 0.3) + (self.uts * 0.35) + (self.uas * 0.35), 2)

class DataMahasiswa:
    def __init__(self):
        self.students = []

    def tambah_mahasiswa(self, mahasiswa):
        self.students.append(mahasiswa)

    def hapus_mahasiswa(self, nama):
        index = self.cari_mahasiswa(nama)
        if index is not None:
            del self.students[index]
            return True
        return False

    def ubah_mahasiswa(self, nama, mahasiswa_baru):
        index = self.cari_mahasiswa(nama)
        if index is not None:
            self.students[index] = mahasiswa_baru
            return True
        return False

    def cari_mahasiswa(self, nama):
        for index, mahasiswa in enumerate(self.students):
            if mahasiswa.nama == nama:
                return index
        return None

    def tampilkan_mahasiswa(self):
        return self.students
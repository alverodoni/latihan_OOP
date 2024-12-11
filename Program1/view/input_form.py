class InputForm:
    @staticmethod
    def input_data():
        nim = input("NIM: ")
        nama = input("Nama: ")
        tugas = int(input("Nilai Tugas: "))
        uts = int(input("Nilai UTS: "))
        uas = int(input("Nilai UAS: "))
        return nim, nama, tugas, uts, uas

data_buku = {
    "buku1"          : {
        "judul"         : "Dikta & Hukum",
        "penulis"       : "Dhia Farah",
        "tahun_terbit"  : 2021
    },

    "buku2" : {
        "judul"        : "Retak",
        "penulis"      : "Azhara Natasya",
        "tahun_terbit" : 2021
    },

    "buku3" : {
        "judul"        : "Hello, Cello",
        "penulis"      : "Nadia Ristivani",
        "tahun_terbit" : 2022
    },

    "buku4" : {
            "judul"        : "Himpunan",
            "penulis"      : "Citra Saras Paramitha",
            "tahun_terbit" : 2018
        },
}

while True:
    print("\n=== MENU DATA BUKU ===")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("\n=== MENAMPILKAN DATA BUKU ===")
        for buku, data in data_buku.items():
            print("\n", buku)
            print("Judul        :", data["judul"])
            print("Penulis      :", data["penulis"])
            print("Tahun Terbit :", data["tahun_terbit"])

            if "penerbit" in data:
                print("Penerbit     :", data["penerbit"])

    elif pilihan == "2":
        print("\n=== TAMBAH DATA PENERBIT ===")
        print("Pilihan buku:")
        print("1. Buku 1")
        print("2. Buku 2")
        print("3. Buku 3")
        print("4. Buku 4")

        for buku, data in data_buku.items():
            print(buku, ":", data["judul"])

        pilih_buku = input("Pilihlah buku: ")

        if pilih_buku == "1":
            penerbit = input("Masukkan data penerbit: ")
            data_buku["buku1"]["penerbit"] = penerbit
            print("DATA PENERBIT BERHASIL DITAMBAHKAN.")

        elif pilih_buku == "2":
            penerbit = input("Masukkan data penerbit: ")
            data_buku["buku2"]["penerbit"] = penerbit
            print("DATA PENERBIT BERHASIL DITAMBAHKAN.")

        elif pilih_buku == "3":
            penerbit = input("Masukkan data penerbit: ")
            data_buku["buku3"]["penerbit"] = penerbit
            print("DATA PENERBIT BERHASIL DITAMBAHKAN.")

        elif pilih_buku == "4":
            penerbit = input("Masukkan data penerbit: ")
            data_buku["buku4"]["penerbit"] = penerbit
            print("DATA PENERBIT BERHASIL DITAMBAHKAN.")

        else:
            print("PILIHAN BUKU TIDAK TERSEDIA.")

    elif pilihan == "3":
            print("\n=== UBAH PENULIS ===")
            print("Pilihan buku:")
            print("1. Buku 1")
            print("2. Buku 2")
            print("3. Buku 3")
            print("4. Buku 4")
        
            pilih_buku = input("Pilihlah buku: ")
        
            if pilih_buku == "1":
                penulis = input("Masukkan penulis baru: ")
                data_buku["buku1"]["penulis"] = penulis
                print("DATA PENULIS BERHASIL DIUBAH.")
        
            elif pilih_buku == "2":
                penulis = input("Masukkan penulis baru: ")
                data_buku["buku2"]["penulis"] = penulis
                print("DATA PENULIS BERHASIL DIUBAH.")
        
            elif pilih_buku == "3":
                penulis = input("Masukkan penulis baru: ")
                data_buku["buku3"]["penulis"] = penulis
                print("DATA PENULIS BERHASIL DIUBAH.")
        
            elif pilih_buku == "4":
                penulis = input("Masukkan penulis baru: ")
                data_buku["buku4"]["penulis"] = penulis
                print("DATA PENULIS BERHASIL DIUBAH.")

            else:
                print("DATA PENULIS TIDAK TERSEDIA.")

    elif pilihan == "4":
        print("\n=== HAPUS DATA PENERBIT ===")

        for buku, data in data_buku.items():
            print(buku, ":", data["judul"])

        pilih_buku = input("Pilihlah buku: ")

        if pilih_buku in data_buku:
            if "penerbit" in data_buku[pilih_buku]:
                del data_buku[pilih_buku]["penerbit"]
                print("DATA PENERBIT BERHASIL DIHAPUS.")
            else:
                print("Data penerbit belum ada.")
        else:
            print("PILIHAN BUKU TIDAK TERSEDIA.")

    elif pilihan == "5":
        print("\nPROGRAM SELESAI.")
        print("\nData Buku Setelah Perubahan:")

        for buku, data in data_buku.items():
            print("\n", buku)
            print("Judul        :", data["judul"])
            print("Penulis      :", data["penulis"])
            print("Tahun Terbit :", data["tahun_terbit"])

            if "penerbit" in data:
                print("Penerbit     :", data["penerbit"])
        break
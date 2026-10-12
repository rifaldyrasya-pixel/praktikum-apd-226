import os

users = [
    ["rasya", "073", "admin"],
    ["smk", "123", "user"]
]

antrean_servis = []
while True:
    user_login = ""
    role_login = ""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================================")
        print("         MOTOCARE MANAGER - LOGIN         ")
        print("==========================================")
        print("1. Login Akun")
        print("2. Register Akun Baru")
        print("3. Keluar Program")
        print("==========================================")
        pilihan_auth = input("Pilih menu (1-3): ")

        if pilihan_auth == "1":
            print("\n--- SILAHKAN LOGIN ---")
            input_user = input("Masukkan Username : ")
            input_pin = input("Masukkan PIN      : ")

            login_sukses = False
            for u in users:
                if u[0] == input_user and u[1] == input_pin:
                    user_login = u[0]
                    role_login = u[2]
                    login_sukses = True
                    break

            if login_sukses:
                print(f"\n>> Login Berhasil! Selamat datang, {user_login} ({role_login}).")
                input("Tekan Enter untuk masuk ke menu utama...")
                break
            else:
                print("\n>> Username atau PIN salah! Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == "2":
            print("\n--- REGISTER AKUN BARU ---")
            reg_user = input("Buat Username baru : ")
            
            user_sudah_ada = False
            for u in users:
                if u[0] == reg_user:
                    user_sudah_ada = True
                    break
            
            if user_sudah_ada:
                print(">> Username tersebut sudah digunakan! Gunakan yang lain.")
            else:
                reg_pin = input("Buat PIN baru      : ")
                users.append([reg_user, reg_pin, "user"])
                print(">> Akun berhasil didaftarkan! Silakan login.")
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan_auth == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Program dihentikan. Terima kasih!")
            exit()
        else:
            print("\n>> Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==========================================")
        print(f"   BENGKEL MOTOCARE - [Login: {user_login}]")
        print("==========================================")
        print("1. Lihat Daftar Antrean")
        if role_login == "admin":
            print("2. Tambah Antrean Motor")
            print("3. Update Status Pengerjaan")
            print("4. Motor Selesai / Hapus Antrean")
        print("5. Logout / Ganti Akun")
        print("6. Keluar Program")
        print("==========================================")
        
        pilihan_menu = input("Pilih menu: ")

        if pilihan_menu == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== DAFTAR ANTREAN SERVIS BENGKEL ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor saat ini.")
            else:
                no = 1
                for item in antrean_servis:
                    print(f"{no}. [{item[4]}] {item[0]} - {item[2]} ({item[1]}) | Keluhan: {item[3]}")
                    no += 1
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "2" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== TAMBAH ANTREAN MOTOR BARU ===")
            nama = input("Nama pemilik  : ")
            plat = input("Plat nomor    : ")
            merk = input("Merk motor    : ")
            keluhan = input("Keluhan       : ")
            status_awal = "Antri"

            antrean_servis.append([nama, plat, merk, keluhan, status_awal])
            print("\n>> Data antrean motor berhasil ditambahkan!")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "3" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== UPDATE STATUS PENGERJAAN ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor untuk di-update.")
            else:
                no = 1
                for item in antrean_servis:
                    print(f"{no}. {item[0]} - {item[2]} ({item[1]}) [Status: {item[4]}]")
                    no += 1
                
                pilih_str = input("\nPilih nomor antrean yang mau diubah: ")
                
                if pilih_str.isdigit():
                    pilih = int(pilih_str) - 1
                    if pilih >= 0 and pilih < len(antrean_servis):
                        print(f"Status sekarang: {antrean_servis[pilih][4]}")
                        print("1. Dikerjakan")
                        print("2. Selesai")
                        st = input("Pilih status baru (1/2): ")
                        
                        if st == "1":
                            antrean_servis[pilih][4] = "Dikerjakan"
                            print(">> Status berhasil diubah jadi 'Dikerjakan'")
                        elif st == "2":
                            antrean_servis[pilih][4] = "Selesai"
                            print(">> Status berhasil diubah jadi 'Selesai'")
                        else:
                            print(">> Pilihan status tidak valid.")
                    else:
                        print(">> Nomor antrean tidak ditemukan.")
                else:
                    print(">> Masukkan angka yang valid.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "4" and role_login == "admin":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== HAPUS / SELESAI ANTREAN MOTOR ===")
            if len(antrean_servis) == 0:
                print("Belum ada antrean motor untuk dihapus.")
            else:
                no = 1
                for item in antrean_servis:
                    print(f"{no}. {item[0]} - {item[2]} ({item[1]})")
                    no += 1
                
                pilih_str = input("\nPilih nomor motor yang ingin dihapus/diambil: ")
                
                if pilih_str.isdigit():
                    pilih = int(pilih_str) - 1
                    if pilih >= 0 and pilih < len(antrean_servis):
                        data_hapus = antrean_servis.pop(pilih)
                        print(f">> Data motor {data_hapus[2]} ({data_hapus[1]}) milik {data_hapus[0]} berhasil dihapus dari antrean.")
                    else:
                        print(">> Nomor antrean tidak ditemukan.")
                else:
                    print(">> Masukkan angka yang valid.")
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan_menu == "5":
            print("\n>> Berhasil Logout.")
            input("Tekan Enter untuk kembali ke halaman login...")
            break 

        elif pilihan_menu == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terima kasih telah menggunakan MotoCare Manager!")
            exit()
        else:
            print("\n>> Pilihan menu tidak valid atau hak akses tidak diizinkan.")
            input("Tekan Enter untuk melanjutkan...")
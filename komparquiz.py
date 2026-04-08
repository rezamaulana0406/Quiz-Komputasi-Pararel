import time
import random

def simulasi_statis():
    print("\n[INFO] Memulai Distribusi Statis (Beban Tetap)")
    beban = [80, 20]
    target = sum(beban) // len(beban)
    iterasi = 0
    
    print(f"[TASK] Inisialisasi beban awal: Pekerja A={beban[0]}, Pekerja B={beban[1]}")
    print(f"[TASK] Target distribusi ideal: {target}")
    
    while beban[0] != target:
        iterasi += 1
        beban[0] -= 1
        beban[1] -= -1
        print(f"[EXEC] Iterasi {iterasi}: Memindahkan 1 beban dari A ke B -> {beban}")
        
    print(f"[RESULT] Distribusi ideal tercapai. Total pergeseran: {iterasi} kali.")

def simulasi_dinamis():
    print("\n[INFO] Memulai Distribusi Dinamis (Antrean Tugas)")
    daftar_tugas = [random.randint(2, 8) for _ in range(5)]
    pekerja = {"Pekerja_1": 0, "Pekerja_2": 0}
    waktu_total = 0
    
    print(f"[TASK] Daftar tugas masuk (durasi detik): {daftar_tugas}")
    
    while daftar_tugas or any(v > 0 for v in pekerja.values()):
        for p in pekerja:
            if pekerja[p] == 0 and daftar_tugas:
                durasi = daftar_tugas.pop(0)
                pekerja[p] = durasi
                print(f"[EXEC] {p} mengambil tugas baru dengan durasi {durasi}s")
        
        durasi_aktif = [v for v in pekerja.values() if v > 0]
        if not durasi_aktif: break
            
        langkah = min(durasi_aktif)
        waktu_total += langkah
        for p in pekerja:
            if pekerja[p] > 0:
                pekerja[p] -= langkah
        print(f"[STATUS] Waktu berjalan: {waktu_total}s (Proses sedang dikerjakan...)")
    print("")
    print(f"[RESULT] Semua tugas selesai. Waktu optimal: {waktu_total} detik.")

def main():
    nrp_input = input("Masukkan NRP Anda: ")
    try:
        nrp = int(nrp_input)
        if nrp % 2 == 0:
            print(f"IDENTIFIKASI: NRP {nrp} adalah GENAP")
            simulasi_statis()
        else:
            print(f"IDENTIFIKASI: NRP {nrp} adalah GANJIL")
            simulasi_dinamis()
    except ValueError:
        print("Input salah. Masukkan angka NRP.")

if __name__ == "__main__":
    main()

print("=" * 50)
print("Nama: Reza Maulana Yazi")
print("NRP: 152024012")
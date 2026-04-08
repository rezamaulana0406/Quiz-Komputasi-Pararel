import time
import random

def simulasi_statis():
    beban = [80, 20]
    target = sum(beban) // len(beban)
    iterasi = 0
    print(f"Mulai Statis: {beban}")
    while beban[0] != target:
        iterasi += 1
        beban[0] -= 1
        beban[1] += 1
        print(f"Iterasi {iterasi}: {beban}")
    print(f"Distribusi ideal tercapai di iterasi ke-{iterasi}")

def simulasi_dinamis():
    daftar_tugas = [random.randint(2, 8) for _ in range(10)]
    pekerja = {"Pekerja_1": 0, "Pekerja_2": 0}
    waktu_total = 0
    print(f"Daftar Tugas: {daftar_tugas}")
    while daftar_tugas or any(v > 0 for v in pekerja.values()):
        for p in pekerja:
            if pekerja[p] == 0 and daftar_tugas:
                pekerja[p] = daftar_tugas.pop(0)
                print(f"{p} mengambil tugas durasi {pekerja[p]}s")
        durasi_aktif = [v for v in pekerja.values() if v > 0]
        if not durasi_aktif:
            break
        langkah = min(durasi_aktif)
        for p in pekerja:
            if pekerja[p] > 0:
                pekerja[p] -= langkah
        waktu_total += langkah
    print(f"Waktu optimal penyelesaian: {waktu_total} detik")

def main():
    input_user = input("Masukkan NRP Anda: ")
    try:
        nrp = int(input_user)
        if nrp % 2 == 0:
            print(f"NRP ({nrp}) terdeteksi GENAP.")
            simulasi_statis()
        else:
            print(f"NRP ({nrp}) terdeteksi GANJIL.")
            simulasi_dinamis()
    except ValueError:
        print("Error: masukkan angka saja.")

if __name__ == "__main__":
    main()

print("=" * 50)
print("Nama: Reza Maulana Yazi")
print("NRP: 152024012")
# ====================================================
# Tugas Praktikum Pertemuan 2
# ====================================================

NAMA_FILE = "stok_barang.txt"

def muat_data():
    data_stok = {}
    try:
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                bagian = baris.strip().split(",")
                if len(bagian) == 3:
                    kode, nama, stok = bagian
                    data_stok[kode] = {"nama": nama, "stok": int(stok)}
    except FileNotFoundError:
        pass 
    return data_stok

def tampilkan_semua(data):
    print(f"\n{'='*45}")
    print(f"{'KODE':<10} | {'NAMA BARANG':<20} | {'STOK':<5}")
    print(f"{'-'*45}")
    if not data:
        print("Belum ada data barang.")
    else:
        for k, v in sorted(data.items()):
            peringatan = "(!)" if v['stok'] < 10 else ""
            print(f"{k:<10} | {v['nama']:<20} | {v['stok']:<5} {peringatan}")
    print(f"{'='*45}")

def laporan_singkat(data):
    if not data:
        print("\nData kosong, tidak bisa membuat laporan.")
        return

    total_jenis = len(data)
    total_stok = sum(item['stok'] for item in data.values())
    stok_rendah = [v['nama'] for v in data.values() if v['stok'] < 10]

    print("\n--- LAPORAN RINGKAS GUDANG ---")
    print(f"Total Jenis Barang  : {total_jenis}")
    print(f"Total Seluruh Stok  : {total_stok}")
    
    if stok_rendah:
        print(f"Barang Hampir Habis : {', '.join(stok_rendah)}")
    else:
        print("Barang Hampir Habis : Tidak ada (Aman)")

def cari_barang(data):
    kode = input("\nCari kode barang: ").strip()
    if kode in data:
        print(f"Ditemukan: {data[kode]['nama']} | Stok: {data[kode]['stok']}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang(data):
    kode = input("\nKode baru: ").strip()
    if kode in data:
        print("Gagal: Kode sudah ada.")
    else:
        nama = input("Nama barang: ")
        stok = int(input("Stok awal: "))
        data[kode] = {"nama": nama, "stok": stok}
        print("Barang ditambahkan.")

def update_stok(data):
    kode = input("\nKode barang: ").strip()
    if kode in data:
        print(f"Stok {data[kode]['nama']} saat ini: {data[kode]['stok']}")
        jml = int(input("Jumlah perubahan (+/-): ")) # Bisa input -5 untuk kurangi
        if data[kode]['stok'] + jml < 0:
            print("Gagal: Stok tidak boleh negatif!")
        else:
            data[kode]['stok'] += jml
            print("Stok diperbarui.")
    else:
        print("Kode tidak ditemukan.")

def simpan_data(data):
    with open(NAMA_FILE, "w") as file:
        for k, v in data.items():
            file.write(f"{k},{v['nama']},{v['stok']}\n")
    print("\n[Data tersimpan di file]")

def main():
    db = muat_data()
    while True:
        print("\n--- SISTEM STOK V.2 ---")
        print("1. Lihat Semua")
        print("2. Cari Kode")
        print("3. Tambah Barang")
        print("4. Update Stok")
        print("5. Laporan Statistik (Baru!)")
        print("6. Simpan Ke File")
        print("0. Keluar")
        
        pilih = input("Menu: ")
        if pilih == "1": tampilkan_semua(db)
        elif pilih == "2": cari_barang(db)
        elif pilih == "3": tambah_barang(db)
        elif pilih == "4": update_stok(db)
        elif pilih == "5": laporan_singkat(db)
        elif pilih == "6": simpan_data(db)
        elif pilih == "0": break
        else: print("Pilihan salah.")

if __name__ == "__main__":
    main()
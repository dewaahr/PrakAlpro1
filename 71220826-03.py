hari_kerja=int(input("Masukan Jumlah Hari Kerja:"))
upah_bruto=10_000*(hari_kerja*8)
pajak=upah_bruto*5/100
upah_netto=upah_bruto-pajak
print("Upah karyawan sebelum pajak: Rp",upah_bruto)
print("Pajak yang harus dibayar: Rp",pajak)
print("Penghasilan bersih yang diterima: Rp",upah_netto)

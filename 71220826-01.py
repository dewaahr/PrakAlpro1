print('='*5,"Program Menghitung Selisih Menit","="*5)
jam_awal= int(input('Masukan jam awal :'))
menit_awal= int(input('Masukan Menit awal :'))
jam_akhir= int(input('Masukan jam akhir :'))
menit_akhir= int(input('Masukan Menit akhir :'))

selisih_jam=(jam_akhir-jam_awal)*60
selisih_menit=menit_akhir-menit_awal
total_selisih =selisih_menit+selisih_jam
print("Selisihnya adalah",total_selisih,"Menit")


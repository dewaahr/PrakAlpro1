
variabel_x=(input("Masukan Nilai X:"))
if "/" not in variabel_x:
    variabel_x=int(variabel_x)
    f=(3*(variabel_x)**3)-(12*(variabel_x)**2)+(7/15*variabel_x)-(22/7)
    print("Hasilnya adalah",f)
else:
    variabel_x_baru=variabel_x.split("/")
    atas=float(variabel_x_baru[0])
    bawah=float(variabel_x_baru[1])
    variabel_x=atas/bawah
    f=(3*(variabel_x)**3)-(12*(variabel_x)**2)+(7/15*variabel_x)-(22/7)
    print("Hasilnya adalah",f)
def boi_tinh_duyen(ten_nam, ten_nu):
    ten_nam = ten_nam.lower()
    ten_nu = ten_nu.lower()
    dem = 0
    for chu_cai in range(ord('a'), ord('z') + 1):
        if chr(chu_cai) in ten_nam and chr(chu_cai) in ten_nu:
            dem += 1
    if dem == 0:
        ket_qua = "nguoi dung nuoc la"
    elif dem < 5:
        ket_qua = "em chi xem anh la thang ban than"
    else:
        ket_qua = "I love you"
    return ket_qua
print("Nhap ten nam:")
ten_nam = input()
print("Nhap ten nu:")
ten_nu = input()
ket_qua_boi = boi_tinh_duyen(ten_nam, ten_nu)
print("Ket qua boi tinh duyen:", ket_qua_boi)


def them(chi_tieu, khoan_chi):
    chi_tieu.append(khoan_chi)
    
def xem(chi_tieu):
    for khoan_chi in chi_tieu:
        print(khoan_chi)
        
def xoa(chi_tieu, ten_chi_tieu):
    index = -1
    for i in range(len(chi_tieu)):
        if ten == chi_tieu[i]["ten"]:
            index = i
            break
    if index == -1:
        print("khong tim thay khoan chi")
              
    else:
        chi_tieu.remove(chi_tieu[index])
        
chi_tieu = []

while True:
    yeu_cau = int(input("lua chon: An 1 de xem chi tieu, an 2 de them chi tieu, an 3 de xoa chi tieu "))
    if (yeu_cau == 1):
        print("hien thi cac chi tieu hien co: ")
        xem(chi_tieu)
    elif(yeu_cau == 2):
        print("them mot khoan chi moi: ")
        ten = input("nhap vao ten khoan chi: ")
        so_tien = int(input("nhap so tien da chi: "))
        ngay = input("nhap ngay chi: ")
        khoan_chi = {
            "ten": ten,
            "so_tien": so_tien,
            "ngay": ngay
        }
        them(chi_tieu, khoan_chi)
    elif(yeu_cau == 3):
        print("xoa mot khoan chi: ")
        ten = input("nhap ten khoan chi muon xoa: ")
        xoa(chi_tieu,ten)
    else:
        print("ban nhap khong dung, vui long nhap lai: ")
    confirm = input("ban co muon tiep tuc khong? Y/N: ? ")
    if confirm.upper() == "N":
        break
        
            










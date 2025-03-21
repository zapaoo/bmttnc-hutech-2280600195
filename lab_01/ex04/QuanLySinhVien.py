from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien=[]

    def generateID(self):
        maxID = 1
        if(self.soLuongSinhVien() >0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxID<sv._id):
                    maxID = sv._id
            maxID = maxID +1
        return maxID
        
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh sinh vien: ")
        while True:
            diemTB = float(input("nhap diem cua sinh vien: "))
            if 0<=diemTB<=10:
                break
            print("Diem nhap khong hop le")
        sv= SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv !=None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh sinh vien: ")
            while True:
                diemTB = float(input("nhap diem cua sinh vien: "))
                if 0<=diemTB<=10:
                    break
                print("Diem nhap khong hop le")
            sv._name= name
            sv._sex = sex
            sv._major= major
            sv._diemTB=diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinhvien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse= False)

    def sortByName(self):
       self.listSinhVien.sort(key=lambda x: x._name, reverse= False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse= False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    def findByName(self, keyword):
        listSV=[]
        if(self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteByID(self, ID):
        isDelete = False
        sv = self.findByID(ID)
        if (sv !=None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif(sv._diemTB >=5):
            sv._hocLuc = "Trung Binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        if not isinstance(listSV, list):
            print("Error: listSV không phải là danh sách!")
            return

        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))

        if listSV:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8.2f} {:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc
                ))
        else:
            print("Danh sách sinh viên trống.")
        
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

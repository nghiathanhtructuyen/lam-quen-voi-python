# Khai báo các thư viện cần sử dụng trong file 
import array as arr

# Bài số 1
def so_gap_doi():
	limit_number = 100
	check = True
	while check:
		a = int(input("Nhập vào một số A bất kỳ: "))
		if a > limit_number: 
			check = True
		else:
			print("Giá trị trả về là: " + str(a * 2))
			break
	print("Kết thúc")


# Bài số 2
def phep_tinh_so_1():
	limit_number = 100
	check = True
	while check:
		a, b, c = map(float, input('Nhập ba số a, b, c bất kỳ cách nhau một khoảng trắng: ')).split()
		if a > limit_number and b > limit_number and c > limit_number: 
			check = True
		else:
			print("Giá trị của phép tính (A - B) * C là: " + str(((a - b) * c)))
			break
	print("Kết thúc")


# Bài số 3
def ky_tu_moi():
	a = input("Nhập vào một ký tự hoa bất kỳ: ")
	print(a.lower())
	print("Kết thúc")


# Bài số 4
def so_so_hang(): 
	limit_number_on_top = 50
	limit_number_on_bottom = 0
	check = True
	while check:
		n = int(input("Nhập một số dương bất kỳ nhỏ hơn hoặc bằng 50: "))
		if n > limit_number_on_top or n < limit_number_on_bottom:
			check = True
		else:
			start = (n - 1) / 2
			end = n
			print("Số các số hạng trong khoảng từ (n - 1) / 2 cho đến n là: " + str(end - start + 1))
			break
	print("Kết thúc")


# Bài số 5
def so_so_hang_2():
	limit_number_on_top = 15
	limit_number_on_bottom = 0
	check = True
	while check:
		n = int(input("Nhập một số dương bất kỳ nhỏ hơn hoặc bằng 50: "))
		if n > limit_number_on_top or n < limit_number_on_bottom:
			check = True
		else:
			start = n + 1
			end = n ** 2
			print("Kết quả của bài toán đã cho là: " + str(end - start + 1))
			break
	print("Kết thúc")


# Bài số 6
def chuoi_mo_dau_ngay_moi():
	chuoi_ban_dau = input("Nhập chuỗi ban đầu vào đây: ")
	print(chuoi_ban_dau.reverse())
	print("Kết thúc")


# Bài số 7
def phep_tinh_phuc_tap():
	limit_number = 1000
	check = True
	while check:
		a, b = map(float, input('Nhập hai số a và b bất kỳ cách nhau một khoảng trắng: ')).split()
		if a > limit_number and b > limit_number: 
			check = True
		else:
			print("Giá trị trả về là: " + str(a + b + a * b))
			break
	print("Kết thúc")


# Bài số 8: 
def ky_tu_cu():
	a = input("Nhập vào một ký tự thường bất kỳ: ")
	print(a.upper())
	print("Kết thúc")


# Bài số 9: 
def vong_tron_chu():
	bang_chu_cai_alphabet = "abcdefghiklmnopqrstuvwxyz"
	check = True
	while check: 
		chu_cai, chu_so = input("Nhập một chữ cái thường và một số bé hơn hoặc bằng 10: ").split
		if int(chu_so) > 10 and int(chu_so) < 0: 
			check = True
		else: 
			if len(chu_cai) != 1: 
				check = True
			elif chu_cai == "z" and chu_so == 1:
				print("Kết quả cho ra của vòng tròn chữ là: z")
				break
			else: 
				print("Kết quả cho ra của vòng tròn chữ là: " + bang_chu_cai_alphabet[bang_chu_cai_alphabet.find(chu_cai)] + chu_so)
				break
	print("Kết thúc")


# Bài số 10: 
def chu_lien_truoc():
	bang_chu_cai_alphabet = "abcdefghiklmnopqrstuvwxyz"
	check = True
	while True:
		a = "Nhập một chữ cái bất kỳ vào đây: "
		if len(a) != 1:
			check = True
		else: 
			if a == a.upper(): 
				check = True
			elif a == "a":
				print("Không có chữ cái nào đứng sau ký tự *a*")
				break
			else:
				print("Kết quả trả về là: " + bang_chu_cai_alphabet[bang_chu_cai_alphabet.find(a) - 1])
				break
	print("Kết thúc")


# Bài số 11:
def tam_giac():
	limit_top = 100
	limit_bottom = 0
	check = True
	while check: 
		a, b, c = double(input("Nhập số đo ba cạnh của một tam giác: "))
		if limit_bottom < a <= limit_top and limit_bottom < b <= limit_top and limit_bottom < c <= limit_top:
			nua_chu_vi = (a + b + c) / 2
			dien_tich_tam_giac = sqrt(nua_chu_vi * (nua_chu_vi - a) * (nua_chu_vi - b) * (nua_chu_vi - c))
			print("Diện tích của tam giác là: " + str(dien_tich_tam_giac))
			break
		else: 
			check = True
	print("Kết thúc")


# Bài số 12: 
def hinh_chu_nhat_thang():
	limit_top = 100
	limit_bottom = 0
	check = True
	while check: 
		hang_ngang, hang_doc = int(input("Nhập độ dài 2 cạnh của hình chữ nhật là số dương tại đây: "))
		if limit_bottom < hang_ngang <= limit_top and limit_bottom < hang_doc <= limit_top:
			for i in range(1, hang_doc):
				for j in range(1, hang_ngang): 
					print("#")
				print("\n")
		else:
			check = True
	print("Kết thúc")


# Bài số 13: 
def giai_thua():
	check = True
	while check:
		a = int(input("Nhập vào đây một số dương bất kỳ lớn hơn 0: "))
		if a > 10 or a < 0: 
			check = True
		else: 
			giai_thua = 1
			for i in range(1, a):
				giai_thua *= i
			print("Giá trị của bài toán là: " + str(giai_thua))
			break
	print("Kết thúc")


# Bài số 14: 
def chu_cai_nam_giua():
	bang_chu_cai_alphabet = "abcdefghiklmnopqrstuvwxyz"
	check = True
	while check:
		a, b = input("Nhập vào đây 2 chữ cái bất kỳ trong bảng chữ cái: ")
		if len(a) != 1 and len(b) != 1: 
			check = True
		else:
			do_dai_cua_chuoi = len(bang_chu_cai_alphabet[bang_chu_cai_alphabet.find(a) : bang_chu_cai_alphabet.find(b)])
			print("Số chữ số đứng ở giữa là: " + str(do_dai_cua_chuoi))
			break
	print("Kết thúc")


# Bài số 15: 
def xau_lien_xau():
	a = input("Nhập một xâu bất kỳ vào đây")
	print("Kết quả sau khi nhập là: " + a + a.reverse())
	print("Kết thúc")


# Bài số 16: 
def chu_cai_lap_lai():
	check = True
	while check: 
		a = input("Nhập một chữ cái bất kỳ vào đây: ")
		if len(a) != 1: 
			check = True
		else: 
			if a == a.upper():
				for i in range(1, 10):
					print(a.lower())
				break
			else:
				for i in range(1, 10):
					print(a)
				break
	print("Kết thúc")


# Bài số 17: 
def lai_la_tam_giac():
	check = True
	while True:
		a, b, c = map(float, input('Nhập độ dài ba cạnh a, b, c của tam giác: ')).split()
		if a < 0 and b < 0 and c < 0: 
			check = True
		else: 
			if (a + b) > c and (b + c) > a and (a + c) > b:
				print("YES")
				break
			else:
				print("NO")
				break
	print("Kết thúc")


# Bài số 18: 
def chan_dau_va_chan_cuoi():
	check = True
	while check:
		so_cac_so_nhap_vao = int(input("Nhập số các số nhập đầu vào: "))
		if so_cac_so_nhap_vao > 1000 and so_cac_so_nhap_vao < 0: 
			check = True
		else:
			mang_luu_tru = arr.array('i')
			for i in range(0, so_cac_so_nhap_vao - 1):
				while True:
					number = int(input())
					if number > 1000000:
						print("Nhập giá trị quá giới hạn. Vui lòng nhập lại!")
						continue
					else:
						mang_luu_tru[i] = number
						break
			print(mang_luu_tru[0])
			print(mang_luu_tru[len(mang_luu_tru) - 1])
			break
	print("Kết thúc")


# Bài số 19: 
def so_19():
	check = True
	while check:
		a = int(input("Nhập vào một số bất kỳ: "))
		if a > 10**15: 
			print("Giá trị lớn hơn cho phép. Vui lòng nhập lại!")
			check = True
		else: 
			if a != 19: 
				print("IMPOSSIBLE")
				continue
			else: 
				print(a)
				break
	print("Kết thúc")


# Bài số 20: 
def tu_khoa():
	check = True
	while check: 
		chuoi_bat_ky = input("Nhập vào một chuỗi bất kỳ lớn hơn 20: ")
		if len(chuoi_bat_ky) < 20:
			print("Độ dài không đảm bảo. Vui lòng nhập lại!")
			check = True
		else:
			print(chuoi_bat_ky[4].upper())
			print(chuoi_bat_ky[8].upper())
			break
	print("Kết thúc")


# Bài số 21:
def tam_giac_vuong_can():
	a = int(input("Nhập độ dài của tam giác là một số nguyên dương"))
	if a <= 1: 
		print("Không thể vẽ tam giác kiểu như vậy")
	else: 
		for i in range(0, a - 1):
			for j in range(1, a):
				print("*")
			break
	print("Kết thúc")


# Bài số 22: 
def binh_phuong():
	check = True
	while check:
		n = int(input("Nhập một giá trị n bất kỳ: "))
		if n > 10**9 and n < 0:
			print("Giá trị không phù hợp. Vui lòng nhập lại!")
			check = True
		else:
			print(n**2)
			break
	print("Kết thúc")


# Bài số 23:
def day_so_2():
	n = int(input("Nhập một số nguyên dương bất kỳ: "))
	if n < 0: 
		print("Không có số nào trong dãy F cả!")
	elif n == 0:
		print("1")
	elif n == 1:
		print("2")
	else: 
		f0, f1 = 1, 2
		for i in range(2, n + 1):
			f2 = 2 * f1 - f0
			f0, f1 = f1, f2
		print(f1)
	print("Kết thúc")


# Bài số 24
def day_so_1():
	n = int(input("Nhập một số nguyên dương bất kỳ: "))
	if n < 0: 
		print("Không có số nào trong dãy F cả!")
	elif n == 0:
		print("1")
	elif n == 1:
		print("1")
	else: 
		f0, f1 = 1, 1
		for i in range(1, n + 1):
			f2 = 2 * f1 - f0
			f0, f1 = f1, f2
		print(f1)
	print("Kết thúc")


# Bài số 25:
def gap_doi():
	chuoi_bat_ky = input("Nhập một chuỗi chữ cái bất kỳ: ")
	print(chuoi_bat_ky + " " + chuoi_bat_ky)
	print("Kết thúc")


# Bài số 26:
def sap_xep():
	a, b, c = map(int, input('Nhập 3 số a, b, c bất kỳ vào đây: ')).split()
	sort_array = array.arr('i')
	print(sort_array.sort())
	print("Kết thúc")


# Bài số 27: 
def primes():
	n = int(input("Nhập một số nguyên dương bất kỳ: "))
	if n <= 1:
		return False
	elif n == 2:
		return True
	if n % 2 == 0:
		return False
	limit = math.isqrt(n)
	for i in range(3, limit + 1, 2):
		if n % i == 0:
			print("Đây không phải số nguyên tố")
	print("Đây là số nguyên tố")

# Bài số 28
def specialPlus():
	n = int(input("Nhập số nguyên n: "))
	k = int(input("Nhập số nguyên k: "))
	total = 0
	for i in range(n, 1):
		total += n * (n + k)
	print("Giá trị của tổng theo yêu cầu là: " + total)

# Bài số 29
def mathOfTriangle():
	a, b, c = map(int, input("Nhập 3 cạnh a, b, c bất kỳ của tam giác: ")).split()
	if (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2):
		print("Đây là một tam giác vuông")
	elif (a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or a**2 + c**2 < b**2):
		print("Đây là một tam giác tù")
	else:
		print("Đây là một tam giác nhọn thường")

# Bài số 30
def mathOfCombination():
	n = int(input("Nhập số nguyên dương bất kỳ: "))
	result = (n * (n - 1) * (n - 2)) / 6
	print("Kết quả của bài toàn sẽ là: " + result)

# Bài số 31
def mathOfPlus():
	n = int(input("Nhập số nguyên n: "))
	total = 0
	for i in range(n, 1):
		total += n
	print("Giá trị của tổng theo yêu cầu là: " + total)
# 1. Phân tích
#   - Input: Thông tin video: Tên tài khoản, Tiêu đề, Mô tả (str).
#            Nhóm hashtag: Chuỗi phân tách bằng dấu phẩy ','
#   - Output: Báo cáo phân tích chuỗi (độ dài, số từ, chữ hoa/thường).
#             Chuỗi kết quả sau khi được định dạng (thêm ký tự @, thay thế từ khóa)

# 2. Giải pháp:
#   - Loại bỏ khoảng trắng đầu/cuối: .strip()
#   - Viết hoa chữ cái đầu mỗi từ: .title()
#   - Chuyển toàn bộ thành chữ thường/chữ hoa: .lower() và .upper()
#   - Cắt chuỗi dựa trên dấu phẩy (Hashtag): .split(',')
#   - Kiểm tra chuỗi rỗng: Kiểm tra sau khi .strip() xem độ dài có bằng 0 hay không (len(s) == 0).
#   - Kiểm tra ký tự bắt đầu: .startswith('#')
#   - Đếm số lần xuất hiện của từ khóa: .count()
#   - Thay thế từ khóa: .replace()

# 3. Code hoàn chỉnh

account_name = ""
video_title = ""
video_description = ""
hashtag_list = []

print("=== HỆ THỐNG KIỂM DUYỆT NỘI DUNG VIDEO TIKTOK ===")

while True:
    print("\n" + "="*40)
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản ")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")
    print("="*40)
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            print("\n--- CHỨC NĂNG 1: NHẬP DỮ LIỆU & BÁO CÁO ---")
            
            raw_account = input("Nhập tên tài khoản: ")
            if not raw_account.strip():
                print("Lỗi: Tên tài khoản không được rỗng")
                continue
                
            raw_description = input("Nhập mô tả video: ")
            if not raw_description.strip():
                print("Lỗi: Mô tả video không được rỗng")
                continue
            
            raw_title = input("Nhập tiêu đề video: ")
            raw_hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            
            account_name = raw_account.strip()
            video_title = raw_title.strip()
            video_description = raw_description.strip()
            
            hashtag_list = [h.strip() for h in raw_hashtags.split(",") if h.strip()]
            
            print("\n BÁO CÁO THỐNG KÊ VIDEO:")
            print(f"+ Tên tài khoản (bỏ khoảng trắng): {account_name}")
            print(f"+ Tiêu đề (Chuẩn hóa Title Case): {video_title.title()}")
            print(f"+ Mô tả video: {video_description}")
            print(f"+ Độ dài mô tả video: {len(video_description)} ký tự")
            print(f"+ Số lượng từ trong mô tả: {len(video_description.split())} từ")
            print(f"+ Danh sách hashtag sau chuẩn hóa: {hashtag_list}")
            print(f"+ Số lượng hashtag: {len(hashtag_list)}")
            print(f"+ Mô tả viết thường: {video_description.lower()}")
            print(f"+ Mô tả viết hoa: {video_description.upper()}")

        case "2":
            print("\n--- CHỨC NĂNG 2: CHUẨN HÓA TÊN TÀI KHOẢN ---")
            if not account_name:
                print("Cảnh báo: Chưa có dữ liệu tài khoản. Vui lòng chạy Chức năng 1 trước.")
            else:
                print(f"Tên tài khoản ban đầu: \"{account_name}\"")
                normalized_account = f"@{account_name.lower()}"
                print(f"Tên tài khoản sau khi chuẩn hoá: \"{normalized_account}\"")

        case "3":
            print("\n--- CHỨC NĂNG 3: KIỂM TRA HASHTAG HỢP LỆ ---")
            new_hashtag = input("Nhập hashtag cần kiểm tra: ").strip()
            
            if len(new_hashtag) == 0:
                print("❌ Lỗi: Hashtag không được rỗng")
            elif not new_hashtag.startswith('#'):
                print("❌ Lỗi: Hashtag phải bắt đầu bằng ký tự #")
            elif " " in new_hashtag:
                print("❌ Lỗi: Hashtag không được chứa khoảng trắng")
            elif len(new_hashtag) < 2:
                print("❌ Lỗi: Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
            else:
                content_after_hash = new_hashtag[1:]
                if content_after_hash.replace("_", "a").isalnum():
                    print("✅ Hashtag hợp lệ")
                    hashtag_list.append(new_hashtag)
                    print(f"Danh sách hashtag hiện tại của video: {hashtag_list}")
                else:
                    print("Lỗi: Hashtag chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #")

        case "4":
            print("\n--- CHỨC NĂNG 4: TÌM KIẾM VÀ THAY THẾ TỪ KHÓA ---")
            if not video_description:
                print("Cảnh báo: Chưa có dữ liệu mô tả video. Vui lòng chạy Chức năng 1 trước.")
            else:
                search_word = input("Nhập từ khóa cần tìm: ")
                replace_word = input("Nhập từ khóa thay thế: ")
                
                if search_word in video_description:
                    count_appear = video_description.count(search_word)
                    video_description = video_description.replace(search_word, replace_word)
                    print("Tìm thấy từ khóa và đã thay thế thành công!")
                    print(f"-> Mô tả sau khi thay thế: {video_description}")
                    print(f"-> Số lần từ khóa xuất hiện: {count_appear} lần")
                else:
                    print(f"Không tìm thấy từ khóa '{search_word}' trong mô tả video.")

        case "5":
            print("\nThoát chương trình. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại số từ 1 đến 5.")
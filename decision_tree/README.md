**Dự đoán điểm tổng kết môn học của sinh viên** </br>

Đường dẫn model và tập dữ liệu trên drive: https://drive.google.com/drive/folders/1voQLw2kaWqxO3QautDDN1XfwKYbIdUl_?usp=sharing </br>

**Hướng dẫn**:</br>
*Chạy code từ đầu và xây dựng model:* chạy tuần tự (Ctrl + F9) </br>
Chương trình sẽ thực hiện các đoạn code sau: </br>
- Cài đặt pyspark
- Thêm thư viện và các module
- Kết nối với google drive
- Đọc file dữ liệu
- Sort theo mã môn học
- Chuyển đổi sang định dạng LabeledPoint
- Xây dựng tập hợp các cây quyết định
- Lưu các model về gdrive
*Chạy code dự đoán điểm tổng kết:* </br>
- Khởi tạo hàm dự đoán
- Đọc hàng dữ liệu chứa các thông tin đã biết về sinh viên đó
- Gọi hàm dự đoán
  + Nếu là lần đầu gọi model mã môn học thì chương trình sẽ load model từ gdrive
  + Ngược lại sẽ đưa ra dự đoán

**Kết quả đạt được**:</br>
Hiệu quả xây dựng model của mỗi tập dữ liệu (50MB) chứa 500000 đối tượng là khoảng 45 phút.
Kết quả dự đoán với độ chính xác cao.

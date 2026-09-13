# 📱 Python Tkinter Calculator - Máy Tính Cầm Tay

Một ứng dụng máy tính cầm tay (Calculator) hoàn chỉnh được xây dựng bằng ngôn ngữ **Python** và thư viện đồ họa **Tkinter**. 

Dự án áp dụng chuẩn thiết kế **Module hóa (Separation of Concerns)** — tách biệt 100% giữa **Giao diện (UI)** và **Não bộ tính toán (Logic)**, giúp mã nguồn sạch sẽ, dễ bảo trì và dễ mở rộng.

---

## 📸 Giao diện ứng dụng

```
+-----------------------------------+
| [                             128] |  <- Màn hình Entry (căn phải, ipady=6)
+---------+---------+---------+-----+
|    C    |   DEL   |    %    |  /  |  <- Hàng 1 (Đỏ, Xám, Cam)
+---------+---------+---------+-----+
|    7    |    8    |    9    |  *  |  <- Hàng 2 (Trắng, Cam)
+---------+---------+---------+-----+
|    4    |    5    |    6    |  -  |  <- Hàng 3 (Trắng, Cam)
+---------+---------+---------+-----+
|    1    |    2    |    3    |  +  |  <- Hàng 4 (Trắng, Cam)
+---------+---------+---------+-----+
|        0 (rộng x2) |    .    |  =  |  <- Hàng 5 (Trắng, Cam)
+-------------------+---------+-----+
```

---

## ✨ Tính năng nổi bật

- ➕ **Tính toán đầy đủ**: Cộng, trừ, nhân, chia, số thập phân và tính phần trăm (`%`).
- 🧹 **Xóa linh hoạt**: 
  - Nút **`C`** (Clear): Xóa toàn bộ màn hình.
  - Nút **`DEL`** (Backspace): Xóa lùi từng ký tự cuối cùng.
- 🎨 **Phân loại màu sắc trực quan**:
  - Phép tính (`/`, `*`, `-`, `+`, `=`): **Màu cam nổi bật** (`#ff9f0a`).
  - Xóa hết (`C`): **Màu đỏ cảnh báo** (`red`).
  - Chức năng (`DEL`, `%`): **Màu xám nhạt** (`#e0e0e0`).
  - Bàn phím số (`0-9`, `.`): **Màu trắng thanh lịch** (`white`).
- 📐 **Bố cục Responsive Grid**: Tự động co giãn đều các nút bấm khi kéo dãn cửa sổ (`weight=1`, `sticky="nsew"`).
- 🛡️ **Bảo vệ ứng dụng (Crash-proof)**: Bọc khối `try...except` chống văng ứng dụng khi người dùng nhập sai cú pháp toán học hoặc chia cho 0.

---

## 📂 Cấu trúc thư mục dự án

```
lap_trinh_Tkinter/
│
├── calculator_logic.py      # Module não bộ (Xử lý chuỗi & tính toán toán học thuần túy)
├── caculator_interface.py   # Module giao diện (Vẽ cửa sổ, nút bấm & bắt sự kiện Tkinter)
└── README.md                # Tài liệu hướng dẫn chi tiết dự án
```

---

## 🚀 Hướng dẫn cài đặt & Chạy ứng dụng

### 1. Yêu cầu hệ thống:
- Đã cài đặt **Python 3.x** trên máy tính (Tkinter là thư viện có sẵn kèm theo Python, không cần cài thêm).

### 2. Khởi chạy:
Mở terminal hoặc Command Prompt tại thư mục dự án và gõ lệnh:

```bash
python caculator_interface.py
```

---

## 📖 GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE

---

### PHẦN 1: Module Não Bộ - `calculator_logic.py`

File này chịu trách nhiệm xử lý nghiệp vụ toán học, độc lập hoàn toàn với Tkinter.

```python
# calculator_logic.py

def cal_expression(exp: str) -> str:
    """
    exp:tên tham số (tên biến đầu vào tự đặt)
    str--> kiểu dữ liêu của tham số đó  (báo hiệu rằng giá trị truyền vào phải là kiểu Chuỗi ký tự - String.)
    Hàm nhận vào một chuỗi biểu thức toán học (ví dụ: '10+5*2')
    và trả về kết quả dưới dạng chuỗi ('20').
    """
    try:
        # Thay thế ký tự '%' thành phép chia cho 100 để máy hiểu đúng toán học
        replace = exp.replace('%', '/100')
        
        # eval(): Hàm tích hợp sẵn của Python, tự động biên dịch và tính biểu thức số học
        result = eval(replace) 
        
        return str(result)
    except Exception:
        # Nếu biểu thức sai cú pháp (như "5++*3") hoặc chia cho 0 ("5/0"), trả về "Lỗi"
        return "Lỗi"


def remove_last_character(current_text: str) -> str:
    """
    Hàm xử lý xóa ký tự cuối cùng (chức năng nút DEL).
    """
    # if current_text: kiểm tra chuỗi có ký tự hay không (tránh lỗi khi màn hình đang rỗng)
    if current_text: # có nghĩa là current_text != " "  biến nó khác rỗng 
        # Cắt chuỗi bằng kỹ thuật Slicing: [:-1] nghĩa là lấy từ đầu đến sát ký tự cuối cùng
        return current_text[:-1]   
    return ""
```

---

### PHẦN 2: Module Giao Diện & Điều Phối - `caculator_interface.py`

#### 1. Khởi tạo cửa sổ chính & Nhập module
```python
import tkinter as tk  #lấy thư viện ra và tự đặt tên cho nó 



from calculator_logic import cal_expression, remove_last_character # import module (file chứa hàm xử lý logic và import các hàm xử lý trong file đó ra )

# Tạo cửa sổ ứng dụng
root = tk.Tk() 
"""
  đặt tên cho của số hiện thị là root (gốC) tkinter sẽ hoạt động theo mô thinh phân câp bắt đầu từ root(gốc) và trong root thiết lập các chức năng giao diện như nút bấn (button),nhãn (label) ,ô nhập liệu( Entry) vvvv....


"""
root.title("Caculator")       # Đặt tiêu đề thanh cửa sổ
root.geometry("300x400")      # Kích thước mặc định rộng 300px, cao 400px
```

#### 2. Màn hình hiển thị kết quả (`Entry`)
```python
Entry = tk.Entry(
    root,
    font=("Segoe UI", 14),    # kiểu  font chữ và kích cỡ của nó 
    justify="right",          # Căn chữ số về phía mép phải như máy tính thật
    bd=5                      # Độ dày đường viền (border width)
)
Entry.grid(
    row=0, column=0, 
    columnspan=4,             # Chiếm trọn 4 cột trên cùng của bàn phím
    padx=5, pady=10, 
    sticky="ew",              # Dãn căng sang 2 hướng Đông - Tây (trái - phải)
    ipady=6                   # Internal Padding Y: Làm chiều cao ô Entry dày lên 6px ở trên & dưới
)
```

#### 3. Hàm điều phối sự kiện (`on_click`)
Đóng vai trò như "ngã tư điều phối giao thông", phân loại hành động dựa trên nút bấm:
```python

Dù máy tính có 20 nút bấm khác nhau, toàn bộ logic chỉ quy về **4 trường hợp duy nhất**:

```
                              [ NGƯỜI DÙNG BẤM PHÍM ]
                                         │
         ┌──────────────────┬────────────┴────────────┬──────────────────┐
         ▼                  ▼                         ▼                  ▼
    Nhóm 1: 'C'        Nhóm 2: 'DEL'               Nhóm 3: '='        Nhóm 4: Các nút còn lại
   (Clear All)         (Backspace)              (Calculate)      (0-9, +, -, *, /, ., %)
         │                  │                         │                  │
         ▼                  ▼                         ▼                  ▼
   Xóa sạch màn       Cắt bỏ 1 ký tự             Tính biểu thức      Nối thêm ký tự
   hình Entry         ở cuối chuỗi               bằng eval()         vào cuối Entry
```



def on_click(char):
    if char == "C":
        # Bấm C: Xóa sạch toàn bộ từ vị trí 0 đến END (từ đầu đến cuôi (0,đến cuối -> (tk.END ))
        Entry.delete(0, tk.END)

    elif char == "DEL":
        # Bấm DEL: Lấy chuỗi hiện tại bằng Entry.get(), đưa qua hàm cắt rồi cập nhật lại
        text_new = remove_last_character(Entry.get())
        Entry.delete(0, tk.END)  #xóa toàn bộ chuối có trên màn hình để thêm vào chỗi mới
        Entry.insert(0, text_new)  # thêm chỗi mới

    elif char == "=":
        # Bấm =: Đưa biểu thức qua hàm cal_expression để tính và hiển thị
        result = cal_expression(Entry.get())
        Entry.delete(0, tk.END)  #xóa toàn bộ chuối có trên màn hình để thêm kết quả hàm cal_expression trả về
        Entry.insert(0, result)  # thêm chỗi mới

    else:
        # Nếu màn hình đang báo lỗi từ trước thì xóa chữ "Lỗi" đi trước khi nhập số mới
        if Entry.get() == "Lỗi" or Entry.get() == "Error":
            Entry.delete(0, tk.END)

        # Nối tiếp ký tự số hoặc phép tính vừa bấm vào sau cùng của chuỗi đang hiển thị trên màn hình 
        Entry.insert(tk.END, char)
```

#### 4. Cấu hình tỷ lệ co dãn (`weight`)
Giúp giao diện không bị co cụm lại một góc khi người dùng dùng chuột kéo to cửa sổ:
```python
# Cho 5 hàng nút (hàng 1 đến hàng 5) dãn đều theo trục dọc
for r in range(1, 6):
    root.rowconfigure(r, weight=1)

# Cho 4 cột (cột 0 đến cột 3) dãn đều theo trục ngang
for c in range(4):
    root.columnconfigure(c, weight=1)
```

#### 5. Sinh lưới nút bấm tự động & Tô màu thông minh (Hàng 1 đến 4)
Thay vì tạo 16 nút thủ công, ứng dụng dùng ma trận 2 chiều (`keys`) duyệt bằng 2 vòng `for` lồng nhau:
```python
keys = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+']
]

for row_idx, row_value in enumerate(keys):  #dùng enumerate để truy cập được cả chỉ số(index) và giá trị(value) trong mảng keys      
    """row_idx là chỉ số của hàng đầu tiên  mang chỉ số 0  ( row_idx cũng là chỉ số hàng dùng để hiện thị button  )
       ví dụ row_value là giá trị của chỉ số hàng đó  ['C', 'DEL', '%', '/']
       vd: row_idx =0 thì -> row_value là 
    """
    
    for column_idx, column_value in enumerate(row_value):
        """
        column_idx --> chỉ số của kí tự trong  row_value (ví dụ: 'C'-->0,'DEL'--->1.....)
        column_value---> giá trị tương ứng với chỉ số cột đó vd  trong  row_value= ['C', 'DEL', '%', '/'] ->column_idx=0 thì column_value='C'
        """

        # Logic phân loại màu sắc cho từng loại nút bấm:
        if column_value in ['/', '*', '-', '+']:
            btn_bg = "#ff9f0a"   # Cam cho phép tính
            btn_fg = "white"
        elif column_value in ['C']:
            btn_bg = "red"       # Đỏ cảnh báo cho nút xóa hết
            btn_fg = "white"
        elif column_value in ['DEL', '%']:
            btn_bg = "#e0e0e0"   # Xám nhạt cho nút phụ
            btn_fg = "black"
        else:
            btn_bg = "white"     # Trắng cho các phím số
            btn_fg = "black"

#thiết lập các nút để đưa vào cửa số root 
        buttons = tk.Button(
            root,
            text=column_value,
            font=("Segoe UI", 14, "bold"),
            width=5, height=2,
            bg=btn_bg, fg=btn_fg,
            # Bẫy Late Binding: Dùng 't=column_value' để đóng băng giá trị của từng nút
            command=lambda t=column_value: on_click(t)
        )
        buttons.grid(row=row_idx + 1, column=column_idx, padx=5, pady=5, sticky="nsew")
```

#### 6. Hàng số 5 đặc biệt (Phím `0`, `.`, `=`)
Các phím có kích thước không đồng đều được định nghĩa riêng:
```python
# Phím 0: Chiếm 2 cột (columnspan=2) để bấm tiện hơn
button_0 = tk.Button(
    root, text="0", font=("Segoe UI", 14, "bold"),
    width=5, height=2, bg="white",
    command=lambda: on_click("0")
)
button_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Phím dấu chấm '.'
button_dot = tk.Button(
    root, text=".", font=("Segoe UI", 14, "bold"),
    width=5, height=2, bg="white",
    command=lambda: on_click(".")
)
button_dot.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

# Phím bằng '=' (Màu cam đồng bộ)
button_equal = tk.Button(
    root, text="=", font=("Segoe UI", 14, "bold"),
    width=5, height=2, bg="#ff9f0a", fg="white",
    command=lambda: on_click("=")
)
button_equal.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

# Vòng lặp giữ cửa sổ chạy liên tục
root.mainloop()
```

---

## 🎯 Các bài học kỹ thuật cốt lõi rút ra từ dự án

1. **Nguyên lý Đóng gói Module (SoC)**: Tách logic nghiệp vụ sang module riêng giúp giao diện gọn nhẹ và dễ viết kiểm thử độc lập.
2. **Kỹ thuật Cắt chuỗi (`Slicing`)**: `current_text[:-1]` là giải pháp ngắn gọn và tối ưu nhất để triển khai nút xóa lùi (Backspace) trong Python.
3. **Quản lý lưới nâng cao (`Grid Layout`)**: Sự phối hợp giữa `columnspan`, `sticky="nsew"` và cấu hình `weight` của `columnconfigure`/`rowconfigure` tạo nên giao diện co giãn hoàn hảo.
4. **Tránh bẫy Ràng buộc muộn (`Late Binding`)**: Khi gắn `lambda` vào vòng lặp `for`, bắt buộc phải gán tham số mặc định `lambda t=biến: ...` để tránh việc các nút nhận nhầm giá trị của vòng lặp cuối.


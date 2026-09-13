#ham tinh toan bieu thuc toan hoc 
#thay thế kí tự % thành phép chia 100
def cal_expression(exp:str) -> str:
    try:
        replace=exp.replace('%','/100') #kiểm tra Entry.get() -->(kí tự/dữ liệu trên màn hình --->vd :'a+b') có kí tự '%' không , nếu có thì đổi thành 'chia cho 100'
        result=eval(replace) #hàm **`eval()`** có khả năng nhận một chuỗi toán học và tự động tính toán ra kết quả:
        return str(result)
    except Exception:
        return "Error"

#ham xoa ki tu khi bam xoa

def remove_last_character(current_text: str) ->str:
    if current_text: #current_text !="" khác rỗng , điều kiện này là để xử lý trong trường  hợp màn hình entry đã rỗng mà user vẫn bấm xóa thì không có hiện tượng gì xảy ra cả 
        return current_text[:-1]   #bỏ kí tự cuối cùng , kiểu cắt chỗi trong python slicing
    return ""
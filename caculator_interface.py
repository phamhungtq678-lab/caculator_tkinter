import tkinter as tk
import customtkinter as ctk
from calculator_logic import  cal_expression,remove_last_character

root=tk.Tk()
root.title("Caculator")
root.geometry("300x400")

#entry --> có căn phải 

Entry=tk.Entry(
    root,
    font=("Segoe UI",14),
    justify="right",
    bd=5
)
Entry.grid(row=0,column=0,columnspan=4,padx=5,pady=10,sticky="ew",ipady=6)
           #Internal Padding Y (Khoảng đệm bên trong theo trục dọc - trục Y).




#hàm điêu phối sự kiện 
def on_click(char):
    if char=="C":
        Entry.delete(0,tk.END)

    elif char=="DEL":
        text_new=remove_last_character(Entry.get()) #chuyền kí tự đang ở trên ô entry vào hàm để cắt
        Entry.delete(0,tk.END)
        Entry.insert(0,text_new)  


    elif char == "=":
        result=cal_expression(Entry.get())
        Entry.delete(0,tk.END)
        Entry.insert(0,result)  


    else:
        if Entry.get()=="Error":
            Entry.delete(0,tk.END)

        Entry.insert(tk.END,char)






#weight=1 kéo dãn

for r in range(1,6):
    root.rowconfigure(r,weight=1)


for c in range(4):
    root.columnconfigure(c,weight=1)
    
#buttons

keys = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+']
]


for row_idx,row_value in enumerate(keys):
    for column_idx,column_value in enumerate(row_value):

        #phân loại màu cho bàn cho bàn phím 
        if column_value in ['/','*','-', '+']:
            btn_bg="#ff9f0a"
            btn_fg="white"

        elif column_value in ['C']:
            btn_bg="red"
            btn_fg="white"

        elif column_value in ['DEL', '%']:
            btn_bg = "#e0e0e0"   # Màu xám nhạt cho nút xóa
            btn_fg = "black"
        else:
            btn_bg = "white"     # Màu trắng cho các nút số
            btn_fg = "black"


        buttons=tk.Button(
            root,
            text=column_value,
            font=("Segoe UI",14,"bold"),
            width=5,
            height=2,
            command=lambda t=column_value : on_click(t),
            #Trong Python, có một quy tắc: Giá trị mặc định của tham số hàm (t = ...) 
            # sẽ được tính toán và ĐÓNG BĂNG NGAY LẬP TỨC tại thời điểm tạo ra hàm
            #Khi vòng lặp duyệt qua chữ '7': t được chụp ảnh và đóng băng ngay thành: t = '7'.
            bg=btn_bg,
            fg=btn_fg
            
        )
        buttons.grid(row=row_idx+1,column=column_idx,padx=5,pady=5,sticky="nsew")




#tạo riêng hàng 5 có columnspan=2 cho số O

button_0=tk.Button(
    root,
    text="0",
    font=("Segoe UI",14,"bold"),
    width=5,
    height=2,
    command= lambda : on_click("0"),
)
button_0.grid(row=5,column=0,columnspan=2,padx=5,pady=5,sticky="nsew")
            
button_dot=tk.Button(
    root,
    text=".",
    font=("Segoe UI",14,"bold"),
    width=5,
    height=2,
    command= lambda : on_click("."),
)
button_dot.grid(row=5,column=2,padx=5,pady=5,sticky="nsew")



button_equal=tk.Button(
    root,
    text="=",
    font=("Segoe UI",14,"bold"),
    width=5,
    height=2,
    command= lambda : on_click("="),
    bg="#ff9f0a",
    fg="white"
)
button_equal.grid(row=5,column=3,padx=5,pady=5,sticky="nsew")






root.mainloop()


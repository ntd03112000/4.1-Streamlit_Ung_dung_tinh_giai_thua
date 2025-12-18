# Edit Cònfigurations --> streamlit.exe --> ở phần Run ngay tại script
#                                        --> C:/Users/dung/Desktop/AIO/.venv/Scripts/streamlit.exe
#                                        --> dòng dưới run "4.1 Streamlit_Ung_dung_tinh_giai_thua.py"(tức tên file python hiện tại)
# chuyển qua streamlit.exe thay vì Current File
# NHẤN SHIFT + F10 ĐỂ CHẠY
# https://41-appungdungtinhgiaithua-cgfp5numhkr4bsxvvhcqjz.streamlit.app/
import io
import os.path

from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Lấy ra danh sách tên đăng nhập được phép truy cập từ file .txt
def load_user():
    try:
        if os.path.exists("4.1 Streamlit_Ung_dung_tinh_giai_thua user.txt"):
            with open("4.1 Streamlit_Ung_dung_tinh_giai_thua user.txt", "r", encoding="utf-8") as f:
                user = [line.strip() for line in f.read().splitlines() if line.strip()]
                return user
    except Exception as e:
        st.write(f"Lỗi: {e}")
        return []
    return []

# Trang ban đầu khi mở web để client đăng nhập
def Trang_dang_nhap():
    st.title("Trang đăng nhập")
    user = load_user()
    # Yêu cầu nhập tên người dùng
    user_name = st.text_input("Tên đăng nhập:")
    if st.button("Đăng nhập"):
        if user_name in user:
            st.session_state.da_dang_nhap = True
            st.session_state.user_name = user_name
            st.rerun()
        else:
            st.session_state.da_dang_nhap = False
            st.session_state.user_name = user_name
            st.rerun()

# Sau khi đăng nhập sai, trang này sẽ hiện ra yêu cầu đăng nhập lại
def Trang_yeu_cau_dang_nhap_lai():
    st.title(f"Xin chào {st.session_state.user_name}!")
    st.write("Tên đăng nhập của bạn đã sai. Vui lòng đăng nhập lại!")
    if st.button("Đăng nhập lại"):
        st.session_state.da_dang_nhap = False
        st.session_state.user_name = ""
        st.rerun()

# Quá trình tính giai thừa
def Tinh_giai_thua(number):
    if number != 0 or number == 1:
        return number * Tinh_giai_thua(number - 1)
    else:
        return 1


def main():
    # Tạo key: value là "da_dang_nhap": False trong dictionary st.session_state
    if "da_dang_nhap" not in st.session_state:
        st.session_state.da_dang_nhap = False

    # Tạo key: value là "user_name": "" trong dictionary st.session_state
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    # Trường hợp đã đăng nhập thành công
    if st.session_state.da_dang_nhap == True:
        page_tinh_giai_thua()

    #  Trường hợp đăng nhập với tên sai
    elif st.session_state.da_dang_nhap == False and st.session_state.user_name != "":
        Trang_yeu_cau_dang_nhap_lai()

    # Trường hợp ban đầu chưa đăng nhập gì cả
    else:
        Trang_dang_nhap()

# Page tính giai thừa hiện ra khi đăng nhập thành công
def page_tinh_giai_thua():
    st.title("Tính giai thừa")
    st.write(f"Xin chào {st.session_state.user_name}!")
    number = st.number_input("Nhập số:", min_value=1, step=1)
    Ket_qua = Tinh_giai_thua(number)
    if st.button("Kết quả"):
        st.write(f"Kết quả với phép tính {number}! là: ", Ket_qua)
    if st.button("Quay lại trang ban đầu"):
        st.session_state.da_dang_nhap = False
        st.session_state.user_name = ""
        st.rerun()


if __name__ == "__main__":
    main()





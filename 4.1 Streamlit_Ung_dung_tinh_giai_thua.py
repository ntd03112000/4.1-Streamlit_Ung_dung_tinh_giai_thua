# Edit Configurations --> streamlit.exe --> ở phần Run ngay tại script
#                                        --> C:/Users/dung/Desktop/AIO/.venv/Scripts/streamlit.exe
#                                        --> dòng dưới run "4.1 Streamlit_Ung_dung_tinh_giai_thua.py"(tức tên file python hiện tại)
# chuyển qua streamlit.exe thay vì Current File
# NHẤN SHIFT + F10 ĐỂ CHẠY
import io
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from numpy.ma.core import min_val


def Tinh_giai_thua(number):
    if number != 0 or number ==1:
        return number * Tinh_giai_thua(number - 1)
    else:
        return 1

st.title("Tính giai thừa")
number = st.number_input("Nhập số:", min_value=1, step=1)
Ket_qua = Tinh_giai_thua(number)
if st.button("Kết quả"):
    st.write(f"Kết quả với phép tính {number}! là: ", Ket_qua)


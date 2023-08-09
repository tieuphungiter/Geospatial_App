import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/tieuphungiter/Geospatial_App>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://upload.wikimedia.org/wikipedia/commons/7/7f/Rotating_earth_animated_transparent.gif?20201022124448"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown("""
    Đây là dự án mẫu minh họa các ứng dụng web tương tác khác nhau được tạo bằng streamlit và thư viện leafmap.
    """)

st.header("Hướng dẫn")

markdown = """
0. Để chạy chương trình: streamlit run streamlit_app.py
1. Tùy chỉnh thanh bên bằng cách thay đổi văn bản và biểu trưng của thanh bên trong mỗi tệp Python.
2. Tìm biểu tượng cảm xúc yêu thích của bạn từ https://emojipedia.org.
3. Thêm ứng dụng mới vào thư mục pages/ có biểu tượng cảm xúc trong tên tệp, ví dụ: 1_🚀_Chart.py.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

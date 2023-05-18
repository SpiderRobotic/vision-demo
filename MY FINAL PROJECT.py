import streamlit as st
#from PIL import Image

page_bg_img = """
<style> 
[data-testid="stAppViewContainer"]{
background-image: url(https://img.freepik.com/free-vector/realistic-black-shimmer-background_23-2150083458.jpg?w=996&t=st=1684378196~exp=1684378796~hmac=b146a27d331dd8d6e6d56ffe49d08c11bb49b6f3d6f1dff7ec5c2ca48819cf70);
background-size: cover;}
[data-testid = "stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
"""

st.set_page_config(
    page_title="BÁO CÁO CUỐI KÌ",
    page_icon="▶",
)


#lottie_coding = load_lottieur1("https://assets5.lottiefiles.com/packages/lf20_4kx2q32n.json")
#img_contact_form = Image.open("images/huy1.png")


# Define CSS styling for the header text
header_style = """
    <style>
        .header-text {
            color: orange;
        }
    </style>
"""

# Display the header text with the defined CSS styling
st.markdown(header_style, unsafe_allow_html=True)
st.markdown('<h1 class="header-text">BÀI BÁO CÁO CUỐI KÌ</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown(page_bg_img, unsafe_allow_html=True)

with st.container(): 
    st.write("---")
    st.markdown(
        """
        ### Môn học: Thị Giác Máy
        ### GVHD: Ts. Trần Tiến Đức
        ### SVTH: 
        ###       1. Tăng Hoàng Huy - 20146342
        ###       2. Nguyễn Đình Trọng - 20146445
        """
    )


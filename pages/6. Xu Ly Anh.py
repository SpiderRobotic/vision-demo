import streamlit as st
import sys
import cv2
import numpy as np
from PIL import Image
import Chapter3 as c3
import Chapter4 as c4
import Chapter05 as c5
import Chapter9 as c9

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
    page_title="Thuật toán xử lý ảnh 🎨",
    page_icon="🏕",
)
st.markdown("<h2 style = 'text-align: center; font-size: 40px; font-family: comic sans ms, cursive; color: #008080;'>Thuật toán xử lý ảnh 🎨 </h2>", unsafe_allow_html=True)
st.sidebar.header(" Mục xử lý ảnh 🏕 ")
st.markdown(page_bg_img, unsafe_allow_html=True)

def imgin_header():
    imgin_Title = '<p style="font-family: Courier; color: #2e8b57; font-size: 24px;"><b>Ảnh đã chọn để xử lý ảnh</b></p>'
    st.markdown(imgin_Title, unsafe_allow_html=True)
def imgout_header():
    imgout_Title = '<p style="font-family: Courier; color: #191970; font-size: 24px;"><b>Ảnh sau khi được xử lý ảnh ✅</b></p>'
    st.markdown(imgout_Title, unsafe_allow_html=True)
def download_info():
    download_notice = '<p style="font-family: monospace; font-size: 18px; color: #006400;"><i>Nhấp chuột phải vào ảnh để tải xuống.</i></p>'
    st.markdown(download_notice, unsafe_allow_html=True) 
    

option = st.sidebar.selectbox('CHỌN CHƯƠNG XỬ LÝ ẢNH 📋 ', ['--Chọn chương--', 'Chương 3 🌻', 'Chương 4 🌻','Chương 5 🌻', 'Chương 9 🌻'])
if option == 'Chương 3 🌻':
    img_upload = st.file_uploader('🗂 Chọn file ảnh', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
            global imgin
            #địa chỉ file ảnh trong desktop G:\ProjectCuoiKy\ProjectCuoiKy\ProcessingImage\Chuong3\\
            filepath = r'C:\machine_vision\ProcessingImage\Chuong3\\' + img_upload.name
            imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            imgin_header()
            st.image(imgin)

            c3_function = st.sidebar.selectbox('Hãy chọn phương pháp xử lý ảnh', [
                '--chọn phương pháp--','Negative', 'Logarit', 'Power', 'PieceWiseLinear', 'Histogram',
                'HistogramEqualization', 'LocalHistogram', 'HistogramStatistics',
                'SmoothingGauss', 'Smoothing', 'MedianFilter', 'Sharpen', 'UnSharpMasking', 'Gradient'])
            # Negative(hàm làm ấm ảnh, Trắng thành đen, đen thành trắng)
            if c3_function == 'Negative':
                global imgout
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Negative(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Negative: Hàm làm ấm ảnh, Trắng thành đen, đen thành trắng</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Logarit (Hàm xử lý ảnh bằng phương pháp logarit. kết quả hàm logarit: sáng ít thành sáng nhiều, đen nhiều thành đen ít)
            elif c3_function == 'Logarit':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Logarit(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Logarit:Hàm xử lý ảnh bằng phương pháp logarit. Kết quả hàm logarit:Sáng ít thành sáng nhiều, đen nhiều thành đen ít.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Power(Hàm xử lý ảnh bằng phương pháp lũy thừa ảnh. kết quả hàm Power: làm ảnh trở nên tối hơn, hoặc tối hơn)

            elif c3_function == 'Power':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Power(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Power: Hàm xử lý ảnh bằng phương pháp lũy thừa ảnh. kết quả hàm Power: làm ảnh trở nên tối hơn, hoặc tối hơn</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # PieceWiseLinear(Hàm xử lý ảnh bằng phương pháp PieceWise. kết quả hàm PieceWiseLinear: Kéo dài độ tương phản, phạm vi mức độ cường độ làm sáng hơn)
            elif c3_function == 'PieceWiseLinear':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.PiecewiseLinear(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>PieceWiseLinear: Hàm xử lý ảnh bằng phương pháp PieceWise. kết quả hàm PieceWiseLinear: Kéo dài độ tương phản, phạm vi mức độ cường độ làm sáng hơn</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Histogram(tạo ra biểu đồ, hiển thị tần suất theo dnajg cột theo dữ liệu tương ứng)
            elif c3_function == 'Histogram':
                imgout = np.zeros((imgin.shape[0], 256, 3), np.uint8) + 255
                c3.Histogram(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Histogram: Tạo ra biểu đồ, hiển thị tần suất theo dạng cột theo dữ liệu tương ứng</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramEqualization(làm cho ảnh đẹp hơn)            
            elif c3_function == 'HistogramEqualization':
                imgout = np.zeros(imgin.shape, np.uint8)
                cv2.equalizeHist(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>HistogramEqualization: Làm cho ảnh đẹp hơn</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # LocalHistogram(làm rõ 1 vùng ảnh)
            elif c3_function == 'LocalHistogram':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.LocalHistogram(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #0064000000; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>LocalHistogram: Làm rõ 1 vùng ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramStatistics(rõ nét 1 số vùng trong ảnh)
            elif c3_function == 'HistogramStatistics':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.HistogramStatistics(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>HistogramStatistics: Rõ nét 1 số vùng trong ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # SmoothingGauss(làm nhòe ảnh làm trơn ảnh tương tự như smooothing nhưng nhòe hơn)
            elif c3_function == 'SmoothingGauss':
                imgout = c3.SmoothingGauss(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>SmoothingGauss: Làm nhòe ảnh làm trơn ảnh tương tự như smooothing nhưng nhòe hơn</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Smoothing(làm nhòe ảnh)
            elif c3_function == 'Smoothing':
                imgout = c3.Smoothing(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Smoothing:Làm nhòe ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # MedianFilter(lọc nhiễu ảnh)
            elif c3_function == 'MedianFilter':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.MedianFilter(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>MedianFilter: Lọc nhiễu ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Sharpen(làm nét ảnh, làm nhọn các góc ảnh)
            elif c3_function == 'Sharpen':
                imgout = c3.Sharpen(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Sharpen: Làm nét ảnh, làm nhọn các góc ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # UnSharpMasking(làm nét ảnh)
            elif c3_function == 'UnSharpMasking':
                imgout = c3.UnSharpMasking(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>UnSharpMasking: Làm nét ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Gradient(tách biên ảnh)
            elif c3_function == 'Gradient':
                imgout = c3.Gradient(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Gradient: Tách biên ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            else:
                st.image('doi.gif', caption='Waiting...')
                state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>None</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 4 🌻':
    img_upload = st.file_uploader('🗂 Chọn file ảnh', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = r'C:\machine_vision\ProcessingImage\Chuong4\\' + img_upload.name #địa chỉ file ảnh trong desktop G:\ProjectCuoiKy\ProjectCuoiKy\ProcessingImage\Chuong4\\
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c4_function = st.sidebar.selectbox('Hãy chọn phương pháp xử lý ảnh', [
            '--chọn phương pháp--','Spectrum', 'FrequencyFilter', 'DrawFilter', 'RemoveNoise'])
        # Spectrum(xử lý quang phổ bằng các công thức tần số sóng điện từ, ánh sáng, điểm ảnh)
        if c4_function == 'Spectrum':
            imgout = c4.Spectrum(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Spectrum: Xử lý quang phổ bằng các công thức tần số sóng điện từ, ánh sáng, điểm ảnh</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # FrequencyFilter(bộ lọc cho tín hiệu có tần số thấp tần số cắt đã chọn, làm suy giảm tần số )
        elif c4_function == 'FrequencyFilter':
            imgout = c4.FrequencyFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>FrequencyFilter:Bộ lọc cho tín hiệu có tần số thấp tần số cắt đã chọn, làm suy giảm tần số</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # DrawFilter(lọc ảnh cơ bản)
        elif c4_function == 'DrawFilter':
            imgout = c4.DrawFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>DrawFilter: Lọc ảnh cơ bản</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # RemoveMoire(xóa điểm nhiễu đi)
        elif c4_function == 'RemoveNoise':
            imgout = c4.RemoveNoise(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>RemoveNoise: Xóa điểm nhiễu đi </i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('doi.gif', caption='Waiting...')
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 5 🌻':
    img_upload = st.file_uploader('🗂 Chọn file ảnh', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = r'C:\machine_vision\ProcessingImage\Chuong5\\' + img_upload.name  #địa chỉ file ảnh trong desktop G:\ProjectCuoiKy\ProjectCuoiKy\ProcessingImage\Chuong5\\
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c5_function = st.sidebar.selectbox('Hãy chọn phương pháp xử lý ảnh', [
            '--chọn phương pháp--', 'CreateMotionNoise', 'DenoiseMotion'])
    
        # CreateMotionNoise (tạo chuyển động nhiễu)
        if c5_function == 'CreateMotionNoise':
            imgout = c5.CreateMotionNoise(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>CreateMotionNoise: Tạo chuyển động nhiễu</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # DenoiseMotion  (khử nhiễu, xóa các chuyển động nhiễu)
        elif c5_function == 'DenoiseMotion':
            imgout = c5.DenoiseMotion(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>DenoiseMotion: Khử nhiễu, xóa các chuyển động nhiễu</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('doi.gif', caption='Wating...')
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)


elif option == 'Chương 9 🌻':
    img_upload = st.file_uploader('🗂 Chọn file ảnh', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = r'C:\machine_vision\ProcessingImage\Chuong9\\' + img_upload.name #địa chỉ file ảnh trong desktop G:\ProjectCuoiKy\ProjectCuoiKy\ProcessingImage\Chuong9\\
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c9_function = st.sidebar.selectbox('Hãy chọn phương pháp xử lý ảnh', [
            '--chọn phương pháp--','Erosion', 'Dilation', 'OpeningClosing', 'Boundary', 'HoleFill', 
            'MyConnectedComponent', 'CountRice'])
        # Erosion( làm bào mòn ảnh)
        if c9_function == 'Erosion':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Erosion(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Erosion: Làm bào mòn ảnh</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Dilation (làm giản nở chữ cái , làm mập chữ)
        elif c9_function == 'Dilation':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Dilation(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Dilation: Làm giản nở chữ cái , làm mập chữ</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # OpeningClosing(xóa nhiễu ảnh)
        elif c9_function == 'OpeningClosing':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.OpeningClosing(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>OpeningClosing: Khử nhiễu ảnh</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Boundary(phát hiển các điểm biên và khoanh vùng các điểm biên)
        elif c9_function == 'Boundary':
            imgout = c9.Boundary(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>Boundary: Phát hiện các điểm biên và khoanh vùng các điểm biên</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # HoleFill(lấp 1 lỗ trong ảnh)
        elif c9_function == 'HoleFill':
            imgout = c9.HoleFill(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>HoleFill: Lấp 1 lỗ trong ảnh</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # MyConnectedComponent( lọc ra liên thông và đếm có bao nhiêu miếng xương gà)
        elif c9_function == 'MyConnectedComponent':
            imgout = c9.MyConnectedComponent(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>MyConnectedComponent: Lọc ra liên thông và đếm có bao nhiêu miếng xương gà</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)

        # CountRice( đếm có bao nhiêu hạt gạo)
        elif c9_function == 'CountRice':
            imgout = c9.CountRice(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>CountRice: Đếm có bao nhiêu hạt gạo</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('doi.gif', caption='Wait for processing...')
            state = '<p style="font-family: didot, serif; color: #006400; font-size: 18px; texxt-align: left;">Phương pháp đã chọn để xử lý ảnh:</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #ff4500; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
else:
    st.image('load1.gif', use_column_width=True)



        
from pdf2docx import Converter
import streamlit as st
from streamlit_pdf_reader import pdf_reader
import io

st.title('PDF to Word Document')

pdf_file = st.file_uploader(
    "Upload PDF", accept_multiple_files=False
)

if pdf_file is not None:

    pdf_name = pdf_file.name
    docx_name = pdf_name[:-4] + '.docx'

    #read & convert file
    bytes_data = pdf_file.getvalue()
    cv = Converter(stream=bytes_data)
    out_stream = io.BytesIO()
    cv.convert(out_stream)
    cv.close()

    #download file
    btn = st.download_button(
        label="Download Word Document",
        data=out_stream.getvalue(),
        file_name=docx_name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
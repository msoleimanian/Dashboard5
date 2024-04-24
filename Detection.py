import streamlit as st
import streamlit as st
from github import Github
import os
import boto3

access_key = 'AKIATUKO5RPGWYNFU2RN'
Secret_access_key = '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'
def get_download_link(file_path):
    """Generate a download link for the file."""
    return f'<a href="{file_path}" download>Click here to download the file</a>'

def Detection_constructor1(file_path, bucket_name, object_key):
    try:
        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
        s3.upload_file(file_path, bucket_name, object_key)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error uploading file: {e}")


def Detection_constructor():
    st.title("File Uploader")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        file_path = os.path.join(uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write(get_download_link(file_path), unsafe_allow_html=True)

        if st.button("Upload to AWS"):
            Detection_constructor1(file_path, 'dtgaroimages', uploaded_file.name)



    





import streamlit as st
import streamlit as st
import os
import boto3

access_key = 'AKIATUKO5RPGWYNFU2RN'
Secret_access_key = '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'


def download_file_from_s3(bucket_name, object_key, download_path):
    try:
        s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
        s3.download_file(bucket_name, object_key, download_path)
        print("File downloaded successfully!")
    except Exception as e:
        print(f"Error downloading file: {e}")



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

def generate_public_url(bucket_name, object_key):
    s3 = boto3.client('s3' , aws_access_key_id=access_key, aws_secret_access_key=Secret_access_key)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600  # URL expiration time in seconds (adjust as needed)
    )
    return url

def Detection_constructor():
    st.title("File Uploader")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        file_path = os.path.join(uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write(get_download_link(file_path), unsafe_allow_html=True)
        Detection_constructor1(file_path, 'dtgaroimages', uploaded_file.name)

    bucket_name = 'dtgaroimages'
    object_key = uploaded_file.name
    download_path = os.path.join(object_key.split("/")[-1])

    download_file_from_s3(bucket_name, object_key, download_path)
    if os.path.exists(download_path):
        print(f"File downloaded to: {download_path}")

    # Example usage
    urlimage = generate_public_url('dtgaroimages', uploaded_file.name)
    print("Public URL:", urlimage)


    #______--------_________-----------__

    import requests
    st.write(urlimage)
    st.write(uploaded_file.name)
    public_url = "https://6cbc-34-74-152-89.ngrok-free.app"  # Replace with your actual URL
    url = urlimage
    local_filename = uploaded_file.name

    # API endpoint URL
    api_endpoint = f"{public_url}/filename"

    # Send POST request to the API with JSON payload
    payload = {
        "filename": local_filename,
        "filelink": url
    }
    response = requests.post(api_endpoint, json=payload)

    # Check if request was successful
    if response.status_code == 200:
        result = response.json()
        print("Response:", result)
        st.write(result)
    else:
        print("Error:", response.text)







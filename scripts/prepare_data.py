import requests
import hashlib
import zipfile
import os

data_url = "https://archive.ics.uci.edu/static/public/109/wine.zip"
zip_file_path = 'wine.zip'

if not os.path.exists(zip_file_path):
    response = requests.get(data_url)
    with open(zip_file_path, mode='wb') as f:
        f.write(response.content)

with open(zip_file_path, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

wine_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'

if wine_sha256 == sha256hash:
    print("Computed hash matches expected hash for original data.")

    os.makedirs('data', exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('data')
    print("File unzipped successfully into 'data' directory.")
else:
    print("Computed hash does not match the expected hash for original data. File will not be unzipped.")

import os
from google.cloud import storage
#クラウドストレージ（バケット）に接続
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='./keyfile.json'
client = storage.Client()
bucket = client.get_bucket('sneakers')

#ファイルをアップロード
blob = bucket.blob('nike/hogehoge.png')
blob.upload_from_filename(filename='/Users/kanamori/Desktop/05a08cb18f11c4870ac49d562d71fdf6.png')
print('https://console.cloud.google.com/storage/browser/sneakers/' + blob.name)
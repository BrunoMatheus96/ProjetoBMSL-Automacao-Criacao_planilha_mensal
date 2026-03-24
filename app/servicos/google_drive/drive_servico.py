"""
Aqui você usa o google drive e executa ações como:
- Upload
- Download
- Listar arquivos
"""

from googleapiclient.discovery import build
from app.servicos.google_drive.auth import get_credenciais
from googleapiclient.http import MediaIoBaseDownload
import io

class GoogleDriveServico:

    def __init__(self):
        creds = get_credenciais()
        self.service = build("drive", "v3", credentials=creds)

    def listar_arquivos(self):
        results = self.service.files().list(
            pageSize=10,
            fields="files(id, name, mimeType)"
        ).execute()

        return results.get("files", [])
    
    def download_arquivo(self, file_id, file_name):
        file = self.service.files().get(fileId=file_id, fields='mimeType').execute()
        mime_type = file['mimeType']

        if 'google-apps' in mime_type:
            request = self.service.files().export_media(
                fileId=file_id,
                mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        else:
            request = self.service.files().get_media(fileId=file_id)

        fh = io.FileIO(file_name, "wb")
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()

        print("Download concluído ✅")
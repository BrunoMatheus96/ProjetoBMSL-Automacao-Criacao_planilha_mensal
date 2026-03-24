from app.servicos.google_drive.drive_servico import GoogleDriveServico

def listar_arquivos():
    drive = GoogleDriveServico()
    files = drive.listar_arquivos()

    for f in files:
        print(f["name"], f['id'], f["mimeType"])
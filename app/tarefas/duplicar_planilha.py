from app.servicos.google_drive.drive_servico import GoogleDriveServico

def navegar_ate_2026():
    drive = GoogleDriveServico()

    raiz = "root"  # Meu Drive

    freelas = drive.get_folder_id("Freelas", raiz)
    silvia = drive.get_folder_id("Silvia", freelas)
    controle = drive.get_folder_id("Controle interno", silvia)
    mes_ano = drive.get_folder_id("Mês/Ano", controle)
    pasta_2026 = drive.get_folder_id("2026", mes_ano)

    print("ID da pasta 2026:", pasta_2026)

    return pasta_2026

def duplicar_mes():
    drive = GoogleDriveServico()

    pasta_2026 = navegar_ate_2026()

    arquivo = drive.get_file_in_folder("Março", pasta_2026)

    novo_id = drive.copiar_arquivo(arquivo["id"])

    drive.renomear_arquivo(novo_id, "Abril")

    print("Duplicado com sucesso")
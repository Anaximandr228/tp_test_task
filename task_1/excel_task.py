import os
import pandas as pd


def create_empty_excel(columns: list, filename: str, sheet_name: str = 'Sheet1'):
    df = pd.DataFrame(columns=columns)

    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = os.path.join('excel_files', filename)
    excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False, sheet_name=sheet_name, freeze_panes=(1, 0))
    excel_writer._save()

    return filepath

def create_tabel_users():
    filepath = create_empty_excel(columns=['Наименование', 'Тип товара', '', 'Тип товара результат'],
                                  filename='Результат.xlsx')


create_tabel_users()
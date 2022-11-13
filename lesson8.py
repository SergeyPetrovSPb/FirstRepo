import tabula
import glob

pdf_files = glob.glob("*.pdf")
for pdf_file_name in pdf_files :
    # Формируем путь к pdf-файлу
    pdf_path = f"./{pdf_file_name}"
    
    # Получаем список из датафреймов с таблицами на 3-й странице
    list_df_tables = tabula.read_pdf(pdf_path, pages=3)
    
    # Обрабатываем датафреймы
    i = 0
    for df_table in list_df_tables :
        # Убираем переводы строки в наименованиях столбцов.
        list_columns = []
        for column_name in list(df_table.columns) :
            list_columns.append(column_name.replace('\r', ' '))
        df_table.columns = list_columns  
        
        # Формируем имя для csv-файла с таблицей
        i = i + 1
        csv_file_name = pdf_file_name.split(".")[0]+f"_table_{i}.csv"
        csv_path = f"./{csv_file_name}"
        
        # Сохраняем датафрейм в формате csv с разделителем - точкой с запятой 
        df_table.to_csv(csv_path, sep=";")
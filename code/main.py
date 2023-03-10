from core.config import *
from core.file_config import *
from core.preprocess import *

if os.path.exists("../tmp_data"):
    rmtree("../tmp_data")
os.mkdir("../tmp_data")

file_csv = convert_to_csv(input_file, dir=output_dir) # конвертация файла в формат .csv
file_without_columns = remove_columns(file_csv, columns=columns) # удаление лишних столбцов из файла

# vectorized_data = vectorize_csv_with_w2v(file_without_columns)

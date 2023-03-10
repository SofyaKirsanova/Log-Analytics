from core.config import *

'''
Модуль для работы с файлами
'''


# конвертация файла в формат .csv
def convert_to_csv(file, dir='.'):
    if file.endswith('.csv'):
        print(f'{file} is already in CSV format.')
        return file

    elif file.endswith('.log') or file.endswith('.txt'):
        delimiter = ' '
    elif file.endswith('.csv'):
        delimiter = ' '
    else:
        print(f'Invalid file format for {file}.')
        return None
    output_file = os.path.join(dir, os.path.splitext(os.path.basename(file))[0] + '.csv')
    print(output_file)
    with open(file, 'r') as in_file:
        with open(f"../{output_file}", 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for line in in_file:
                fields = line.split(delimiter)
                writer.writerow(fields)

    print(f'{file} has been converted to CSV format and saved as {output_file}.')
    return output_file


# удаление столбцов из файла
def remove_columns(file, columns):
    # Open the input file
    with open(f"../{file}", 'r') as in_file:
        # Create a CSV reader object
        reader = csv.reader(in_file)

        # Create the output file name
        output_file = os.path.splitext(file)[0] + '_without_columns.csv'

        # Open the output file for writing
        with open(f"../{output_file}", 'w', newline='') as out_file:
            # Create a CSV writer object
            writer = csv.writer(out_file)

            # Loop through each row in the input file
            for row in reader:
                # Create a new row without the specified columns
                new_row = [field for i, field in enumerate(row) if i not in columns]

                # Write the new row to the output file
                writer.writerow(new_row)

    print(f'{file} has been processed and saved as {output_file}.')
    return output_file
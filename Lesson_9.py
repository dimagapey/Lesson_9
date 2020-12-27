import csv
import argparse

#сделал так, как ты показывал. Незнаю, что можно было бы изменить,
#чтобы улучшить. А ухудшать смысла не вижу.

def check_arguments(arguments):
    arg_dict = {'BRAND': arguments.brand, 'COLOR': arguments.color,
                'MAKE_YEAR': arguments.year, 'FUEL': arguments.fuel}
    arg_dict = {key: value for key,
                               value in arg_dict.items() if value is not None}
    if arg_dict:
        return arg_dict
    else:
        raise SystemExit('There is no optional arguments')


def read_from_csv(filename):
    with open('cars.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimeter=';')
        result = []
        filters = {k: v for k, v in args_dict.items() if v}
        for row in csv_reader:
            if row['BRAND'] == args_dict['brand'] and \
                    row['COLOR'] == args_dict['color'] and \
                    row['MAKE_YEAR'] == args_dict['year'] and \
                    row['FUEL'] == args_dict['fuel']:
                result.append(row)
            if filters.items() <= row.items():
                result.append(row)
    return write_in_csv(result)


def write_in_csv(res):
    filename = '-'.join(args_dict.values()) + '.csv'
    with open(filename, 'w', newline='') as csvresult:
        headers = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL']
        csv_writer = csv.DictWriter(csvresult, filename=headers,
                                    extrasaction='ignore')
        csv_writer.writeheaders()
        csv_writer.writerows(res)
        print(f'Writed into {filename}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transport Registry')
    parser.add_argument('o', help='Enter the filename in csv format')
    parser.add_argument('--brand', help='Введите название модели')
    parser.add_argument('--color', help='Введите цвет модели')
    parser.add_argument('--year', help='Введите год выпуска')
    parser.add_argument('--fuel', help='Введите желаемый вид топлива')
    arguments = parser.parse_args()
    args_dict = check_arguments(arguments)
    read_from_csv(arguments.o)

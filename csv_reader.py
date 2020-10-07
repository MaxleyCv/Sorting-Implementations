import csv
import utils
import printer


def get_printers_from_file():
    csv_info_file = open(utils.INPUT_FILE)
    reader = csv.reader(csv_info_file)
    list_of_printers = []
    for row in reader:
        new_printer = printer.Printer(name=row[0], printing_speed=row[1], price_in_uah=row[2])
        list_of_printers.append(new_printer)
    return list_of_printers



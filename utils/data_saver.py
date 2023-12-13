import csv
import json
import logging


# Class for saving/reading data
class FileHandler:

    # Save data to json file
    def save_to_json(self, filename, data):
        logging.info(f'Saving data to file {filename}')
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    # Save data to csv file
    def save_to_csv(self, filename, data, header=True):
        logging.info(f'Saving data to file {filename}')
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if header:
                if data:
                    fields = list(data[0].keys())
                    csv_writer.writerow(fields)
            for item in data:
                csv_writer.writerow(item.values())

    # Save data to txt file
    def save_to_txt(self, filename, data):
        logging.info(f'Saving data to file {filename}')
        with open(filename, 'w') as txt_file:
            if data == list:
                for item in data:
                    txt_file.write(item + '\n')
            else:
                txt_file.write(data)

    # Read data from json file
    def read_json_from_file(self, filename):
        logging.info(f'Reading data to file {filename}')
        with open(filename, 'r') as json_file:
            return json.load(json_file)

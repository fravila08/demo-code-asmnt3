import csv, os
# ​
import csv
# Zaynab's Code
# ​
class CSV_Interface:
    
    def __init__(self, filename):
        
        with open(os.path.join(filename), "r") as f:
            reader = csv.DictReader(f, skipinitialspace=True, delimiter=',')
            self.column_names = reader.fieldnames
        
        self.filename = filename
        self.all_data = self.update_data_from_file()
        
    
    def get_data(self):
        self.update_data_from_file()
        return self.all_data 
    
    def update_data_from_file(self):
        """ reads the csv file and update the all_data """
        data = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f, skipinitialspace=True, delimiter=',')
            for row in reader:
                data.append(row)
            
        self.all_data = data
        return self.all_data
    
    def append_one_row_to_file(self, new_data_dict):
        """ writes to csv file by row then it updates the current all_data """
        print(new_data_dict.keys())
        
        #  "a" just appends to the data instead of "w" which overwites it
        with open(self.filename, "a", newline='') as f:
            writer = csv.DictWriter(f,fieldnames=self.column_names)
            writer.writerow(new_data_dict)
            
        self.update_data_from_file()
        return self.all_data
    
    def write_all_rows_to_file(self, data_rows):
        """ This grabs a list of dictionaries and rewrites the whole file"""
        with open(self.filename, "w", newline='' ) as f:
            writer = csv.DictWriter(f, skipinitialspace=True,fieldnames=self.column_names)
            # writerheader() adds the header
            writer.writeheader()
            writer.writerows(data_rows)
        
        self.update_data_from_file()
        return self.all_data
    
    def remove_a_row(self, dict_of_data_to_be_removed):
        """takes a specific dictionary and removes it from csv and updates the all_data"""
        self.all_data.remove(dict_of_data_to_be_removed)
        self.write_all_rows_to_file(self.all_data)
        self.update_data_from_file()
        return self.all_data
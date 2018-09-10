import csv
import pandas as pd
import re # regex



def read_file(file_name):
    # with open(file_name, newline='') as csvfile:
    #     csv_reader = csv.DictReader(csvfile, delimiter=';')
    #
    #     headers = csv_reader.fieldnames()
    # print("Headers are: {0}".format(headers))
    # # for row in csv_reader:
    # #     print(', '.join(row))
    print("CSV_PROCESSOR: gonna open {0}".format(file_name))
    input_data = pd.read_csv(file_name, sep=";")
    # headers = input_data.iloc[0]
    # print("Headers are: {0}".format(headers))
    return input_data



class Report():

    fields_to_ommit = "Osoba sprawdzająca", "Sygnatura czasowa"
    id = -1

    def __init__(self, headers ,in_data):
        # self.id = id
        self.data = {}
        i = 0
        points_accumulated = 0
        for name in headers:
            if pd.isnull(in_data[i]) or pd.isna(in_data[i]):
                val = ""
            else :
                val = in_data[i]
                # TODO ( high ) w niektórych opisach znajduje się rok i jest on przetwarzany jako liczba.
                # if name != "Drużyna" and name != "Sygnatura czasowa":
                    # try:
                    #     tmp = re.search(r"(\d+\.?,?\d+)", val).group(0)
                    #     tmp = tmp.replace(",",".")
                    #     points_accumulated += float(tmp)
                    #     print("From val {0} there is tmp {1}".format(val, tmp))
                    # except TypeError:
                    #     points_accumulated += float(val)
                    #     print("From val {0} there is tmp {1}".format(val, val))
                    # except Exception:
                    #     pass
            # print("Dodaje: ['{0}'] = {1}".format(name, val))
            # if name in self.data.keys() and self.data[name] != val:
            #     print("Byla wartosc dla: >>{0}<< poprzednia >>{1}<< teraz bedzie >>{2}<<".format(name, self.data[name], val))
            self.data[name] = val
            i += 1
        self.data['Punktów ogółem'] = points_accumulated
        # print(self.shortDesc())
        # self.data = in_data

    def shortDesc(self):
        return "Raport dla {0}".format(self.Drużyna)

    def toString(self):
        result = ""
        for x in self.data:
            result += "{0}: {1}\n".format(x, self.data[x])
        return result

    def __getattr__(self, attr):
        return self.data[attr]

    def getFields(self):
        return list(self.data.keys())

    def getDisplayableFileds(self):
        displayableFields = list()
        for field in list(self.data.keys()):
            if not field in self.fields_to_ommit:
                displayableFields.append( re.sub(r"\. ?\d+", "", field) ) #deletes . optionally spaces and digits after this

        return displayableFields




def create_record_table(records_data):
    headers = records_data.columns
    # print(headers)
    records_table = [ Report(headers, record) for record in records_data.get_values() ]
    # print("Elementow: {0}".format(records_table.__len__()))
    # for x in records_table:
    #     print(x.shortDesc())
    return records_table


def generate_HTML_report_table(record):
    table_style = "table { \
    font-family: arial, sans-serif; \
    border-collapse: collapse; \
    width: 100%; } \
    td, th { \
    border: 1px solid #dddddd; \
    text-align: left; \
    padding: 8px; } \
    tr:nth-child(even) { \
    background-color: #dddddd;}"

    result = '<!doctype html><head><style>{1}</style><title>Sprawdzenie poprawnosci dla {0}</title></head><body><h2> Ocena planu pracy {2}</h2><table><tbody>'.format(record.Drużyna, table_style, record.Drużyna)
    for field in record.getDisplayableFileds():
        if isinstance( record.data[field], str) :
            result += "<tr><td>{0}</td><td>{1}</td></tr>".format(field, record.data[field])
        else:
            result += "<tr><td>{0}</td><td>{1}</td></tr>".format(field, record.data[field])
    result +="<tbody></table></body></html>"


    return result

# data = read_file("data\odpowiedzi.csv")
# print(data.iloc[0])
# print("-=-=-=-=-=-=-=--=-")
# print(data.iloc[1])
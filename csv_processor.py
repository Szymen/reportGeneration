import csv
import pandas as pd
import Report


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






def create_record_table(records_data):
    headers = records_data.columns
    # print(headers)
    # print(type(records_data))
    
    records_table = [ Report.Report(headers, record) for record in records_data.values ]
    
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
    # if record.Drużyna !=  # dodac co jak szczep/krag/gromada

    result = '<!doctype html><head><meta charset="UTF-8"><style>{1}</style><title>Sprawdzenie poprawnosci dla {0}</title></head><body><h2> Ocena programu pracy {2}</h2><table><tbody>'.format(record.groupType, table_style, record.groupType)
    for field in record.getDisplayableFieldsList():
        key = Report.getDisplayableFieldName(field) 
        if key.count("(") > 0:
            key = key.replace("(", "</br>(")  
            key = key.replace(")", ")</br>")  

        if isinstance( record.data[field], str) :
            
            if record.data[field].count(";") > 1:
                value =  record.data[field].split(";")
                value = "</br>".join(value)
            else:
                value =  record.data[field]
            

            result += "<tr><td>{0}</td><td>{1}</td></tr>".format( key, value)
        else:
            result += "<tr><td>{0}</td><td>{1}</td></tr>".format( key, record.data[field])
    result +="<tbody></table></body></html>"


    return result

# data = read_file("data\odpowiedzi.csv")
# print(data.iloc[0])
# print("-=-=-=-=-=-=-=--=-")
# print(data.iloc[1])
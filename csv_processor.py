import pandas as pd
import Report

from config import config as global_config


def read_file(file_name):
    print("CSV_PROCESSOR: gonna open {0}".format(file_name))
    input_data = pd.read_csv(file_name, sep=global_config.CSV_SEPARATOR)
    return input_data


def create_record_table(records_data):
    headers = records_data.columns
    records_table = [ Report.Report(headers, record) for record in records_data.values ]
    return records_table

def generate_HTML_report_table(record):
    table_style = """
    @font-face {
font-family:"museo-sans";
src:url("https://use.typekit.net/af/a28b50/00000000000000000000e803/27/l?primer=f592e0a4b9356877842506ce344308576437e4f677d7c9b78ca2162e6cad991a&fvd=n5&v=3") format("woff2"),url("https://use.typekit.net/af/a28b50/00000000000000000000e803/27/d?primer=f592e0a4b9356877842506ce344308576437e4f677d7c9b78ca2162e6cad991a&fvd=n5&v=3") format("woff"),url("https://use.typekit.net/af/a28b50/00000000000000000000e803/27/a?primer=f592e0a4b9356877842506ce344308576437e4f677d7c9b78ca2162e6cad991a&fvd=n5&v=3") format("opentype");
font-display:swap;font-style:normal;font-weight:500;
}

  html{
    font-family: museo-sans, arial, sans-serif;
  }

    table {
      border-collapse: collapse;
      width: 100%;
    }

    td,
    th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {
      background-color: #D9E8BF;
    }
    
    """

    result = '<!doctype html><head><meta charset="UTF-8"><style>{1}</style><title>Sprawdzenie poprawnosci dla {0}</title></head><body><h2> Ocena programu pracy {2}</h2><table><tbody>'.format(record.groupType, table_style, record.groupType)
    for field in record.getDisplayableFieldsList():
        key = Report.getDisplayableFieldName(field) 
        if key.count("(") > 0:
            key = key.replace("(", "</br>(")  
            key = key.replace(")", ")</br>")

        if isinstance( record.data[field], str):
            if record.data[field].count(";") > 1:
                value = "<br>".join(record.data[field].split(";"))
            else:
                value =  record.data[field]
            
            value = value.strip()
            result += "<tr><td>{0}</td><td>{1}</td></tr>".format( key, value)
        else:
            result += "<tr><td>{0}</td><td>{1}</td></tr>".format( key, record.data[field])
    result +="<tbody></table></body></html>"

    return result

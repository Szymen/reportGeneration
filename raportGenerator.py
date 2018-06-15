from flask import Flask, render_template
import csv_processor
import  os, sysconfig

app = Flask(__name__)

currentRoot = "C:\\src\\raportGenerator\\"
report_data = csv_processor.read_file( currentRoot +"data\\odpowiedzi.csv")
records = csv_processor.create_record_table(report_data)
# print (records)
directory = os.path.dirname(currentRoot +"raports\\")
if not os.path.exists(directory):
    os.makedirs(directory)

report_count = 0
for record in records:
    # print(record.toString())
    try:
        report_in_html = csv_processor.generate_HTML_report_table(record)
        file_name = currentRoot +"raports\\sprawdzenie_planu_pracy_"+record.Drużyna+".html"
        print("REPORT GENERATOR: Opening file {0}".format(file_name))
        f_out = open(file_name, 'w')
        f_out.write(report_in_html)
        f_out.close()
        report_count += 1
    except Exception:
        print("REPORT GENERATOR: Something went wrong with generation raport")
        print("REPORT GENERATOR: Error message {0}".format( sysconfig.exc_info()[0]) )
print("REPORT GENERATOR: Successfully created {0} reports".format(report_count))

@app.route('/')
def list_reports():
    raports_list = os.listdir(currentRoot +"raports")  # returns list
    # print(raports_list)
    return render_template('fullraport.html', raports_list = raports_list, local_path = currentRoot+"raports/" )


if __name__ == '__main__':
    app.run()

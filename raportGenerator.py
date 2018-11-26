from flask import Flask, render_template
import csv_processor
import  os, sysconfig, logging, time
import Report

app = Flask(__name__)



try:
    logger = logging.getLogger('Report Generator')
    logger.setLevel(logging.DEBUG) # most verbose version
    log_file_name = "application_logs.log"
    fh = logging.FileHandler(log_file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    Report.logger = logger
except Exception:
    print("Something went wrong with setup of logs")
    print("Error message {0}".format(sysconfig.exec_info()[0]))
    exit

print("Logs setup into {0}".format(log_file_name))

currentRoot = "C:\\src\\raportGenerator\\"


@app.route('/')
def hello_world():
    # return "Semmes that server is working!"
    return render_template("hello_page.html", context = 0)

@app.route('/reports')
def list_reports():
    reports_path = currentRoot +"\\reports"
    if os.path.exists(reports_path):
        logger.debug("Getting list of {0}".format(reports_path))
        reports_list = os.listdir(reports_path)  # returns list
        # print(reports_list)
        return render_template('full_report.html', reports_list = reports_list, local_path =currentRoot + "reports/")
    else:
        return "No reports generated so far in {0}: (.".format(reports_path)


@app.route('/generate/<path:filename>')
def generate_reports(filename):

    # report_data_path = currentRoot + "data\\odpowiedzi.csv"
    report_data_path = currentRoot + filename
    logger.info("Will be reading data from {0}".format(report_data_path))

    report_data = csv_processor.read_file(report_data_path)
    records = csv_processor.create_record_table(report_data)

    # print (records)
    report_directory = os.path.dirname(currentRoot + "reports\\")
    logger.info("Reports will be put into {0}".format(report_directory))
    if not os.path.exists(report_directory):
        logger.debug("Folder {0} had to be created".format(report_directory))
        os.makedirs(report_directory)
    else:  # there could be leftovers from previous execution
        previous_files = os.listdir(report_directory)
        if previous_files.__len__() != 0:
            archive_folder = "{0}\old_files_{1}".format(report_directory, time.strftime(
                "%d%m%Y_%H%M"))  # folder will be like \raports\old_files_20121224_2323
            if os.path.exists(archive_folder):
                archive_folder += "_{0}".format(os.listdir(
                    report_directory).__len__() + 1)  # if it was runned the same minute it will get just suffix with count of folders
            logger.info("There was files in raport directory. Moving them into {0}".format(archive_folder))
            os.makedirs(archive_folder)
            for file in previous_files:
                os.rename("{0}\{1}".format(report_directory, file), "{0}\{1}".format(archive_folder, file))
                logger.debug("Moved {0} into {1}"
                             .format("{0}\{1}".format(report_directory, file), "{0}\{1}".format(archive_folder, file)))
            print("Moved whole content of report folder into {0}".format(archive_folder))

    report_count = 0
    for record in records:
        # print(record.toString())
        try:
            report_in_html = csv_processor.generate_HTML_report_table(record)
            file_name = "{0}reports\\sprawdzenie_programu_pracy_{1}.html".format(currentRoot,
                                                                              record.groupType.replace(" ", ""))
            f_out = open(file_name, 'w', encoding="utf-8")
            f_out.write(report_in_html)
            logger.debug("Generated {0}".format(file_name))
            f_out.close()
            report_count += 1
        except Exception:
            logger.error("REPORT GENERATOR: Error message {0}".format(sysconfig.exc_info()[0]))

    logger.info("Successfully created {0} reports".format(report_count))
    print("REPORT GENERATOR: Successfully created {0} reports".format(report_count)) #writes to console

    return "Successfully created {0} reports from file: {1}".format(report_count, report_data_path)


if __name__ == '__main__':
    print("Application is serving this maping: \n{0}".format(app.url_map))
    print("") # for empty line
    app.run()

import re # regex
import pandas as pd
import os
import json
import raportGenerator

groupTypes = ("Drużyna", "Szczep", "Gromada", "Krąg") #these are the names group types

# @staticmethod
def getDisplayableFieldName(fieldName):
    if fieldName == "groupType": # TODO (medium/low): think of better solution for dynamic group typess
        return "Jednostka"
    return re.sub(r"\. ?\d+", "", fieldName)  # deletes . optionally spaces and digits after this

def getNumberFromFieldVaule(fieldValue):
    try:
        tmp = re.search(r"(\(\d+\.?,?\d+\))", fieldValue).group(0)
        tmp = tmp.replace(",", ".")
        to_be_added = float(tmp)
        print("From val {0} there is tmp {1} = {2}".format(fieldValue, tmp, to_be_added))
    except TypeError:
        try:
            to_be_added = float(fieldValue)
        except Exception:
            pass
        print("From val {0} there is tmp {1}".format(fieldValue, fieldValue))
    except Exception:
        pass


    return -1

class Report():

    default_global_config_path = ".\config\global_config.json"

    logger = raportGenerator.logger # injects logger set in reportGenerator.py

    logger.debug("Want to read: {0}".format(default_global_config_path))
    if os.path.exists(default_global_config_path):
        with open(default_global_config_path, encoding="UTF-8") as f:
            logger.info("Have read global config from: {0}".format(default_global_config_path))
            config_json = json.load(f)
            if "raport_fields_to_ommit" in config_json.keys():
                fields_to_ommit = config_json["raport_fields_to_ommit"]
                logger.debug("Fields to ommit: {0}".format(fields_to_ommit))
    else:
        logger.debug("Default global config not found")

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
                to_be_added = 0
                val = in_data[i]
                # TODO ( high ) w niektórych opisach znajduje się rok i jest on przetwarzany jako liczba.

            #     if name != "Drużyna" and name != "Sygnatura czasowa":
            #         to_be_added = getNumberFromFieldVaule(val)
            # points_accumulated += to_be_added
            # print("Dodaje: ['{0}'] = {1} - {2}".format(name, val, to_be_added))

            # if name in self.data.keys() and self.data[name] != val:
            #     print("Byla wartosc dla: >>{0}<< poprzednia >>{1}<< teraz bedzie >>{2}<<".format(name, self.data[name], val))
            # if name in self.data.keys():
            #     key_name = "{0}____{1}".format(self.data.keys().__len__(), name) # some field name can appear multiple times, but they are in different context, so we are adding suffix which will be deleted before getting visible
            # else:
            #     key_name = name
            # self.data[key_name] = val
            if name in groupTypes:
                # print("is  {0} in {1}".format(name, groupTypes))
                self.data['groupType'] = val
            else:
                # print("not {0} in {1}".format(name, groupTypes))
                self.data[name] = val
            i += 1
        # self.data['Punktów ogółem'] = points_accumulated
        # print(self.shortDesc())
        # self.data = in_data

    def shortDesc(self):
        return "Raport dla {0}".format(self.groupType)

    def toString(self):
        result = ""
        for x in self.data:
            result += "{0}: {1}\n".format(x, self.data[x])
        return result

    def __getattr__(self, attr):
        return self.data[attr]

    def getFields(self):
        return list(self.data.keys())


    def getDisplayableFieldsList(self):
        displayableFields = list()
        for field in list(self.data.keys()):
            if not field in self.fields_to_ommit:
                displayableFields.append( field )
        return displayableFields


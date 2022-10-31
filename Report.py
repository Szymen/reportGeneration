import re # regex
import pandas as pd
import os
import json
import reportGenerator
import config.field_order as field_order
groupTypes = ("Drużyna", "Szczep", "Gromada", "Krąg") #these are the names group types
GROUP_TYPE_KEY = 'Jednostka'

logger = reportGenerator.logger  # injects logger set in reportGenerator.py


# @staticmethod
def getDisplayableFieldName(fieldName):
    if fieldName == GROUP_TYPE_KEY: # TODO (medium/low): think of better solution for dynamic group typess
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


def _get_longest_duplicate_substring(input_string: str) -> str:

    substing_array = []
    for i in range(input_string.__len__()):
        work_string = input_string[0:i]
        sub_string_count = input_string.count(work_string)

        if sub_string_count > 1 and input_string.replace(work_string, "").strip() == "":
            substing_array.append(work_string)

    if substing_array == []:
        return input_string.strip()

    result_string = ""
    for x in substing_array:
        if result_string.__len__() < x.__len__():
            result_string = x

    return result_string


def remove_duplicates(input_string: str) -> str:
    if type(input_string) != str:
        return input_string

    if len(input_string) < 5 or input_string == "":
        return ""

    if input_string.count(input_string[0:4]) == 1:
        return input_string

    final_result = _get_longest_duplicate_substring(input_string)

    previous_result = ""
    while final_result != previous_result:
        previous_result = final_result
        final_result = _get_longest_duplicate_substring(final_result)

    # sometimes there is multiple duplicates so we do this recursive
    return final_result.strip()

class Report():
    default_global_config_path = "./config/global_config.json"


    logger.debug("Want to read: {0}".format(default_global_config_path))
    if os.path.exists(default_global_config_path):
        with open(default_global_config_path, encoding="UTF-8") as f:
            logger.info("Have read global config from: {0}".format(default_global_config_path))
            config_json = json.load(f)
            if "report_fields_to_ommit" in config_json.keys():
                fields_to_ommit = config_json["report_fields_to_ommit"]
                logger.debug("Fields to ommit: {0}".format(fields_to_ommit))
    else:
        logger.debug("Default global config not found")

    id = -1

    def __init__(self, headers, in_data):
        # self.id = id
        # logger.debug("Creating report with headers=\'{0}\' \nin_data=\'{1}\'".format(headers, in_data))

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


            if name in groupTypes or name.startswith("Drużyna") or name.startswith("Szczep") or name.startswith("Gromada") or name.startswith("Jednostka") or name.startswith("Numer Gromady"):
                # print("is >>{0}<< in {1} and val is >>{2}<<".format(name, groupTypes, val))
                self.data[GROUP_TYPE_KEY] = val
                self.data['groupType'] = val
            else:
                # print("not {0} in {1}".format(name, groupTypes))
                field_name = remove_duplicates(name)
                self.data[field_name] = remove_duplicates(val)
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
        # print( field_order.field_order )
        # print(self.data.keys())

        used_fields = 0
        not_used_fields = 0
        ommited = 0

        # for field in list(self.data.keys()):
        for field in field_order.field_order:
            if field not in self.fields_to_ommit :
                if field in self.data.keys():
                    # logger.debug("field {} present in data.keys()".format(field))
                    displayableFields.append( field )
                    used_fields += 1
                else:
                    logger.debug("field {} not present in data.keys() <=========".format(field))
                    not_used_fields += 1
            else:
                ommited += 1

        # +1 jest po groupType, które jest dodawane bo gdzieś jest uzywane i bez tego się wysypuje skrypt
        if used_fields + not_used_fields + ommited +1 != len(self.data.keys()):
            a = set(displayableFields)
            b = set(self.data.keys())
            print(b.difference(a))
            print("jest bubda")
            print("Used: {} not_used: {} ommited: {} Self.data.keys: {}".format(used_fields, not_used_fields, ommited, len(self.data.keys())))
            exit(1)

        if "" in displayableFields:
            displayableFields.remove("")

        # Ensure that groupType is the first key
        displayableFields.remove(GROUP_TYPE_KEY)
        displayableFields.insert(0, GROUP_TYPE_KEY)

        return displayableFields


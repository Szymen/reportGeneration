import re # regex
import pandas as pd
import os
import json
import reportGenerator

groupTypes = ("Drużyna", "Szczep", "Gromada", "Krąg") #these are the names group types
GROUP_TYPE_KEY = 'groupType'
EMAIL_HEADER_SET = {
    'Adres e-mail, z którego otrzymaliśmy program'
    # "Adres e-mail, z którego otrzymaliśmy program",
    "Adres e-mail, z którego wysłano program",
    "Adres email, z którego wysłano program",
    'Adres email, z którego wysłano program',
    'Mail odbiorcy',
    'Adres e-mail, z którego otrzymaliśmy program'
}
EMAIL_FIELD_KEY = "email_recipent"

TEMPLATE_HEADER = "ocena_templatka"


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

    if input_string.strip().lower() == "tak":
        return "tak"

    if input_string.strip().lower() == "nie":
        return "nie"

    if input_string.count(input_string[0:4]) == 1:
        return input_string

    if len(input_string) < 5 or input_string == "":
        return ""

    final_result = _get_longest_duplicate_substring(input_string)

    previous_result = ""
    while final_result != previous_result:
        previous_result = final_result
        final_result = _get_longest_duplicate_substring(final_result)

    # sometimes there is multiple duplicates so we do this recursive
    return final_result.strip()

class Report():
    default_global_config_path = "./config/global_config.json"

    logger = reportGenerator.logger # injects logger set in reportGenerator.py

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
        self.template_name = "defaultTemplateName"
        self.values_changed = False
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
            while(name.endswith("\n")):
                name = name.strip()


            if name in groupTypes or name.startswith("Drużyna") or name.startswith("Szczep") or name.startswith("Gromada") or name.startswith("Jednostka") or name.startswith("Numer Gromady") or name.startswith("Krąg"):
                # print("is >>{0}<< in {1} and val is >>{2}<<".format(name, groupTypes, val))
                self.data[GROUP_TYPE_KEY] = val
            elif remove_duplicates(name) in EMAIL_HEADER_SET or name in EMAIL_HEADER_SET:
                # print(f"Znalazlem mail!")
                # print(f"{val}")
                # exit(1)
                self.data[EMAIL_FIELD_KEY] = val.lower().strip()
            elif remove_duplicates(name) == TEMPLATE_HEADER:
                # print(f"template name! {val} - {remove_duplicates(val)}")
                self.template_name = val
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
        for field in list(self.data.keys()):
            if field.startswith("*"):
                print(f"Ommiting the field as it starts with asteriks! >{field}<")
                continue

            if field in self.fields_to_ommit or field in EMAIL_HEADER_SET:
                continue

            displayableFields.append( field )

        if "" in displayableFields:
            displayableFields.remove("")

        # Ensure that groupType is the first key
        displayableFields.remove(GROUP_TYPE_KEY)
        displayableFields.insert(0, GROUP_TYPE_KEY)
        return displayableFields


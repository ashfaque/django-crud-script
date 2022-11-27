
# ! USER INPUT VALIDATE
# ! If user press 0 any time. Current models.py is deleted and .bak file is renamed to models.py file. And same happens to other views urls slizer(check if urls and slizer exists if not exists then after cancel don't have urls and slizer leftover)
# ! https://stackoverflow.com/questions/65627122/moving-file-to-recycle-bin
# ! define a function for the above reason and call it everytime.
# ! in charfield option for do you want digits or both char in options show example. (1,sdlkjf) or (lksdf, lksjdf)
# ! URLS SERIALIZER VIEWS BAK. RED MSG AFTER HEADLINE THAT A BAK FILE IS AUTO GENERATED CONTAINING YOUR OLDER MODELS SLIZER VIEWS URLS FILE IF YOU TERMINATED THIS PROGRAM IN B/W ELSE. AA-REMOVE IT IN BACKGROUND AFTER PROGRAM ENDS.
# ! support for SSCRM and PMS like dj apps
# ! support for linux + macos + windows
# ! in the end convert this .py file to .exe file and give it to the user.
# ! Make well documented code as you might need to edit this file later so you can do it easily later on.
# ! have interactive messages for the user to see the progress of execution of code.
# ? https://towardsdatascience.com/how-to-easily-convert-a-python-script-to-an-executable-file-exe-4966e253c7e9
# ? pip install auto-py-to-exe
# ? auto-py-to-exe (Enter), in settings - change output location.
# ! create a .bak file
# ! Document # ?
# ! if user entered 0 then quit the execution of this program
# ! validate user inputs
# ! from `working_dir` auto pick file after assigning to a var, if path is not a file then ask for user input for file path and pass to function file_path_check_and_clean() and use it, assign its o/p to a var and use it
# ! ------------------------------------------------------------------------------------------------------------------------



def checkExit(variable : str):
    from sys import exit
    if variable == '0':
        exit()



def camelcase_to_snakecase_convert(string: str) -> str:
    import re
    # return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

    # ? To handle more advanced cases
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()



def file_path_check_and_clean(user_prompt : str) -> str:
    from sys import platform
    import os, re

    while True:
        file_path = input(user_prompt)
        checkExit(file_path)
        if file_path \
            and ( \
                (file_path[0] == "\"" and file_path[-1] == "\"") \
                or (file_path[0] == "\'" and file_path[-1] == "\'") \
        ):      # ? If first & last char of path is " or ' then it will be removed.
            file_path=file_path[1:-1]

        if platform == "win32":    # ? If OS is Windows.
            if file_path and file_path[0].isalpha() and file_path[1]==":" and (file_path[2]=="\\" or file_path[2]=="/"):      # ? If 1st char is case insensitive alphabet, 2nd char is a `:` & 3rd char is a `/` or `\`.
                if os.path.exists(file_path[:3]):         # ? Check if drive letter exists.
                    if os.path.isfile(file_path):         # ? Check if user given path points to a file ?
                        break
                    if os.path.isdir(file_path):      # ? If user given path doesn't have existing directory. It will create one.
                        print("\n\n##### ENTERED PATH POINTS TO A DIRECTORY #####")
                    # if os.path.exists(file_path):
                    #     break
                    else:
                        print("\n\n##### PLEASE ENTER VALID PATH #####")
                else:
                    print("\n\n##### DRIVE LETTER DOESN'T EXIST #####")
            else:
                print("\n\n##### PLEASE ENTER VALID PATH #####")

        elif platform == "linux" or platform == "linux2" or platform == "darwin":    # ? Checking if user OS is Linux or macOS.
            if os.path.isfile(file_path):         # ? Check if user given path points to a file ?
                break
            elif os.path.isdir(file_path):      # ? If user given path doesn't have existing directory. It will create one.
                print("\n\n##### DIR DOESN'T EXIST #####")
            # elif os.path.exists(file_path):
            #     break
            else:
                print("\n\n##### PLEASE ENTER VALID PATH #####")

        else:
            print("\n\n!!!!! UNSUPPORTED OPERATING SYSTEM !!!!!")

    return file_path



def main():

    import os, re
    from sys import platform, exit
    # from ashfaquecodes.ashfaquecodes import red_print_start, blue_print_start, green_print_start, color_print_reset

    print("\n\n"+"########## DJANGO MASTER API CREATOR ##########".center(120," ")+"\n")
    print("By Ashfaque Alam".center(120," ")+"\n\n")


    # ? Taking user input for generation of only model or APIs with model
    while True:
        only_model_generate = input("Do you want to only generate model or CRUD APIs with model? \nWrite 'y' to only generate model and 'n' to generate both APIs and models\nEnter your choice: ")
        checkExit(only_model_generate)
        if only_model_generate.lower() == 'y':
            only_model_generate = True
            break
        elif only_model_generate.lower() == 'n':
            only_model_generate = False
            break
        else: print("\n\nInvalid choice !!!. Please enter either y or n.")


    # ? Taking working directory input from user
    while True:
        working_dir = input("\nCopy & Paste the path of DJANGO APP from file explorer with drive letter.\nDjango App Path: ")
        checkExit(working_dir)
        if working_dir \
            and ( \
                (working_dir[0] == "\"" and working_dir[-1] == "\"") \
                or (working_dir[0] == "\'" and working_dir[-1] == "\'") \
        ):      # ? If first & last char of path is " or ' then it will be removed.
            working_dir=working_dir[1:-1]

        if platform == "win32":    # ? If OS is Windows.
            if working_dir and working_dir[0].isalpha() and working_dir[1]==":" and (working_dir[2]=="\\" or working_dir[2]=="/"):      # ? If 1st char is case insensitive alphabet, 2nd char is a `:` & 3rd char is a `/` or `\`.
                if os.path.exists(working_dir[:3]):         # ? Check if drive letter exists.
                    if os.path.isfile(working_dir):         # ? Check if user given path points to a file ?
                        print("\n\n##### GIVEN PATH POINTS TO A FILE. PLEASE ENTER A VALID DIRECTORY PATH #####")
                        continue
                    if not os.path.isdir(working_dir):      # ? If user given path doesn't have existing directory. It will create one.
                        print("\n\n##### DIR DOESN'T EXIST #####")
                    if os.path.exists(working_dir):
                        break
                else:
                    print("\n\n##### DRIVE LETTER DOESN'T EXIST #####")
            else:
                print("\n\n##### PLEASE ENTER VALID DIRECTORY PATH #####")

        elif platform == "linux" or platform == "linux2" or platform == "darwin":    # ? Checking if user OS is Linux or macOS.
            if os.path.isfile(working_dir):         # ? Check if user given path points to a file ?
                print("\n\n##### GIVEN PATH POINTS TO A FILE. PLEASE ENTER A VALID DIRECTORY PATH #####")
                continue
            elif not os.path.isdir(working_dir):      # ? If user given path doesn't have existing directory. It will create one.
                print("\n\n##### DIR DOESN'T EXIST #####")
            elif os.path.exists(working_dir):
                break
            else:
                print("\n\n##### PLEASE ENTER VALID DIRECTORY PATH #####")

        else:
            print("\n\n!!!!! UNSUPPORTED OPERATING SYSTEM !!!!!")



    app_name = working_dir.split('\\')[-1] if '\\' in working_dir else working_dir.split('/')[-1]


    # * ################################################ Models Generation #################################################

    # ? Checking if models.py exists, if not then asking use to enter the models.py file path.
    models_path = f"{working_dir}/models.py"
    if not os.path.isfile(models_path):
        models_path = file_path_check_and_clean("\nCopy & Paste the path of models.py from file explorer with drive letter: ")



    # ? Making a backup of user models file
    with open(models_path, "r") as readModelsFile:
        with open(f"{models_path}.bak", "w") as readModelsBakFile:
            readModelsBakFile.write(readModelsFile.read())



    # ? Generating new model in models.py file
    with open(models_path, "a+") as models_file:        # ? https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
        models_file.seek(0)                                            # ? Move file pointer to the beginning of the file.
        read_modelsfile = models_file.read()

        # ? Taking timezone info from user
        while True:
            is_timezone = input("Does your project contains timezone based fields? (y / n): ")
            checkExit(is_timezone)
            if is_timezone.lower() == 'y' or is_timezone.lower() == 'n':
                break
            else:
                print("\nInvalid input!!! Enter either y or n.")


        # ? Taking abstract user info from user
        while True:
            is_abstract_user = input("Does your project contains AbstractUser based User model? (y / n): ")
            checkExit(is_abstract_user)
            if is_abstract_user.lower() == 'y':
                working_dir_list = working_dir.split('\\') if '\\' in working_dir else working_dir.split('/')
                proj_dir_name = working_dir_list[-2]
                working_dir_list[-1] = working_dir_list[-2]
                proj_dir_path = '\\'.join(working_dir_list)
                try:
                    with open(f"{proj_dir_path}/settings.py", "r") as settings_file:
                        read_settings_file = settings_file.read()
                    if 'AUTH_USER_MODEL' in read_settings_file:
                        user_model = 'settings.AUTH_USER_MODEL'
                except:
                    user_model = input("Enter AbstractUser model name: ")
                    checkExit(user_model)
                    user_model_app_name = input("Enter abstract user model app name: ")
                    checkExit(user_model_app_name)
                    # user_model = user_model_app_name + '.' + user_model
                break

            elif is_abstract_user.lower() == 'n':
                user_model = 'User'
                while True:
                    is_user_model_extended = input("Do you have any other model which extends the auth_user model? (y / n): ")
                    checkExit(is_user_model_extended)
                    if is_user_model_extended.lower() == 'y' or is_user_model_extended.lower() == 'n':
                        break
                    else:
                        print("\nInvalid input!!! Enter either y or n.")
                if is_user_model_extended.lower() == 'y':
                    extended_user_model_name = input("Enter extended user model name: ")    # ? E.g., TCoreUserDetails which has a one-to-one relationship with User model.
                    checkExit(extended_user_model_name)
                    extended_user_model_app_name = input("Enter extended user model APP name: ")
                    checkExit(extended_user_model_app_name)
                break
            else:
                print("\nInvalid input!!! Enter either y or n.")


        # ? Taking model name as user input and writing it in the models.py file
        while True:
            model_name = input("Enter model name to create: ")
            checkExit(model_name)
            if not f"class {model_name.lower()}" + "(models.Model):".lower() in read_modelsfile.lower():
                break
            else: print(f"\nModel {model_name} already exists in app {app_name}. Try a different name.")
            # models_file.seek(0, 2)                                              # ? Move the file pointer to the end of file. https://pynative.com/python-file-seek/    https://www.geeksforgeeks.org/python-seek-function/
            # ? In a+ mode before writing, it auto moves to EOL.
        models_file.write(
f"""\n\n\nclass {model_name}(models.Model):
""")



    # ? https://stackoverflow.com/a/49546923/16377463
    # ? https://www.skillsugar.com/how-to-prepend-content-to-a-file-in-python
    # ? https://www.quora.com/How-can-I-write-text-in-the-first-line-of-an-existing-file-using-Python
    # ? https://stackoverflow.com/a/49546923/16377463

    # ? If import doesn't exist, it copies all data of file to a variable then auto generates import at the beginning of the file and paste old content after that.
    with open(models_path, "r") as models_file:
        read_models_file = models_file.read()
    with open(models_path, "w") as models_file:
        if not "from django.db import models".lower() in read_models_file.lower():
            models_file.write(f"""from django.db import models\n""")

        if is_timezone.lower() == 'y':
            if not "from django.utils import timezone".lower() in read_models_file.lower():
                models_file.write(f"""from django.utils import timezone\n""")

        # if not "from .models import *".lower() in read_models_file.lower():
        #     models_file.write(f"""from .models import *\n""")

        if 'settings'.lower() in user_model.lower():
            if not "from django.conf import settings".lower() in read_models_file.lower():
                models_file.write(f"""from django.conf import settings\n""")
        elif 'User' == user_model:
            if not "from django.contrib.auth.models import User".lower() in read_models_file.lower():
                models_file.write(f"""from django.contrib.auth.models import User\n""")
        else:
            try:
                if not f"from {user_model_app_name}.models import {user_model}".lower() in read_models_file.lower():
                    models_file.write(f"""from {user_model_app_name}.models import {user_model}\n""")
            except: ...

        models_file.write(read_models_file)



    # ? Taking table name from user
    with open(models_path, "r") as models_file:
        read_models_file = models_file.read()
    while True:
        table_name = input("Enter database table name: ")
        checkExit(table_name)
        table_name_lower = "\'" + table_name.lower() + "\'"
        # if "db_table = " + table_name_lower or "db_table =" + table_name_lower or "db_table= " + table_name_lower or "db_table=" + table_name_lower in read_modelsfile.lower():
        if ("db_table = " + table_name_lower in read_models_file.lower()) \
        or ("db_table =" + table_name_lower in read_models_file.lower()) \
        or ("db_table= " + table_name_lower in read_models_file.lower()) \
        or ("db_table=" + table_name_lower in read_models_file.lower()):
            print(f"\nTable {table_name} already exists in app {app_name}. Try a different name.")
            continue
        # modelsfile.seek(0, 2)
        # ? Database table name appended later in the code.
        break



    # ? Taking field type & name from user and appending it in models.py file.
    print("\n##### AUTOGENERATED FIELDS - is_deleted, deleted_at, created_at, created_by, updated_at, updated_by, deleted_at, deleted_by #####")
    while True:
        while True:
            print(f"""\nChoose a field type :-
                    Foreignkey - Press 1
                    CharField - Press 2
                    TextField - press 3
                    IntegerField - press 4
                    FloatField - press 5
                    BooleanField - press 6
                    DateTimeField - press 7
                    DateField - press 8
                    Finish model creation - press 0
                    """)
                #    EmailField - press 8
                #    BinaryField - press 9

            field_type = int(input(": "))

            if field_type == 0:    # ? Autogenerate is_deleted, deleted_at, created_at, created_by, updated_at, updated_by, deleted_at, deleted_by
                related_name_initial = ''
                for i in model_name:
                    if i.isupper() == True:
                        related_name_initial += i.lower()
                while True:
                    # REMOVE THIS COMMENTS LATER.
                    # if "related_name = " + "\'" + related_name_initial in read_models_file.lower():
                    #     related_name_initial += 'a'    # ? Initial of my name :P
                    # elif "related_name =" + "\'" + related_name_initial in read_models_file.lower():
                    #     related_name_initial += 'a'    # ? Initial of my name :P
                    # elif "related_name= " + "\'" + related_name_initial in read_models_file.lower():
                    #     related_name_initial += 'a'    # ? Initial of my name :P
                    # elif "related_name = " + "\'" + related_name_initial in read_models_file.lower():
                    #     related_name_initial += 'a'    # ? Initial of my name :P
                    if ("related_name = " + "\'" + related_name_initial in read_models_file.lower()) \
                    or ("related_name =" + "\'" + related_name_initial in read_models_file.lower()) \
                    or ("related_name= " + "\'" + related_name_initial in read_models_file.lower()) \
                    or ("related_name = " + "\'" + related_name_initial in read_models_file.lower()):
                        related_name_initial += 'a'    # ? Initial of my name :P
                    else: break
                if related_name_initial == '':
                    related_name_initial = model_name
                with open(models_path, "a+") as models_file:
                    # modelsfile.seek(0, 2)    # ? Seeking to end of file
                    if is_timezone.lower() == 'y':
                        models_file.write(
f"""\n    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_created_by')
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_updated_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_deleted_by')
""")
                    else:    # ? If not using timezone
                        models_file.write(
f"""\n    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_created_by')
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_updated_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey({user_model}, on_delete=models.CASCADE, blank=True, null=True, related_name='{related_name_initial}_deleted_by')
""")
                break    # ? Inside `if field_type == 0:` which breaks inner while loop.

            while True:
                field_name = input("Enter field name: ")
                checkExit(field_name)
                field_name = field_name.lower()
                # ? Finding if user input field name exists in current model. [By setting seek() position at current model starting position and finding afterwards. So, it will not look for the field_name in previous models.]
                with open(models_path, "r") as models_file:
                    read_models_file = models_file.readlines()
                    # models_file.seek(read_models_file.index(f"class {model_name}(models.Model):"))    # ? From the position where this class of model defined, seek to that position, 0 in 2nd argument means start moving from the beginning of file, https://pynative.com/python-file-seek/#:~:text=The%20allowed    offset = after how many characters including space and newline as 1 char, whence = 0 -> starting of file, 1 -> current position, 2 -> End of file.
                    #print("----------------",read_models_file.index(f"class {model_name}(models.Model):"))
                    offset_position_list = [models_file.tell() for line in read_models_file if f"class {model_name}(models.Model):" in line]    # ? Iterates over each lines of `read_models_file` and matches user entered model and picks its current offset position. fp.tell() is used to fetch the current position offset.
                    models_file.seek(offset_position_list[0])
                    read_models_file = models_file.read()    # ? This time it will read after the seek position.
                    if f"{field_name} = models.".lower() in read_models_file.lower():
                        print(f"Field {field_name} already exists in model {model_name}. Please enter a different name.")
                    else: break
            if field_name == '0':
                break

            if field_type == 1:    # ? Adding Foreign key field
                related_name = f'{field_name}_{model_name.lower()}'
                is_user_fkey = input("Is it a user model foreign key? (y / n): ")
                checkExit(is_user_fkey)
                if is_user_fkey.lower() == 'y':
                    with open(models_path, "a+") as models_file:
                        models_file.write(f"""\n    {field_name} = models.ForeignKey({user_model}, on_delete=models.CASCADE, null=True, blank=True, related_name='{related_name}')""")
                    print(f"\nUsing model {user_model} for foreign key relationship.")
                else:
                    fkey_model = input("Enter foreign key model name: ")
                    checkExit(fkey_model)
                    # ? Checking if the foreign key model exists in same file.
                    with open(models_path, "r") as models_file:
                        read_models_file = models_file.read()
                    # ? If not exists in current model. Then asking user for foreign key model and importing in current model.
                    if not "class " + fkey_model.lower() + "(" in read_models_file.lower():
                        print(f"The model {fkey_model} doesn't exists in the models file of {app_name}.")
                        fkey_model_app = input(f"Enter APP name of model {fkey_model}: ")
                        checkExit(fkey_model_app)
                        with open(models_path, "r") as models_file:
                            read_models_file = models_file.read()
                        with open(models_path, "w") as models_file:
                            if not f"from {fkey_model_app} import {fkey_model}".lower() in read_models_file.lower():
                                models_file.write(f"""from {fkey_model_app} import {fkey_model}\n""")
                            models_file.write(read_models_file)

                    with open(models_path, "a+") as models_file:
                        models_file.write(f"""\n    {field_name} = models.ForeignKey({fkey_model}, on_delete=models.CASCADE, null=True, blank=True, related_name='{related_name}')""")
                break    # ? Inside `if field_type == 1:` which breaks inner while loop.


            elif field_type == 2:    # ? Adding CharField
                while True:
                    is_choice = input("Do you want it to be a choice field? (y / n): ")
                    checkExit(is_choice)
                    if is_choice.lower() == 'y':
                        print("\nEnter choices separated by COMMA with key value pair separated by a colon.")
                        print("Example:- value:value,another value:another value,yet another value:yet another value")
                        choice_values = input("Enter choice values like shown in the above example: ")
                        checkExit(choice_values)
                        choice_values_list = choice_values.split(",")
                        with open(models_path, "a+") as models_file:
                            models_file.write(f"""\n    {field_name.upper()}_CHOICE = (""")
                            for each_choice in choice_values_list:
                                models_file.write(f"""\n        ('{each_choice.split(':')[0].lower()}', '{each_choice.split(':')[1].lower()}'),""")
                            models_file.write(f"""\n    )""")
                        break
                    elif is_choice.lower() == 'n': break
                    else: print("Invalid choice !!!. Please enter either y or n.")
                while True:
                    want_default = input("Do you want any default value? (y / n): ")
                    checkExit(want_default)
                    if want_default.lower() == 'y':
                        default = input("Enter default value: ")
                        checkExit(default)
                        break
                    elif want_default.lower() == 'n':
                        default = 'None'
                        break
                    else: print("Invalid choice !!!. Please enter either y or n.")
                while True:
                    max_length = input("Enter max_length: ")
                    checkExit(max_length)
                    # ? Checking if max_length only contains integers. https://stackoverflow.com/a/57012038/16377463
                    pattern = re.compile("[0-9]+")
                    if pattern.fullmatch(max_length) is None:
                        print("Please enter only integers.")
                        continue
                    if int(max_length) > 255:
                        print(f"Entered value {max_length} is greater than 255. So max_length=255 is used for field {field_name}.")
                        max_length = '255'
                    break

                with open(models_path, "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.CharField(""")
                    if is_choice.lower() == 'y':
                        models_file.write(f"""choices={field_name.upper()}_CHOICE, """)
                    models_file.write(f"""max_length={max_length}, blank=True, null=True, """)
                    if default == 'None': models_file.write(f"""default={default}""")
                    else: models_file.write(f"""default='{default}'""")
                    models_file.write(f""")""")
                break    # ? Inside `if field_type == 2:` which breaks inner while loop.


            elif field_type == 3:    # ? Adding TextField
                with open(models_path, "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.TextField(blank=True, null=True)""")
                break    # ? Inside `if field_type == 3:` which breaks inner while loop.


            elif field_type == 4:    # ? Adding IntegerField
                while True:
                    is_choice = input("Do you want it to be a choice field? (y / n): ")
                    checkExit(is_choice)
                    if is_choice.lower() == 'y':
                        while True:
                            print("\nEnter choices separated by COMMA with key value pair separated by a colon.")
                            print("Example:- 1:value,2:another value,3:yet another value")
                            choice_values = input("Enter choice values like shown in above example: ")
                            checkExit(choice_values)
                            choice_pair_values_list = choice_values.split(",")
                            pattern = re.compile("[0-9]+")
                            all_int_flag = 1
                            # ? check if key is integer or not: https://stackoverflow.com/a/48940855/16377463    https://stackoverflow.com/a/9266979/16377463
                            for each in choice_pair_values_list:
                                if pattern.fullmatch(each.split(':')[0]) is None:
                                    print("Please enter only integers.")
                                    all_int_flag = 0
                                    break
                            if all_int_flag == 1:
                                break

                        with open(models_path, "a+") as models_file:
                            models_file.write(f"""\n    {field_name.upper()}_CHOICE = (""")
                            for each_choice in choice_pair_values_list:
                                models_file.write(f"""\n        ('{each_choice.split(':')[0]}', '{each_choice.split(':')[1].lower()}'),""")
                            models_file.write(f"""\n    )""")
                        break
                    elif is_choice.lower() == 'n': break
                    else: print("Invalid choice !!!. Please enter either y or n.")
                while True:
                    want_default = input("Do you want any default value? (y / n): ")
                    checkExit(want_default)
                    if want_default.lower() == 'y':
                        while True:
                            default = input("Enter default value: ")
                            checkExit(default)
                            # ? Checking if user entered default value is integer or not.
                            pattern = re.compile("[0-9]+")
                            if pattern.fullmatch(default) is None:
                                print("Please enter only integers.")
                                continue
                            break
                        break
                    elif want_default.lower() == 'n':
                        default = 'None'
                        break
                    else: print("Invalid choice !!!. Please enter either y or n.")

                with open(models_path, "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.IntegerField(""")
                    if is_choice.lower() == 'y':
                        models_file.write(f"""choices={field_name.upper()}_CHOICE, """)
                    models_file.write(f"""blank=True, null=True, """)
                    models_file.write(f"""default={default}""")
                    models_file.write(f""")""")
                break    # ? Inside `if field_type == 4:` which breaks inner while loop.


            elif field_type == 5:    # ? Adding FloatField
                while True:
                    is_choice = input("Do you want it to be a choice field? (y / n): ")
                    checkExit(is_choice)
                    if is_choice.lower() == 'y':
                        while True:
                            print("\nEnter choices separated by COMMA with key value pair separated by a colon.")
                            print("Example:- 1.1:value,2.1:another value,3.1:yet another value")
                            choice_values = input("Enter choice values like shown in above example: ")
                            checkExit(choice_values)
                            choice_pair_values_list = choice_values.split(",")
                            pattern = re.compile("[0-9.]+")
                            all_float_flag = 1
                            # ? Check if user entered choice key value is float or not
                            for each in choice_pair_values_list:
                                if pattern.fullmatch(each.split(':')[0]) is None:
                                    print("Please enter only float.")
                                    all_float_flag = 0
                                    break
                            if all_float_flag == 1:
                                break

                        with open(models_path, "a+") as models_file:
                            models_file.write(f"""\n    {field_name.upper()}_CHOICE = (""")
                            for each_choice in choice_pair_values_list:
                                # ? Adding 0 to the starting and ending of the key it it starts with a dot (.)
                                models_file.write(f"""\n        ('{each_choice.split(':')[0] if not (each_choice.split(':')[0][0] == '.') and not (each_choice.split(':')[0][-1] == '.') else ('0' + each_choice.split(':')[0]) if (each_choice.split(':')[0][0] == '.') else (each_choice.split(':')[0] + '0') if (each_choice.split(':')[0][-1] == '.') else "0.0"}', '{each_choice.split(':')[1].lower()}'),""")
                            models_file.write(f"""\n    )""")
                        break
                    elif is_choice.lower() == 'n': break
                    else: print("Invalid choice !!!. Please enter either y or n.")
                while True:
                    want_default = input("Do you want any default value? (y / n): ")
                    checkExit(want_default)
                    if want_default.lower() == 'y':
                        while True:
                            default = input("Enter default value: ")
                            checkExit(default)
                            # ? Checking if user entered default value is float or not.
                            pattern = re.compile("[0-9.]+")
                            if pattern.fullmatch(default) is None:
                                print("Please enter only float value.")
                                continue
                            break
                        break
                    elif want_default.lower() == 'n':
                        default = 'None'
                        break
                    else: print("Invalid choice !!!. Please enter either y or n.")

                with open(models_path, "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.FloatField(""")
                    if is_choice.lower() == 'y':
                        models_file.write(f"""choices={field_name.upper()}_CHOICE, """)
                    models_file.write(f"""blank=True, null=True, """)
                    models_file.write(f"""default={default}""")
                    models_file.write(f""")""")
                break    # ? Inside `if field_type == 5:` which breaks inner while loop.


            elif field_type == 6:    # ? Adding BooleanField
                while True:
                    default = input("Enter default value True or False (t / f): ")
                    checkExit(default)
                    if default.lower() == 't':
                        default = 'True'
                        break
                    elif default.lower() == 'f':
                        default = 'False'
                        break
                    else: print("Invalid default value !!!. Please enter either t or f.")

                with open(models_path, "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.BooleanField(default={default})""")
                break    # ? Inside `if field_type == 6:` which breaks inner while loop.


            elif field_type == 7:    # ? Adding DateTimeField
                while True:
                    is_auto_add_now = input("Do you want it to add current time by default? (y / n): ")
                    checkExit(is_auto_add_now)
                    if is_auto_add_now.lower() == 'y':
                        with open(models_path, "a+") as models_file:
                            if is_timezone.lower() == 'y': models_file.write(f"""\n    {field_name} = models.DateTimeField(default=timezone.now, blank=True, null=True)""")
                            else: models_file.write(f"""\n    {field_name} = models.DateTimeField(auto_now_add=True, blank=True, null=True)""")
                            break
                    elif is_auto_add_now.lower() == 'n':
                        with open(models_path, "a+") as models_file:
                            models_file.write(f"""\n    {field_name} = models.DateTimeField(blank=True, null=True)""")
                        break
                    else: print("Invalid default value !!!. Please enter either y or n.")
                break


            elif field_type == 8:    # ? Adding DateField
                while True:
                    is_auto_add_now = input("Do you want it to add current time by default? (y / n): ")
                    checkExit(is_auto_add_now)
                    if is_auto_add_now.lower() == 'y':
                        with open(models_path, "a+") as models_file:
                            if is_timezone.lower() == 'y': models_file.write(f"""\n    {field_name} = models.DateField(default=timezone.now, blank=True, null=True)""")
                            else: models_file.write(f"""\n    {field_name} = models.DateField(auto_now_add=True, blank=True, null=True)""")
                            break
                    elif is_auto_add_now.lower() == 'n':
                        with open(models_path, "a+") as models_file:
                            models_file.write(f"""\n    {field_name} = models.DateField(blank=True, null=True)""")
                        break
                    else: print("Invalid default value !!!. Please enter either y or n.")
                break


            else:
                print("\nEnter valid choice!!!")

        if field_type == 0:    # ? Breaks out of the outer while loop of field_type / field_name.
            break



    with open(models_path, "a+") as models_file:
        models_file.write(
f"""\n    def __str__(self):
        return str(self.id)
""")
        # ? ONLY FOR SFTDox - 1 #
        if 'sft_dms' in working_dir.split('\\')[-2].lower() if '\\' in working_dir else working_dir.split('/')[-2].lower():
            models_file.write(
f"""\n    def get_name(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        loggedin_user = exposed_request.user

        from sft_docs.base_functions import save_user_action
        pk = self.pk
        super().save( *args, **kwargs)

        # After insert or update action
        action='create'
        if pk:
            action='update'
        save_user_action(loggedin_user, self, action=action)
""")
        # ? ENDS SFTDox - 1 #

        models_file.write(
f"""\n    class Meta:
        db_table = '{table_name}'
""")

    # ? ONLY FOR SFTDox - 2 #
    if 'sft_dms' in working_dir.split('\\')[-2].lower() if '\\' in working_dir else working_dir.split('/')[-2].lower():
        with open(models_path, "r") as models_file:
            read_models_file = models_file.read()

        with open(models_path, "w+") as models_file:
            if not "exposed_request  = ''".lower() in read_models_file.lower():
                models_file.write(f"""exposed_request  = ''\n\n""")
            models_file.write(read_models_file)
    # ? ENDS SFTDox - 2 #

    # * ################################################ Models Generation ENDs ############################################



    # * ################################################ Admin.py Generation ###############################################

    # ? Checking if admin.py exists, if not then asking use to enter the admin.py file path.
    admin_path = f"{working_dir}/admin.py"
    model_import_text = "from .models import *"
    if not os.path.isfile(admin_path):
        admin_path = file_path_check_and_clean("Copy & Paste the path of admin.py from file explorer with drive letter: ")
        model_dir_name = models_path.split('\\')[-2] if '\\' in models_path else models_path.split('/')[-2]
        model_import_text = f"from {app_name} import {model_dir_name}"



    # ? Making a backup of user admin.py file
    with open(admin_path, "r") as readAdminFile:
        with open(f"{admin_path}.bak", "w") as readAdminBakFile:
            readAdminBakFile.write(readAdminFile.read())



    # ? Reading existing contents of admin.py file
    with open(admin_path, "r") as admin_file:
        read_admin_file = admin_file.read()



    # ? If import doesn't exist, it copies all data of file to a variable then auto generates import at the beginning of the file and paste old content after that.
    with open(admin_path, "w") as admin_file:
        if not "from django.contrib import admin".lower() in read_admin_file.lower():
            admin_file.write(f"""from django.contrib import admin\n""")

        if not model_import_text.lower() in read_admin_file.lower():
            admin_file.write(f"""{model_import_text}\n""")

        admin_file.write(read_admin_file)



    # ? Generating new admin entry in admin.py file
    with open(admin_path, "a+") as admin_file:
        admin_file.write(
f"""\n\n@admin.register({model_name})
class {model_name}(admin.ModelAdmin):
    list_display = [field.name for field in {model_name}._meta.fields]
    search_fields = ('__all__',)
""")

    # * ################################################ Admin.py Generation ENDs ##########################################



    if not only_model_generate:    # ? If user wants to create both models and CRUD APIs.

        # * ################################################ Serializers Generation ############################################
        # ? Checking if serializers.py exists, if not then asking use to enter the serializers.py file path.
        serializers_path = f"{working_dir}/serializers.py"
        model_import_text = "from .models import *"
        if not os.path.isfile(serializers_path):
            serializers_path = file_path_check_and_clean("Copy & Paste the path of serializers.py from file explorer with drive letter: ")
            model_dir_name = models_path.split('\\')[-2] if '\\' in models_path else models_path.split('/')[-2]
            model_import_text = f"from {app_name} import {model_dir_name}"



        # ? Making a backup of user serializers.py file
        with open(serializers_path, "r") as readSerializersFile:
            with open(f"{serializers_path}.bak", "w") as readSerializersBakFile:
                readSerializersBakFile.write(readSerializersFile.read())



        # ? Reading existing contents of serializers.py file
        with open(serializers_path, "r") as serializers_file:
            read_serializers_file = serializers_file.read()



        # ? If import doesn't exist, it copies all data of file to a variable then auto generates import at the beginning of the file and paste old content after that.
        with open(serializers_path, "w") as serializers_file:
            if not "from rest_framework import serializers".lower() in read_serializers_file.lower():
                serializers_file.write(f"""from rest_framework import serializers\n""")

            if not "import datetime".lower() in read_serializers_file.lower():
                serializers_file.write(f"""import datetime\n""")

            if not model_import_text.lower() in read_serializers_file.lower():
                serializers_file.write(f"""{model_import_text}\n""")

            serializers_file.write(read_serializers_file)



        # ? Generating new serializers entry in serializers.py file
        with open(serializers_path, "a+") as serializers_file:
            serializers_file.write(
f"""\n\nclass {model_name}CreateSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}EditSerializer(serializers.ModelSerializer):
    updated_by = serializers.CharField(default=serializers.CurrentUserDefault())
    updated_at = serializers.DateTimeField(default=datetime.datetime.now())
    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}DeleteSerializer(serializers.ModelSerializer):
    deleted_by = serializers.CharField(default=serializers.CurrentUserDefault())
    is_deleted = serializers.BooleanField(default=True)
    deleted_at = serializers.DateTimeField(default=datetime.datetime.now())

    class Meta:
        model = {model_name}
        fields = '__all__'
""")

        # * ################################################ Serializers Generation ENDs #######################################



        # * ################################################ Views Generation ##################################################

        # ? Checking if views.py exists, if not then asking use to enter the views.py file path.
        views_path = f"{working_dir}/views.py"
        model_import_text = "from .models import *"
        serializers_import_text = "from .serializers import *"
        if not os.path.isfile(views_path):
            views_path = file_path_check_and_clean("Copy & Paste the path of views.py from file explorer with drive letter: ")

            model_dir_name = models_path.split('\\')[-2] if '\\' in models_path else models_path.split('/')[-2]
            model_import_text = f"from {app_name} import {model_dir_name}"

            serializers_dir_name = serializers_path.split('\\')[-2] if '\\' in serializers_path else serializers_path.split('/')[-2]
            serializers_import_text = f"from {app_name} import {serializers_dir_name}"



        # ? Making a backup of user views.py file
        with open(views_path, "r") as readViewsFile:
            with open(f"{views_path}.bak", "w") as readViewsBakFile:
                readViewsBakFile.write(readViewsFile.read())



        # ? Reading existing contents of views.py file
        with open(views_path, "r") as views_file:
            read_views_file = views_file.read()



        # ? If import doesn't exist, it copies all data of file to a variable then auto generates import at the beginning of the file and paste old content after that.
        with open(views_path, "w") as views_file:
            if not "from rest_framework.permissions import IsAuthenticated".lower() in read_views_file.lower():
                views_file.write(f"""from rest_framework.permissions import IsAuthenticated\n""")

            if not "from knox.auth import TokenAuthentication".lower() in read_views_file.lower():
                views_file.write(f"""from knox.auth import TokenAuthentication\n""")

            if not "from rest_framework import generics".lower() in read_views_file.lower():
                views_file.write(f"""from rest_framework import generics\n""")

            if not "from rest_framework.views import APIView".lower() in read_views_file.lower():
                views_file.write(f"""from rest_framework.views import APIView\n""")

            if not "from rest_framework.response import Response".lower() in read_views_file.lower():
                views_file.write(f"""from rest_framework.response import Response\n""")

            if not "from django.db.models import Q, F".lower() in read_views_file.lower():
                views_file.write(f"""from django.db.models import Q, F\n""")

            if not model_import_text.lower() in read_views_file.lower():
                views_file.write(f"""{model_import_text}\n""")

            if not serializers_import_text.lower() in read_views_file.lower():
                views_file.write(f"""{serializers_import_text}\n""")

            if 'sft_dms' in working_dir.split('\\') if '\\' in working_dir else working_dir.split('/'):    # ? For SFTDox only
                if not "from sft_docs.base_paginations import OnOffPagination".lower() in read_views_file.lower():
                    views_file.write(f"""from sft_docs.base_paginations import OnOffPagination\n""")

                if not "from sft_docs.base_functions import get_sorted_by_fields".lower() in read_views_file.lower():
                    views_file.write(f"""from sft_docs.base_functions import get_sorted_by_fields\n""")

                if not f"""from sft_docs.base_decorators import (
                                    response_modify_decorator_post
                                    , response_modify_decorator_get
                                    , response_modify_decorator_update
                                    , response_modify_decorator_list_or_get_after_execution_for_onoff_pagination\n""".lower() in read_views_file.lower():
                    views_file.write(f"""from sft_docs.base_decorators import (
                                    response_modify_decorator_post
                                    , response_modify_decorator_get
                                    , response_modify_decorator_update
                                    , response_modify_decorator_list_or_get_after_execution_for_onoff_pagination
                                )\n""")

            else:
                if not "from pagination import OnOffPagination".lower() in read_views_file.lower():
                    views_file.write(f"""from pagination import OnOffPagination\n""")

                if not "from global_function import get_sorted_by_fields".lower() in read_views_file.lower():
                    views_file.write(f"""from global_function import get_sorted_by_fields\n""")

                if not "from django.db.models import Q, F".lower() in read_views_file.lower():
                    views_file.write(f"""from custom_decorator import (
                            response_modify_decorator_post
                            , response_modify_decorator_get
                            , response_modify_decorator_update
                            , response_modify_decorator_list_or_get_after_execution_for_onoff_pagination
                        )\n""")

            views_file.write(read_views_file)



        # ? Generating new views entry in views.py file
        with open(views_path, "a+") as views_file:
            views_file.write(
f"""\n\nclass {model_name}CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}CreateSerializer

    @response_modify_decorator_post
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class {model_name}EditView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}EditSerializer

    @response_modify_decorator_get
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @response_modify_decorator_update
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class {model_name}DeleteView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}DeleteSerializer

    @response_modify_decorator_update
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class {model_name}ListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = {model_name}.objects.filter(is_deleted = False).values()

    def get_filter(self):
        filter = {{}}
        exclude = {{}}
        or_filter = Q()    # If want to include `or` conditon in filter.

        searchkey = self.request.query_params.get('searchkey', None)

        if searchkey:
            filter['searchkey__icontains'] = searchkey

        queryset = self.queryset.filter(**filter).filter(or_filter).exclude(**exclude).order_by('-id')
        return queryset

    @response_modify_decorator_list_or_get_after_execution_for_onoff_pagination
    def get(self, request, *args, **kwargs):
        count = self.request.query_params.get('count')

        # Pagination Functionality
        paginator = OnOffPagination()
        page_size = self.request.GET['page_size']

        # Filter
        self.queryset = self.get_filter()

        field_name = self.request.query_params.get('ordering')
        if field_name:
            self.queryset = get_sorted_by_fields(self, self.queryset)

        if page_size == '0':
                response = self.queryset
            if count:
                count = len(response)
                return Response({{'total_count': count}})
        else:
            result_page = paginator.paginate_queryset(self.queryset, request)
            response = paginator.get_paginated_response(result_page)
            response = response.data
        return Response(response)
""")

        # * ################################################ Views Generation ENDs #############################################



        # * ################################################ Urls Generation ###################################################

        # ? Checking if urls.py exists, if not then asking use to enter the urls.py file path.
        urls_path = f"{working_dir}/urls.py"
        views_import_text = "from . import views"
        if not os.path.isfile(urls_path):
            urls_path = file_path_check_and_clean("Copy & Paste the path of urls.py from file explorer with drive letter: ")

            views_dir_name = views_path.split('\\')[-2] if '\\' in views_path else views_path.split('/')[-2]
            views_import_text = f"from {app_name} import {views_dir_name}"



        # ? Making a backup of user urls.py file
        with open(urls_path, "r") as readUrlsFile:
            with open(f"{urls_path}.bak", "w") as readUrlsBakFile:
                readUrlsBakFile.write(readUrlsFile.read())



        # ? Reading existing contents of urls.py file
        with open(urls_path, "r") as urls_file:
            read_urls_file = urls_file.read()



        # ? If import doesn't exist, it copies all data of file to a variable then auto generates import at the beginning of the file and paste old content after that.
        with open(urls_path, "w") as urls_file:
            if not "from django.urls import path".lower() in read_urls_file.lower():
                urls_file.write(f"""from django.urls import path\n""")

            if not views_import_text.lower() in read_urls_file.lower():
                urls_file.write(f"""{views_import_text}\n""")

            urls_file.write(read_urls_file)


        # ? CamelCase to snake_case convert using regex: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
        # ? Generating new urls entry in urls.py file
        
        with open(urls_path, "a+") as urls_file:
            urls_file.write(
f"""\n\nurlpatterns += [
    path('{camelcase_to_snakecase_convert(model_name)}_create/', views.{model_name}CreateView.as_view())
    , path('{camelcase_to_snakecase_convert(model_name)}_edit/<pk>/', views.{model_name}EditView.as_view())
    , path('{camelcase_to_snakecase_convert(model_name)}_delete/<pk>/', views.{model_name}DeleteView.as_view())
    , path('{camelcase_to_snakecase_convert(model_name)}_list/', views.{model_name}ListView.as_view())
]
""")

        # * ################################################ Urls Generation ENDs ##############################################



if __name__ == "__main__":
    main()







# * ARCHIVES :-
# with open(f"{working_dir}/models.py", "r") as models_file:
#     read_models_file = models_file.read()

# with open(f"{working_dir}/models.py", "w+") as models_file:
#     if not "from django.db import models".lower() in read_models_file.lower():
#         models_file.write(
# f"""from django.db import models
# \n""")
#     models_file.write(read_models_file)

# with open(f"{working_dir}/models.py", "a+") as models_file:
#     models_file.write(f""" """)
# ? Check if file exists:-
# file_name = ""
# isFile = os.path.isfile(working_dir + "/" + file_name)
# isExist = os.path.exists(working_dir + "/" + file_name)

# os.rename(f"{working_dir}/models1.py", f"{working_dir}/models.py")
# os.rename(f"{working_dir}/models1.py", f"{working_dir}/models.py")
# ! CHECK IF THESE VARIABLES ARE VALID OR NOT
# ! also create entries in admin.py, take bkup of it as well
# ! choice for only model creation or full model, slizer, views, url creation?
# ! If user press 0 any time. Current models.py is deleted and .bak file is renamed to models.py file. And same happens to other views urls slizer(check if urls and slizer exists if not exists then after cancel don't have urls and slizer leftover)
# ! define a function for the above reason and call it everytime.
# ! in charfield option for do you want digits or both char in options show example. (1,sdlkjf) or (lksdf, lksjdf)
# ! URLS SERIALIZER VIEWS BAK. RED MSG AFTER HEADLINE THAT A BAK FILE IS AUTO GENERATED CONTAINING YOUR OLDER MODELS SLIZER VIEWS URLS FILE IF YOU TERMINATED THIS PROGRAM IN B/W ELSE. AA-REMOVE IT IN BACKGROUND AFTER PROGRAM ENDS.
# ! ------------------------------------------------------------------------------------------------------------------------



def checkExit(variable : str):
    if variable == '0':
        exit()



def main():

    import os, re
    from sys import platform, exit

    print("\n\n"+"########## DJANGO MASTER API CREATOR ##########".center(120," ")+"\n")
    print("By Ashfaque Alam".center(120," ")+"\n\n")


    # ? Taking working directory input from user
    while True:
        working_dir = input("Copy & Paste the path of DJANGO APP from file explorer with drive letter.\nDjango App Path: ")
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

    # ? Making a backup of user models file
    with open(f"{working_dir}/models.py", "r") as readModelsFile:
        with open(f"{working_dir}/models.py.bak", "w") as readModelsBakFile:
            readModelsBakFile.write(readModelsFile.read())



    # ? Generating new model in models.py file
    with open(f"{working_dir}/models.py", "a+") as models_file:        # ? https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
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
            if not "class " + model_name.lower() in read_modelsfile.lower():
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
    with open(f"{working_dir}/models.py", "r") as models_file:
        read_models_file = models_file.read()
    with open(f"{working_dir}/models.py", "w") as models_file:
        if not "from django.db import models".lower() in read_models_file.lower():
            models_file.write(f"""from django.db import models\n""")

        if is_timezone.lower() == 'y':
            if not "from django.utils import timezone".lower() in read_models_file.lower():
                models_file.write(f"""from django.utils import timezone\n""")

        if not "from .models import *".lower() in read_models_file.lower():
            models_file.write(f"""from .models import *\n""")

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
    with open(f"{working_dir}/models.py", "r") as models_file:
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
                with open(f"{working_dir}/models.py", "a+") as models_file:
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
                with open(f"{working_dir}/models.py", "r") as models_file:
                    read_models_file = models_file.read()
                    models_file.seek(read_models_file.index(f"class {model_name}(models.Model):"), 0)    # ? https://pynative.com/python-file-seek/#:~:text=The%20allowed    offset = after how many characters including space and newline as 1 char, whence = 0 -> starting of file, 1 -> current position, 2 -> End of file.
                    #print("----------------",read_models_file.index(f"class {model_name}(models.Model):"))
                    read_models_file = models_file.read()    # ? This time it will read after the seek position.
                    #print("########################",read_models_file)    # ! For some reason its also reads a few line above this model
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
                    with open(f"{working_dir}/models.py", "a+") as models_file:
                        models_file.write(f"""\n    {field_name} = models.ForeignKey({user_model}, on_delete=models.CASCADE, null=True, blank=True, related_name='{related_name}')""")
                    print(f"\nUsing model {user_model} for foreign key relationship.")
                else:
                    fkey_model = input("Enter foreign key model name: ")
                    checkExit(fkey_model)
                    # ? Checking if the foreign key model exists in same file.
                    with open(f"{working_dir}/models.py", "r") as models_file:
                        read_models_file = models_file.read()
                    # ? If not exists in current model. Then asking user for foreign key model and importing in current model.
                    if not "class " + fkey_model.lower() + "(" in read_models_file.lower():
                        print(f"The model {fkey_model} doesn't exists in the models file of {app_name}.")
                        fkey_model_app = input(f"Enter APP name of model {fkey_model}: ")
                        checkExit(fkey_model_app)
                        with open(f"{working_dir}/models.py", "r") as models_file:
                            read_models_file = models_file.read()
                        with open(f"{working_dir}/models.py", "w") as models_file:
                            if not f"from {fkey_model_app} import {fkey_model}".lower() in read_models_file.lower():
                                models_file.write(f"""from {fkey_model_app} import {fkey_model}\n""")
                            models_file.write(read_models_file)

                    with open(f"{working_dir}/models.py", "a+") as models_file:
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
                        with open(f"{working_dir}/models.py", "a+") as models_file:
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

                with open(f"{working_dir}/models.py", "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.CharField(""")
                    if is_choice.lower() == 'y':
                        models_file.write(f"""choices={field_name.upper()}_CHOICE, """)
                    models_file.write(f"""max_length={max_length}, blank=True, null=True, """)
                    if default == 'None': models_file.write(f"""default={default}""")
                    else: models_file.write(f"""default='{default}'""")
                    models_file.write(f""")""")
                break    # ? Inside `if field_type == 2:` which breaks inner while loop.


            elif field_type == 3:    # ? Adding TextField
                with open(f"{working_dir}/models.py", "a+") as models_file:
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

                        with open(f"{working_dir}/models.py", "a+") as models_file:
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

                with open(f"{working_dir}/models.py", "a+") as models_file:
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

                        with open(f"{working_dir}/models.py", "a+") as models_file:
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

                with open(f"{working_dir}/models.py", "a+") as models_file:
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

                with open(f"{working_dir}/models.py", "a+") as models_file:
                    models_file.write(f"""\n    {field_name} = models.BooleanField(default={default})""")
                break    # ? Inside `if field_type == 6:` which breaks inner while loop.


            elif field_type == 7:    # ? Adding DateTimeField
                while True:
                    is_auto_add_now = input("Do you want it to add current time by default? (y / n): ")
                    checkExit(is_auto_add_now)
                    if is_auto_add_now.lower() == 'y':
                        with open(f"{working_dir}/models.py", "a+") as models_file:
                            if is_timezone.lower() == 'y': models_file.write(f"""\n    {field_name} = models.DateTimeField(default=timezone.now, blank=True, null=True)""")
                            else: models_file.write(f"""\n    {field_name} = models.DateTimeField(auto_now_add=True, blank=True, null=True)""")
                            break
                    elif is_auto_add_now.lower() == 'n':
                        with open(f"{working_dir}/models.py", "a+") as models_file:
                            models_file.write(f"""\n    {field_name} = models.DateTimeField(blank=True, null=True)""")
                        break
                    else: print("Invalid default value !!!. Please enter either y or n.")
                break


            elif field_type == 8:    # ? Adding DateField
                while True:
                    is_auto_add_now = input("Do you want it to add current time by default? (y / n): ")
                    checkExit(is_auto_add_now)
                    if is_auto_add_now.lower() == 'y':
                        with open(f"{working_dir}/models.py", "a+") as models_file:
                            if is_timezone.lower() == 'y': models_file.write(f"""\n    {field_name} = models.DateField(default=timezone.now, blank=True, null=True)""")
                            else: models_file.write(f"""\n    {field_name} = models.DateField(auto_now_add=True, blank=True, null=True)""")
                            break
                    elif is_auto_add_now.lower() == 'n':
                        with open(f"{working_dir}/models.py", "a+") as models_file:
                            models_file.write(f"""\n    {field_name} = models.DateField(blank=True, null=True)""")
                        break
                    else: print("Invalid default value !!!. Please enter either y or n.")
                break


            else:
                print("\nEnter valid choice!!!")

        if field_type == 0:    # ? Breaks out of the outer while loop of field_type / field_name.
            break



    with open(f"{working_dir}/models.py", "a+") as models_file:
        models_file.write(
f"""\n    def __str__(self):
        return str(self.id)
""")
        ##### ! ONLY FOR SFTDOX - 1 #####
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
        #!############# ENDS - 1 ##############
        models_file.write(
f"""\n    class Meta:
        db_table = '{table_name}'
""")

    ##### ! ONLY FOR SFTDOX -2 #####
    if 'sft_dms' in working_dir.split('\\')[-2].lower() if '\\' in working_dir else working_dir.split('/')[-2].lower():
        with open(f"{working_dir}/models.py", "r") as models_file:
            read_models_file = models_file.read()

        with open(f"{working_dir}/models.py", "w+") as models_file:
            if not "exposed_request  = ''".lower() in read_models_file.lower():
                models_file.write(f"""exposed_request  = ''\n\n""")
            models_file.write(read_models_file)
    #!############# ENDS - 2 ##############


    # ! AFTER MODEL CREATION MAKE CODE READABLE
    # ? slizer view urls append as well






    '''
    # ? If file not exist then creates it. And append DYNAMIC content inside it.
    if not os.path.isfile(working_dir + "/com." + project_name + "." + application_name + "/res.kts"):
        with open(working_dir + "/com." + project_name + "." + application_name + "/res.kts", "w") as file:
            # multi line f-string & use {{}} to print curly braces.
            file.write(
    f"""package com.{project_name}.{application_name}
    import androidx.appcompat.app.AppCompatActivity import android.os.Bundle

    class MainActivity : AppCompatActivity() {{
    \toverride fun onCreate(savedInstanceState: Bundle?)
    \t{{
    \t\tsuper.onCreate(savedInstanceState)
    \t\tsetContentView(R.layout.activity_main)
    \t}}
    }}
    """)
        print("res.kts file created....")
    '''

    # ? Check if file exists:-
    # file_name = ""
    # isFile = os.path.isfile(working_dir + "/" + file_name)
    # isExist = os.path.exists(working_dir + "/" + file_name)

    # ! in the end convert this .py file to .exe file and give it to the user.
    # ? Make well documented code as you might need to edit this file later so you can do it easily later on.
    # * have interactive messages for the user to see the progress of execution of code.

    # ? Make .exe file of the script.
    # ? https://towardsdatascience.com/how-to-easily-convert-a-python-script-to-an-executable-file-exe-4966e253c7e9
    # ? pip install auto-py-to-exe
    # ? auto-py-to-exe (Enter), in settings - change output location.


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



if __name__ == "__main__":
    main()
# Imports required for the program :
# ===================================
#   read_parquet => Function to read the content of ".parquet" file into a dataframe.
#   read_csv => Function to read the content of ".csv" file into a dataframe.
#
#   os => Module required to access environment variables.
#
#   dump => Function required to convert an object into standard json object.
#
#   smart_open => Function to stream files stored in S3
#
#   load_dotenv => Function to load env variables

from pandas import read_csv, read_parquet
import os
from smart_open import smart_open
from json import dump
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()


# Function data_processing :
# ========================
#
# Arguments => students (type : dataframe) : dataframe containing students' data from "students.csv" file.
#              teachers (type : dataframe) : dataframe containing teachers' data from "teachers.parquet" file.
# 
# Description => Traverse the dataframes and maps the teachers to the students via the class_id, i.e., "cid" and then convert it into standard json object
#               and store it in "data.json" file
def data_processing(students, teachers):

    json_data = []

    for index, row in teachers.iterrows():
        tmp = {'teacher_id': row['id'],
               'teacher_name': row['fname'] + ' ' + row['lname'],
               'class_id': row['cid']}

        teacher_obj = []
        for ind, _row in students[students['cid'] == row['cid']].iterrows():
            student_obj = {'student_id': _row['id'],
                      'student_name': _row['fname'] + ' ' + _row['lname']}
            teacher_obj.append(student_obj)

        tmp['students'] = teacher_obj
        json_data.append(tmp)

    # Writing json data to a file
    with open('data.json', 'w') as student_object:
        dump(json_data, student_object, indent=4)

    # print the json data on console
    print(json_data)


# Function to load the files from current directory, parse it's data and send for processing.
def local_files(teachers_path, students_path):
    try:
        teachers = read_parquet(teachers_path)
        students = read_csv(students_path, delimiter='_')
        data_processing(students, teachers)

    except FileNotFoundError as e:
        print(e)


# Function to load the files from S3 bucket, using "smart_open" and then parse it's data and send for processing.
def s3_files(aws_access_key, aws_secret_key, bucket_name, object_key_teacher, object_key_student):
    try:
        path = 's3://{}:{}@{}/'.format(aws_access_key, aws_secret_key, bucket_name)
        teachers = read_parquet(smart_open(path + object_key_teacher))
        students = read_csv(smart_open(path + object_key_student), delimiter='_')
        data_processing(students, teachers)

    except Exception as e:
        print(e)



if __name__ == "__main__":
    try: 
        aws_access_key = os.environ.get('AWS_ACCESS_KEY')
        aws_secret_key = os.environ.get('AWS_SECRET_KEY')
        bucket_name = os.environ.get('AWS_BUCKET_NAME')
        object_key_teacher = os.environ.get('TEACHERS_FILE_NAME')
        object_key_student = os.environ.get('STUDENTS_FILE_NAME')
        teachers_path = os.path.join(os.environ.get('TEACHERS_FILE_PATH'), object_key_teacher)
        students_path = os.path.join(os.environ.get('STUDENTS_FILE_PATH'), object_key_student)

        print('Please choose correct option to choose file')
        print('1.) From Local\n2.) From S3\n3.) Quit\n')
        choice = input("> ")
        if choice == '1':
            local_files(teachers_path, students_path)
        elif choice == '2':
            if aws_access_key and aws_secret_key and bucket_name:
                s3_files(aws_access_key, aws_secret_key, bucket_name, object_key_teacher, object_key_student)
            else:
                print('Please Provide AWS credentials in environment file')
                exit(0)
        elif choice == '3':
            print('Bye...')
            exit(0)
        else:
            print('Wrong choice, Please choose correct option and try agian...\nBye...')
            exit(0)
            
    except Exception as e:
        print(e)

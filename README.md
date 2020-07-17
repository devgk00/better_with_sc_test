# **Task :**
An application that processes the two data files { students.csv , teachers.parquet }. The application should use both files to output a report in json listing each teacher with the students being taught by him / her.
The application will be used with both local files (where the absolute file paths will be passed in Environment file) and files stored in aws S3 (where the Access key, Secret Key and the bucket urls of files will be passed in Environment file).


Docker is also being used to inject the property of containerism, so that the code can be used as an atomic container.

> ## Note:
>   The AWS credentials and file urls (in case of fetching from S3) or the file paths (in case of fetching from local system) are to be entered in **".env"** file.
 

# **Modules used :**
- os
- json
- pandas
- dot_env
- smart_open
 

# **System requirements :**
- OpenSSL 1.1.1
- python 3.5


# **Set up environment :**
> - ### **Create an environment :**
> ```python
> python -m virtualenv venv
> ```
> 
>  
> - ### **Activate environment :**
> ```python
> source venv/bin/activate
> ```
> 
>  
> - ### **Install requirements**
> ```python
> pip install -r requirements.txt
> ```


# Environment variable setting :
TEACHERS_FILE_NAME='teachers.parquet'
STUDENTS_FILE_NAME='students.csv'

> - ### If file is in local then pass the file path upto the directory containing those files in .env file
TEACHERS_FILE_PATH=''
STUDENTS_FILE_PATH=''

> - ### If file is in S3 Provide AWS Access Key, AWS Secret key and Bucket name upto directory containing those files in .env file 
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_BUCKET_NAME=


# **Commands to run :**
- ### **Git clone** :
```git
git clone https://github.com/devgk00/better_with_sc_test.git
```

- ### **Command to run :**
```python
python3 -m venv /path/to/task_env        # could be any path
source /path/to/task_env/bin/activate
pip install -r requirements.txt
python3 src/readfile-app.py
```


- ### **Docker commands :**
```dockerfile
$ docker build -t my-python-app .
$ docker run -it --rm --name my-running-app my-python-app
```

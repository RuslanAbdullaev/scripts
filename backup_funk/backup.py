'''
ФУНКЦИЯ БЕКАПИРОВАНИЯ ФАЙЛА В ОБЬЕКТНОЕ ХРАНИЛИЩЕ ЯНДЕКС ОБЛАКА.
Для работы функции должна быть установленна библиотека boto3 (pip3 install boto3)
Так же нужно настроить авторизацию, для этого создаем 2 файла:
1 .aws/config
Добавляем туда 
[default]
            region=ru-central1

2 .aws/credentials
Добавляме туда 
[default]
            aws_access_key_id = $(Ваш key_id)
            aws_secret_access_key = $(Ваш access_key)     

Исопльзование функции:
Вызываем ее таким образом backup('file in yout server', 'backet in cloud', 'name your file in cloud;)
'''
import boto3


def backup(file_name, bucket_name, object_name):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )
    try:
        s3.upload_file(file_name, bucket_name, object_name)
    except Exception as e:
        print('SOMETHING WRONG')


if __name__ == '__main__':
    pass
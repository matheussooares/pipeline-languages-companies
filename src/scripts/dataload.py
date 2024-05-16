import requests
import base64

class load_repository:
    def __init__(self,username,access_token):
        self.USERNAME = username
        self.API_BASE_URL = 'https://api.github.com'
        self.access_token = access_token
        self.HEADERS = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def crate_repository(self,name_repository,description):
        data = {
            'name': name_repository,
            'description': description,
            'private': False
        } 
        reponse = requests.post(f'{self.API_BASE_URL}/user/repos', 
                                json = data,
                                headers=self.HEADERS)
        print(f"A criação do repositório gerou o status code: {reponse.status_code}")

    def push_data(self,path_dataset,path_remote,name_repo):
        with open(path_dataset, 'rb') as file:
            file_content = file.read()

        encoded_content = base64.b64encode(file_content)

        url = f'{self.API_BASE_URL}/repos/{self.USERNAME}/{name_repo}/contents/{path_remote}'

        data = {
            'message': 'add file csv',
            'content': encoded_content.decode('utf-8')
        }

        reponse = requests.put(url, json = data,headers=self.HEADERS)
        
        print(f"A carga do arquivo gerou o status code: {reponse.status_code}")


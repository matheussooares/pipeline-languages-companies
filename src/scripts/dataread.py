import requests
from pandas import DataFrame 
class get_repository:
    def __init__(self,owner,access_token):
        self.owner = owner
        self.API_BASE_URL = 'https://api.github.com'
        self.access_token = access_token
        self.HEADERS = {'Authorization': 'Bearer ' + self.access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

    def get(self, num_page):
        repos_list = []
        # Percorre as páginas do repositório da amazon
        for page_num in range(1, num_page):
            # Tratamento de erro
            try:
                url_page = f'{self.API_BASE_URL}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url_page, headers=self.HEADERS)#,verify=False)
                response.status_code
                repos_list.append(response.json())
            # caso ocorra algum erro
            except:
                repos_list.append(None)
        return repos_list
    
    def read(self,repos_list,attr):
        respo_val = []
        for page in repos_list:
            for repo in page:
                respo_val.append(repo[attr])
        return respo_val
    
    def data_repository(self,num_page,attrs):
        repo = self.get(num_page)
        data = DataFrame
        for attr in attrs:
            val = self.read(repo,attr)
            data[attr] = val
        return data


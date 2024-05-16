from scripts import dataread as dh
from scripts import dataload as dl

access_token = 'coloque aqui'
num_page = 20
attrs = ['name','language']

owners = ['amzn','netflix','spotify']
for owner in owners:
    repos = dh.get_repository(owner='amzn',
                                access_token=access_token)

    data  = repos.data_repository(num_page=num_page,
                                    attrs=attrs)
    
    path = f'src\\data\\dataset-{owner}.csv'

    data.to_csv(path)

username = 'matheussooares'
repo = 'pipeline-languages-companies'
description =  'Pipeline de dados: extraindo, transformando e carregando dados acerca das linguagens de programação utilizadas por algumas empresas'

dl.crate_repository(name_repository=repo,
                    description =  description)


repo = dl.load_repository(username=username,access_token=access_token)
for owner in owners:
    path_datase = f'src/data/dataset-{owner}.csv'
    path_remote = f'src/data/dataset-{owner}.csv'
    repo.push_data(path_dataset=path_datase,
                path_remote = path_remote,
                name_repo =repo)


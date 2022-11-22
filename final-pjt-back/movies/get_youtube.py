import requests
import json


# with open('final-pjt-back/movies/fixtures/movies.json', 'r', encoding="UTF-8") as json_file:
with open('all_2.json', 'r', encoding="UTF-8") as json_file:
    data_json_list = json.load(json_file)




def make_url(url, params):
    for key, value in params.items():
        url = url + f'&{key}={value}'
    return url

def get_movies(movie_id):
    
    params = {
        'api_key': 'b62d15126d65f2f351e77aa02c968e67',
        'language':'en-US',
    }
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?'
    maked_url = make_url(URL, params)

    response = requests.get(maked_url).json()  # 받아오기
    return (response.get('results')[0].get('key'), response.get('results')[0].get('site'))          # 안에꺼만 추출

###################
    
movies = []
errs = []
sites = []
result = []

for idx, data in enumerate(data_json_list):
    print(f'{idx}    ' + data_json_list[idx]['fields']['title'] + '  ' , end='')
    try:
        key, site = get_movies(data['pk'])
        data_json_list[idx]['fields']['key'] = key
        if site == "YouTube":
            result.append(data_json_list[idx])
    except:
        data_json_list[idx]['fields']['key'] = '0'
        errs.append(data_json_list[idx]['fields']['title'])
    print(data_json_list[idx]['fields']['key'])

file_path = "./allllllll.json" # 주소
    
with open(file_path, 'w', encoding="UTF-8") as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)
print(len(result))
print(errs)
print(sites)

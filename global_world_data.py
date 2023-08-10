import requests
base_url='https://zucwflxqsxrsmwseehqvjmnx2u0cdigp.lambda-url.ap-south-1.on.aws/mentorskool/v1/sales'
limit = 100
offset = 0
final_data=[]
while offset < 500:
    params={"limit":limit, "offset":offset}
    response = requests.get(base_url, params=params,headers={"access_token":"fe66583bfe5185048c66571293e0d358"})
    print(response.status_code)
    if response.status_code == 200:
        data=response.json()
        if len(data['data'])==0:
            break
        final_data.extend(data['data'])
        offset+=limit
    else:
        print("failed")
        break
import pandas as pd    
df = pd.json_normalize(final_data)
df
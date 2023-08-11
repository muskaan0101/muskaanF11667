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

unique_values=df['product.product_name'].nunique()
df[df['product.product_name']=='Balt Solid Wood Rectangular Table']
df[df['product.product_name']== 'Strathmore #10 Envelopes, Ultimate White']["product.sizes"]
df['product.sizes'].unique()[1]
# develop a function that accepts the data frame and name of the product and 
# returns the list of sizes of that specific product that they have in stock.

def list_of_sizes(data,product_name):
    size_list = df[df["product.product_name"]==product_name]["product.sizes"].unique()[0]
    print(size_list)

product_name=df[["product.product_name"]].iloc[2]["product.product_name"]
product_name
list_of_sizes(df,product_name)

# to find size range of all products and arrange them in descending order of no. of sizes available
#  and find the product with maximum no. of sizes available

unique_sizes_list= [df["product.product_name"].unique()[i] for i in range(unique_values)]
unique_sizes_list
len(unique_sizes_list)
for i in unique_sizes_list:
    if list_of_sizes(df,i) is not None or 'null':
        print(i, list_of_sizes(df,i))

list_of_sizes(df,'Mitel 5320 IP Phone VoIP phone')

    

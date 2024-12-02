#####################
###### IMPORTS ######
#####################
from google.oauth2.service_account import Credentials
from google.cloud import bigquery


#####################
####### LOGIC #######
#####################

key_path = '/PATH/TO/SERVICE_ACCOUNT.JSON'

credentials = Credentials.from_service_account_file(
    key_path,
    scopes=['https://www.googleapis.com/auth/cloud-platform'])

def run_bq_query(sql):

    # BQ CLIENT
    bq_client = bigquery.Client(credentials = credentials)

    # RUN QUERY
    job_config = bigquery.QueryJobConfig()
    client_result = bq_client.query(sql, job_config=job_config)

    job_id = client_result.job_id

    # RETURN DATA FRAME
    df = client_result.result().to_arrow().to_pandas()
    print(f"Finished job_id: {job_id}")
    return df

query = """
SELECT 
    a.id, a.body.content AS Question, ARRAY_AGG(b.body.content IGNORE NULLS) AS Reply
FROM 
    `PROJECT_ID.DATASET_ID.TABLE_ID` a, a.replies AS b
GROUP BY 
    a.id, a.body.content
ORDER BY 
    a.id
"""

df = run_bq_query(query)

# COMBINE ALL THE REPLIES INTO ONE BIG STRING
df['Reply'] = df['Reply'].apply(lambda x : ' '.join(x))

# SAVE IT INTO JSON FILE
df.to_json('data-v3.json', orient='records', lines=True)
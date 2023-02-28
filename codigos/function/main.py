import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import pandas_gbq
from google.cloud import bigquery

client = bigquery.Client()
project_id = 'semiotic-joy-379201'
table_destination = 'raw.base_vendas'

def sheets_sales(event,context):

  scope = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

  keyfile = 'oauth.json'

  creds = ServiceAccountCredentials.from_json_keyfile_name(
      keyfile)

  client = gspread.authorize(creds)

  sheets_id = ['1JdYB7J0oYcBi5vyKgJ3yQcuGhElQTPGF0sJ46Nzqz7o','1HcVFDK2EYFoiJRD8wWcyOfnpBn2EvzeVUBOmpiDroxU','1DULSHz708AXHWIhXB2GqDBEmeaY6eG1DLYw61JfD3JM']
  for id in sheets_id:
    sheet = client.open_by_key(
      id).sheet1

    result = sheet.get_all_records()

    df = pd.DataFrame(result)
    df.ID_MARCA = df.ID_MARCA.astype(str)
    df.ID_LINHA = df.ID_LINHA.astype(str)
    df.DATA_VENDA = df.DATA_VENDA.astype(str)
    df.QTD_VENDA = df.ID_LINHA.astype(str)
   
    load_bq = pd.DataFrame(df)
    pandas_gbq.to_gbq(load_bq, table_destination, project_id = project_id, if_exists = 'append')

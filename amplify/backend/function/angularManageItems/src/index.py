import json
import boto3

# テーブルスキャン
# https://business.ntt-east.co.jp/content/cloudsolution/column-try-20.html
def operation_scan(table):
    scanData = table.scan()	# scan()メソッドでテーブル内をscan。一覧を取得
    items = scanData['Items']	# 応答からレコード一覧を抽出
    print(items)	# レコード一覧を表示
    return scanData

# レコード追加・更新
def operation_put(table, body):
    print('put')
    print(type(body))
    print(body)
    putResponse = table.put_item(	# put_item()メソッドで追加・更新レコードを設定
        Item={	# 追加・更新対象レコードのカラムリストを設定
            'id': body['id'],
            'name': body['name'],
        }
    )
    if putResponse['ResponseMetadata']['HTTPStatusCode'] != 200:	# HTTPステータスコードが200 OKでないか判定
        print(putResponse)	# エラーレスポンスを表示
    else:
        print('PUT Successed.')
    
    return putResponse

# レコード削除
def operation_delete(table, body):
    delResponse = table.delete_item(	# delete()メソッドで指定テーブルを削除
       Key={	# Keyオブジェクトで削除対象レコードのキー設定
            'id': body['id'],
       }
    )
    if delResponse['ResponseMetadata']['HTTPStatusCode'] != 200:	# HTTPステータスコードが200 OKでないか判定
        print(delResponse)	# エラーレスポンスを表示
    else:
        print('DEL Successed.')
    return delResponse

def handler(event, context):
    print('received event:')
    print(json.dumps(event))

    dynamoDB = boto3.resource("dynamodb")
    table = dynamoDB.Table("amplify-items") 

    request_body: dict = event['body']
    print(type(request_body))
    print(request_body)

    # statusCode = 200
    # headers = {
    #         "Content-Type": "application/json",
    #         'Access-Control-Allow-Headers': '*',
    #         'Access-Control-Allow-Origin': '*',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    # }

    response_body: dict = None
    if event['httpMethod'] == 'GET':
        response_body = operation_scan(table)

    if event['httpMethod'] == 'POST' or event['httpMethod'] == 'PUT':
        response_body = operation_put(table, request_body)
    

    if event['httpMethod'] == 'DELETE':
        response_body = operation_delete(table, request_body)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response_body)
        # 'body': json.dumps('Hello from your new Amplify Python lambda!')
    }
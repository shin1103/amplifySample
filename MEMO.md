# API GatewayのIP制限について
https://docs.aws.amazon.com/apigateway/latest/developerguide/openapi-extensions-policy.html

https://dev.classmethod.jp/articles/api-gateway-resouce-policy-ip-address/
上記サイトにはGUIでテンプレートが作成され、そこから特定のＩＰのみアクセス可能にするような方法が記載されていた。

# Lambdaにマネージポリシーを設定する方法
https://aws.amazon.com/jp/premiumsupport/knowledge-center/cloudformation-attach-managed-policy/
を参考に作成。

amplify/backend/function/angularManageItems/angularManageItems-cloudformation-template.json
のルートに次の項目を追加
```json
  "Parameters": {
    "awsExampleManagedPolicyParameterOne": {
      "Type": "String",
      "Description": "Role for DynamoDB Access"
    },
    "awsExampleManagedPolicyParameterTwo": {
      "Type": "String",
      "Description": "Role for DynamoDB Access"
    }
  },
```
続いてResouces,LambdaExecutionRole,Propertiesに次の項目を追加
```
        "ManagedPolicyArns": [
          {
            "Ref": "awsExampleManagedPolicyParameterOne"
          },
          {
            "Ref": "awsExampleManagedPolicyParameterTwo"
          }
        ]
```

amplify/team-provider-info.json
awsExampleManagedPolicyParameterOne,awsExampleManagedPolicyParameterTwoに具体的なポリシーを追加
```json
      "function": {
        "angularManageItems": {
          "deploymentBucketName": "amplify-angularamplifypc-dev-73222-deployment",
          "s3Key": "amplify-builds/angularManageItems-6945535668514e697147-build.zip",
          "awsExampleManagedPolicyParameterOne": "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
          "awsExampleManagedPolicyParameterTwo": "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole"
        }
      }

```

# DynamoDBの接続について
https://business.ntt-east.co.jp/content/cloudsolution/column-try-20.html
上記サイトを参考に作成。いくつか動かないところがあったり、APIGatewayとLambdaが密結合になるやり方が良くないので、こちらで修正。

# PythonのラムダがDeployできない
Cloud9のEC2はPythonのバージョンが3.7系にあるのに対し、Amplifyは3.8系であることが求められる。
そのため、pyenvをインストールして異なるバージョンを入れる。
https://github.com/pyenv/pyenv

インストール後、次のコマンドで動くはず。
```bash
pyenv install 3.8.12
pyenv global 3.8.12
```

To run this example execute terraform:

```sh
export APP_NAME=interns-party
export TF_VAR_app_name=interns-party
terraform init -backend-config "workspace_key_prefix=${APP_NAME}"
terraform plan
```
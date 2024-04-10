#!/usr/bin/env sh
export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=${VAULT_DEV_ROOT_TOKEN_ID}

# enable jwt auth method
vault auth enable jwt
vault policy write jwt - <<EOF
# Allow working with secrets
path "secret/*" {
    capabilities = [ "create", "read", "update", "delete", "list" ]
}
EOF
vault write auth/jwt/role/jwt_role \
  role_type=jwt \
  bound_subject="subject" \
  user_claim="my_claim" \
  token_policies="jwt"
vault write auth/jwt/config jwt_validation_pubkeys="$(cat /jwt_public_key.pem)"

# enable approle auth method
vault auth enable approle
vault policy write approle - <<EOF
# Allow working with secrets
path "secret/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}
EOF
vault write auth/approle/role/approle_role token_policies="approle"
echo "Approle credentials"
vault read auth/approle/role/approle_role/role-id | grep -i "role_id" | awk '{printf "role_id: %s\n", $2}'
vault write -f auth/approle/role/approle_role/secret-id | grep -i "secret_id" | awk '{printf "secret_id: %s\n", $2}' | head -n 1

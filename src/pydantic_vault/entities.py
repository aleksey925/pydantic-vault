from typing import NamedTuple, Union

from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict as _SettingsConfigDict
from typing_extensions import TypedDict


class SettingsConfigDict(_SettingsConfigDict, total=False):
    vault_url: Union[str, None]
    vault_token: Union[str, SecretStr, None]
    vault_namespace: Union[str, None]
    vault_certificate_verify: Union[bool, str, None]
    vault_auth_mount_point: Union[str, None]
    vault_role_id: Union[str, None]
    vault_secret_id: Union[str, SecretStr, None]
    vault_kubernetes_role: Union[str, None]
    vault_auth_path: Union[str, None]
    vault_jwt_role: Union[str, None]
    vault_jwt_token: Union[str, SecretStr, None]


class HvacClientParameters(TypedDict, total=False):
    namespace: str
    token: str
    verify: Union[bool, str]


class HvacReadSecretParameters(TypedDict, total=False):
    path: str
    mount_point: str


class AuthMethodParameters(TypedDict, total=False):
    mount_point: str
    path: str


class Approle(NamedTuple):
    role_id: str
    secret_id: SecretStr


class Kubernetes(NamedTuple):
    role: str
    jwt_token: SecretStr


class VaultJwt(NamedTuple):
    role: str
    token: SecretStr

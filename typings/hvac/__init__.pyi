from typing import Any

class ApproleStub:
    @staticmethod
    def login(
        role_id: str,
        secret_id: str | None = None,
        use_token: bool = True,
        mount_point: str = "approle",
    ) -> dict[str, Any]:
        raise NotImplementedError()

class KubernetesStub:
    @staticmethod
    def login(
        role: str,
        jwt: str,
        use_token: bool = True,
        mount_point: str = "kubernetes",
    ) -> dict[str, Any]:
        raise NotImplementedError()

class AuthStub:
    approle: ApproleStub
    kubernetes: KubernetesStub
    jwt: JwtStub

class JwtStub:
    @staticmethod
    def jwt_login(role: str, jwt: str, path: str | None = None) -> dict[str, Any]: ...

class Client:
    auth: AuthStub
    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        verify: bool | str = True,
        timeout: int = 30,
        allow_redirects: bool = True,
        namespace: str | None = None,
    ) -> None:
        raise NotImplementedError()
    def read(self, path: str) -> dict[str, Any]:
        raise NotImplementedError()

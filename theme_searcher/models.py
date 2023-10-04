from pydantic import BaseModel


class Theme(BaseModel):
    theme: str
    phrases: list[str]

    def __str__(self) -> str:
        # return f"{self.theme}: {', '.join(self.phrases)};"
        return self.theme

    def __hash__(self) -> int:
        return hash(self.theme)


class ThemeSearchReq(BaseModel):
    query: str


class SuccessResp(BaseModel):
    success: bool

from pydantic import BaseModel

class CommentsInput(BaseModel):
    comments: list[str]
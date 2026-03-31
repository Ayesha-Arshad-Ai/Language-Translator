from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    target_language: str = Field(..., min_length=1)
    source_language: str = Field(default="auto")
    tone: str = Field(default="neutral")
    preserve_formatting: bool = Field(default=True)


class TranslationResponse(BaseModel):
    status: str
    source_language: str
    target_language: str
    translated_text: str
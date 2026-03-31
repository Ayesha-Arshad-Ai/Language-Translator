from fastapi import FastAPI, HTTPException
from groq import Groq

from app.config import settings
from app.prompt import build_translation_messages
from app.schemas import TranslationRequest, TranslationResponse


app = FastAPI(
    title="Language Translator API",
    version="1.0.0"
)

client = Groq(api_key=settings.GROQ_API_KEY)


@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    try:
        messages = build_translation_messages(
            text=request.text,
            target_language=request.target_language,
            source_language=request.source_language,
            tone=request.tone,
            preserve_formatting=request.preserve_formatting,
        )

        completion = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=messages,
            temperature=settings.TEMPERATURE,
            max_completion_tokens=settings.MAX_COMPLETION_TOKENS,
            top_p=settings.TOP_P,
            stream=False,
        )

        translated_text = completion.choices[0].message.content.strip()

        return TranslationResponse(
            status="success",
            source_language=request.source_language,
            target_language=request.target_language,
            translated_text=translated_text,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
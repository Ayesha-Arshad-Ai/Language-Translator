def build_translation_messages(
    text: str,
    target_language: str,
    source_language: str = "auto",
    tone: str = "neutral",
    preserve_formatting: bool = True,
) -> list:
    system_prompt = f"""
You are an expert multilingual translator.

Translate the user's text into {target_language}.

Rules:
1. Detect source language automatically if source_language is "auto".
2. Preserve meaning, intent, and context.
3. Use tone: {tone}.
4. Return only translated text.
5. Do not add notes or explanations.
6. {"Preserve formatting and line breaks." if preserve_formatting else "Formatting may be adjusted slightly."}
""".strip()

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text.strip()},
    ]
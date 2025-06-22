import openai
def ai_reviewer(draft: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Review clarity, style, grammar."},
                  {"role": "user", "content": draft}]
    )
    return resp.choices[0].message.content

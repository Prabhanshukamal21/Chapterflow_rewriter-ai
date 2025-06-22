from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

def rewrite_chapter(text):
    print("✍️ Rewriting using Groq + LLaMA 3...")

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # You can change to "mixtral-8x7b-32768" or "gemma-7b-it"
        messages=[
            {"role": "system", "content": "You are a helpful and creative writing assistant."},
            {"role": "user", "content": f"Rewrite the following text to improve grammar, clarity, and narrative style:\n\n{text}"}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

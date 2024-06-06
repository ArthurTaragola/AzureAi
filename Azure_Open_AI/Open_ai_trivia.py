import os
import sys
from openai import AzureOpenAI

def generate_trivia(category):
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2024-02-01",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    instructions='Return 3 trivia quesions of the category "%s" with 4 corresponding possible answers with one of them being the real answer. Your output should be in the following format: \
    [{ \
        "question": "example question1", \
        "options": ["A) possibilityA", "B) possibilityB", "C) possibilityC", "D) possibilityD"], \
        "correct_option": "B" \
    }, \
    { \
        "question": "example question2", \
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], \
        "correct_option": "C", \
    }]"' % (category)

    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=[
            {"role": "system", "content": "Assistant that writes trivia questions"},
            {"role": "user", "content": instructions}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python open_ai_trivia.py <category>")
        sys.exit(1)

    category = sys.argv[1]
    output = generate_trivia(category)
    print(output)
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 환경변수를 로드
load_dotenv()

# api키 설정
api_key = os.getenv('OPENAI_API_KEY')

# 클라이언트 인스턴스를 생성
client = OpenAI(api_key=api_key)

# api를 호출할 준비!
def test_api():
    try:
        chat_completion = client.chat.completions.create(
            # model / message / max_tokens
            model = "gpt-4o-mini",
            messages = [
                {
                    "role" : "user",
                    "content" : "안녕 반가워"  
                }
            ],
            max_tokens = 50  
        )
        # 결과 출력
        print(chat_completion.choices[0].message.content.strip())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_api()
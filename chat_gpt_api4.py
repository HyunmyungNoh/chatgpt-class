import gradio as gr
import requests

def chat_gpt_api(user_input):
    #API 엔드포인트 URL
    url = "https://open-api.jejucodingcamp.workers.dev/"

    #API에 요청에 사용할 데이터
    data = [
        {"role": "system", "content": "너는 전문 뉴스 작성자야. 제목, 기자 이름, 작성 날짜, 주요 내용, 그리고 결론을 포함한 뉴스 기사를 작성해줘."},
        {"role": "user", "content": f"다음 주제에 대한 뉴스 기사를 작성해주세요 : {user_input}. 최신 트랜드, 사실 포함, 300단어 이내로 작성 : 제목, 기자, 작성 날짜, 내용, 결론으로 구성해주세요."} 
    ]

    #HTTP 요청 헤더
    headers = {
        "Content-Type": "application/json"
    }

# POST 요청 보내기 / 데이터는 JSON 형태로 보냄
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error : {response.status_code}, {response.text}"

#뉴스기사 생성
def generate_news_article(input_text):
    # ChatGPT API를 사용하여 뉴스 기사 생성
    raw_article = chat_gpt_api(input_text)
    return raw_article

#웹 화면 구축
iface = gr.Interface(
    fn=generate_news_article, #텍스트가 입력!
    inputs=gr.Textbox(lines=2, placeholder="뉴스 주제를 입력하세요..."),
    outputs="text",
    title="AI 뉴스 생성기",
    description="뉴스 주제를 입력하시면 AI가 선별된 정보를 가지고 트랜드와 사실을 반영한 기사를 생성해 줍니다."
)

iface.launch() 
import gradio as gr
import requests

def chat_gpt_api(user_input):
    #API 엔드포인트 URL
    url = "https://open-api.jejucodingcamp.workers.dev/"

    #API에 요청에 사용할 데이터
    data = [
        {"role": "system", "content": "너는 한국어 응답에 대한 도우미야. 다음 문장을 영어로 번역해줘."},
        {"role": "user", "content": f"{user_input}"} 
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
    
# 챗봇 구현! 챗봇 관리
def chatbot(input_text):
    # 한국어 영어로 번역하는 기능
    response = chat_gpt_api(input_text)
    
    return f"한국어 입력 {input_text}, chat gpt 응답은 {response}"

#웹 화면 구축
iface = gr.Interface(
    fn=chatbot, #텍스트가 입력!
    inputs=gr.Textbox(lines=2, placeholder="한국어로 질문을 입력하세요"),
    outputs="text",
    title="한국 to 영어 번역기",
    description="한국어를 입력하면 영어로 번역해줍니다."
)

iface.launch()
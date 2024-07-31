import requests

def chat_gpt_api(user_input):
    # API 엔드포인트 URL -> 특정 API 서비스에 요청을 보내기 위한 URL
    url = "https://open-api.jejucodingcamp.workers.dev/"
    
    # API에 요청에 사용할 데이터
    # Chat GPT의 역할 -> 점심 메뉴 추천 요리사
    # 우리의 역할 -> 이 요리사한테 정보를 줘서 추천을 받는 역할
    data = [
        {"role": "system", "content": "환자의 생활 지침을 알려주세요. 프롬프트에 적힌 대로 수행해주세요"},
        {"role": "user", "content": user_input}
    ]
    
    # HTTP 요청 헤더
    # headers는 HTTP 요청시에 사용할 헤더 정보를 설정
    # Content-Type : 요청 본문의 타입을 설정
    # application/json : JSON 형태로 데이터를 보낼 때 사용
    headers = {
        "Content-Type" : "application/json"
    }
    
    # API 요청 / POST 방식으로 요청을 보내고, 데이터는 JSON 형태로 보냄
    response = requests.post(url, json=data, headers=headers)
    
    # 응답 처리
    if response.status_code == 200: #200일때 정상
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return "API 요청에 실패했습니다."
    
# main 함수!

def main():
    print("이 프로그램은 환자들의 생활 루틴을 제안하는 서비스입니다. (종료를 원하시면 q를 입력해 주세요)")
    
    while True:
        user_input = input("앓고 계신 질환을 입력하세요 : ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
        prompt = f"""
        {user_input}에 대한 생활 습관을 다음 형식으로 제공해주세요.
        단 이 환자는 아무 것도 모르는 상태이기 때문에 최대한 쉬운 언어로 말해주세요:
        질병: {user_input}
        1. [수면]
           - 설명: [2-3문장으로 수면에 대한 설명]
        2. [식단]
           - 설명: [2-3문장으로 식단에 대한 설명]
        3. [운동]
           - 설명: [2-3문장으로 운동에 대한 설명]
        4. [약]
          - 설명: [2-3문장으로 복용해야 할 약에 대한 설명]
        5. [주의점]
          - 설명: [10문장까지만 {user_input}을 가진 환자가 주의해야 할 점 설명]
        """
        
        response = chat_gpt_api(prompt)
        print(f"{response}")
        
if __name__ == "__main__":
    main()
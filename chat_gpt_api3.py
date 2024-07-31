import requests

def chat_gpt_api(user_input):
    # API 엔드포인트 URL -> 특정 API 서비스에 요청을 보내기 위한 URL
    url = "https://open-api.jejucodingcamp.workers.dev/"
    
    # API에 요청에 사용할 데이터
    # Chat GPT의 역할 -> 건강에 대한 정보 공유
    # 우리의 역할 -> 이 요리사한테 정보를 줘서 추천을 받는 역할
    data = [
        {"role": "system", "content": "너는 건강에 대한 도우미야. 건강에 대한 정보들을 공유해줘"},
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
    
# print_result 함수!
def print_result(step, prompt, response):
    print(f"단계 {step} :")
    print(f"프롬프트 : {prompt}")
    print(f"모델 응답 : {response}")
    print("\n")
    
# 중간부분!
def run_prompt_engineering_example(step=None):
    
    
    #단계 1 : 초기 프롬프트
    if step is None or step == 1:
        initial_prompt = "건강한 생활습관 대해서 설명해주세요."
        response1 = chat_gpt_api(initial_prompt)
        print_result(1,initial_prompt,response1)

    # 단계 2: 반복적 개선
    if step is None or step == 2:
        improved_prompt = """
        일상생활에서 실천할 수 있는 건강한 습관 5가지를 설명해주세요.
        각 습관에 대해 그 중요성과 실천 방법을 포함해주세요.
        """
        response2 = chat_gpt_api(improved_prompt)
        print_result(2, improved_prompt, response2)

    # 단계 3: 단계별 지시 추가
    if step is None or step == 3:
        step_by_step_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 다음 단계를 따라주세요:
        1. 건강한 식습관 2가지를 설명하세요.
        2. 규칙적인 운동의 중요성과 간단한 운동 루틴을 제안하세요.
        3. 충분한 수면의 이점과 좋은 수면 습관을 설명하세요.
        4. 스트레스 관리를 위한 기술 2가지를 제안하세요.
        5. 이러한 습관들이 전반적인 건강에 미치는 영향을 요약하세요.
        """
        response3 = chat_gpt_api(step_by_step_prompt)
        print_result(3, step_by_step_prompt, response3)

    # 단계 4: 예시 제공
    if step is None or step == 4:
        example_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 각 항목을 다음 형식으로 작성해주세요:
        습관: [습관 이름]
        중요성: [1-2문장 설명]
        실천 방법: [구체적인 실천 방법 2-3가지]

        예시:
        습관: 충분한 수분 섭취
        중요성: 수분은 체내 대사와 체온 조절에 필수적입니다. 적절한 수분 섭취는 피부 건강과 집중력 향상에도 도움을 줍니다.
        실천 방법:
        - 매일 아침 기상 직후 물 한 잔 마시기
        - 식사 때마다 물 한 잔씩 곁들이기
        - 운동 전후로 충분한 수분 보충하기

        위 예시와 같은 형식으로 총 4가지 건강한 생활 습관을 설명해주세요.
        """
        response4 = chat_gpt_api(example_prompt)
        print_result(4, example_prompt, response4)

    # 단계 5: 제약 조건 설정
    if step is None or step == 5:
        
        constrained_prompt = """
        건강한 생활 습관 가이드를 작성해주세요. 각 항목을 다음 형식으로 작성해주세요:
        습관: [습관 이름]
        중요성: [1-2문장 설명]
        실천 방법: [구체적인 실천 방법 2-3가지]

        예시:
        습관: 충분한 수분 섭취
        중요성: 수분은 체내 대사와 체온 조절에 필수적입니다. 적절한 수분 섭취는 피부 건강과 집중력 향상에도 도움을 줍니다.
        실천 방법:
        - 매일 아침 기상 직후 물 한 잔 마시기
        - 식사 때마다 물 한 잔씩 곁들이기
        - 운동 전후로 충분한 수분 보충하기

        위 예시와 같은 형식으로 총 4가지 건강한 생활 습관을 설명해주세요.
        
        앞서 설명한 건강한 생활 습관 가이드를 바탕으로, 바쁜 직장인을 위한 버전을 만들어주세요. 다음 조건을 반드시 지켜주세요:
        - 각 습관은 하루 15분 이내로 실천할 수 있어야 합니다.
        - 특별한 장비나 시설이 필요 없는 방법만 포함해주세요.
        - 과학적 근거를 바탕으로 한 조언만 제공해주세요.
        - 특정 제품이나 브랜드를 언급하지 마세요.
        총 3가지 습관을 위 조건에 맞춰 설명해주세요.
        """
        response5 = chat_gpt_api(constrained_prompt)
        print_result(5, constrained_prompt, response5)
        
# main 함수!

def main():
    print("이 프로그램은 여행지를 추천해주는 서비스입니다. (종료를 원하시면 q를 입력해 주세요)")
    
    while True:
        user_input = input("실행할 단계를 선택해주세요 (1~5)  만약에 전부다 수행하고 싶으면 all을 입력해주세요 : ")
        
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
        if user_input.lower() == 'all':
            run_prompt_engineering_example() # 모든 것을 출력!
        elif user_input in ['1','2','3','4','5']:
            step = int(user_input)
            run_prompt_engineering_example(step)
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자나 all을 입력해주세요.")
        
if __name__ == "__main__":
    main()
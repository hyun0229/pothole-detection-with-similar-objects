# pothole-detection-with-similar-objects

---
## 개요

본 저장소는 "유사 객체 데이터를 통한 포트홀 객체 인식 정확도 향상 연구" 논문에 사용된 코드를 포함하고 있습니다. 본 연구는 포트홀 탐지의 정확도를 향상시키기 위해 유사 객체 동시 학습 방법을 제안합니다.

## 목차

1. [소개](#소개)
2. [설치](#설치)
3. [데이터셋](#데이터셋)
4. [모델](#모델)
5. [결과](#결과)

## 소개

본 연구는 최근 이상기후로 인한 포트홀 발생 증가에 대응하기 위해 포트홀 탐지의 정확도를 향상하는 학
습법을 제안합니다. 도로 위에는 포트홀뿐 아니라 맨홀, 이미 보수된 포트홀과 같이 포트홀과 외형적으로 유사
한 여러 개체가 존재하며 이들은 포트홀 자동 탐지 시스템의 정확성을 저하되게 하는 주요 원인으로 작용합니다. 이를 해결하기 위해서 본 연구에서는 이러한 개체들을 포트홀과 함께 별도의 클래스로 분류하여 동시에 
학습시키는 방법을 채택하여 각 클래스 간의 차이점을 학습시킵니다. 

## 설치

환경 설정 및 필요한 종속성을 설치


Window 환경에서 Coda를 사용하였으며 다른 환경에서의 지원여부는 확인되지 않았습니다.

1. 저장소를 클론:
    ```bash
    git clone https://github.com/hyun0229/pothole-detection-with-similar-objects.git
    cd pothole-detection-improvement
    ```

2. 가상 환경을 생성 및 활성화:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. 필요한 패키지를 설치:
    ```bash
    pip install -r requirements.txt
    ```
 
## 데이터셋
본 저장소는 데이터셋을 포함하고 있지 않습니다.

본 연구에서 AIhub의 '지자체 도로 정비 AI 학습용 데이터'를 사용했으며 사용된 데이터셋은 세 가지 주요 그룹으로 분류됩니다:

1. 포트홀 이미지
2. 포트홀 + 보수된 포트홀 이미지
3. 포트홀 + 맨홀 이미지


| 데이터셋       | 원본 이미지 수 | 수직 대칭 이미지 수 | 총 이미지 수 |
| -------------- | -------------- | ----------------- | ----------- |
| 포트홀         | 400            | 400               | 800         |
| 포트홀 + 보수된 포트홀  | 200            | 200               | 400         |
| 포트홀 + 맨홀           | 200            | 200               | 400         |
| **총합**       | 800            | 800               | 1600        |


데이터셋은 총 1600장의 이미지로 구성되어 있으며 train, value, test 세트로 나누어집니다.

## 모델

동일한 데이터셋을 사용하여 모델 A, B를 학습하였습니다:

- **모델 A:** 포트홀 단일 클래스로 학습
- **모델 B:** 포트홀, 보수된 포트홀, 맨홀 이미지를 각각 별도의 클래스로 학습

 
| 모델  | 클래스 이름         | 클래스 정보          |
| ----- | ------------------- | -------------------- |
| A 모델| 0                   | 포트홀               |
| B 모델| 0                   | 포트홀               |
|       | 1                   | 보수된 포트홀        |
|       | 2                   | 맨홀                 |



## 결과

모델의 성능은 포트홀 클래스의 Average Precision (AP) 지표를 통해 평가되었습니다:

- **모델 A:** AP = 68.5%
- **모델 B:** AP = 76.6%

| 클래스 | AP         |
| ----- | ------------------- |
| 0| 0.766                   |
| 1| 0.913                   |
| 2| 0.945                   |


모델 B는 맨홀과 보수된 포트홀과 같은 유사 객체가 있는 환경에서도 포트홀을 정확하게 탐지하는 성능을 보여주며 포트홀 탐지 정확도가 크게 향상되었습니다.

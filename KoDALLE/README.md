#  그림 그리는 인공지능 Text to Image

사람에 대한 묘사를 기반으로 이미지를 자동으로 생성하는 [KoDALLE](https://github.com/KR-HappyFace/KoDALLE) 기반 모델

| Text | Generated montage |
| --- | --- |
| 볼이 넓은 계란형 얼굴이며 앞머리가 이마의 양쪽 끝을 가리고 있어 모양은 보이지 않는다.   오른쪽 턱의 각진 부분이 왼쪽에 비해 아래로 내려와 있고 왼쪽은 약간 완만한 형태이다.  턱끝으로 내려오는 턱모양은 약간 둥근형으로 보인다. 왼쪽의 볼이 더 평평하고 넓은 편이다. | ![](assets/output1.png) |
| 이마라인 가운데가 아래로 살짝 내려와 있어 M모양을 띄고 있으며 가르마의 구분 없이 모두 올려져 있으나 헤어라인 가운데에서 살짝 오른편으로 헤어젤을 바른 듯 조금 나뉜 모습도 보인다. 옆머리는 왼쪽은 귓바퀴 시작 지점까지 내려와 있으며 오른쪽은 귀에 바로 닿을 듯 내려와 있다. | ![](assets/output2.png) |
| 각진 얼굴에 광대는 매끄럽고 큰 볼을 가지고 있어 약간 후덕한 인상을 준다. 눈매의 라인이 부드러워 따뜻한 인상을 주며 누구에게나 친절을 베풀 것 같은 인물이다. 입매가 부드럽고 약간 얇은 듯해서 말하기 좋아하는 사람 같기도 하다. | ![](assets/output3.png) |
| 눈매와 입매가 부드럽고 미소짓고 있는 모습으로  성품이 착하고 유한 사람으로 보인다. 약간 여성스러운 성격일 수도 있을 것 같으며 누구에게나 친절하고 어진 모습으로 대해주는 편안한 사람으로 느껴진다. | ![](assets/output4.png) |
| 눈이 작고 여성스러운 이미지를 가지고 있으며 입술은 도톰하다. | ![](assets/output5.png) |

## Dataset

[페르소나 기반의 가상 인물 몽타주 - AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=618)

![https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=618](assets/dataset.jpg)

## Training Process

1. Download dataset from above
2. Preprocess dataset using [preprocess.ipynb](preprocess.ipynb)
3. Train [VQGAN](https://github.com/kairess/taming-transformers)
4. Extract `klue/roberta-large` models (run [extract_emb_models.py](extract_emb_models.py))
5. Train KoDALLE

## Inference Pipeline

- [test.ipynb](test.ipynb)
- [Gradio App](app.py)

## Wandb Logs

- KoDALLE [https://wandb.ai/kairess/optimization?workspace=user-kairess
](https://wandb.ai/annie26751/Kodalle?nw=nwuserannie2675)
---

## 한국어 텍스트 인코더
Experimentations were conducted with the following Korean Transformers Models’ embedding layers. The team selected klue/roberta-large as baseline in the repository considering the size of the model.

- **[klue/roberta-large](https://huggingface.co/klue/roberta-large): Vocab Size of 32000, Embedding Dimension of 1024.**
- [KoGPT Trinity of SKT](https://huggingface.co/skt/ko-gpt-trinity-1.2B-v0.5): Vocab Size of 51200, Embedding Dimension of 1920.
- [KoGPT of Kakao Brain](https://huggingface.co/kakaobrain/kogpt): Vocab Size of 64512, Embedding Dimension of 4096.

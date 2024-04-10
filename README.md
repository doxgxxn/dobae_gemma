# 도배 하자 질의 응답 처리 : 한솔데코 시즌2 AI 경진대회
preparation
```
    $ git clone https://github.com/doxgxxn/dobae_gemma.git
    $ cd dobae_gemma
    $ pip install -r requirements.txt
```
    
RUN 
```
    $ python
    >>> from ai_assistant import AIassistant
    >>> AIassistant = AIassistant()
    >>> answer = AIassistant.query("쌀풀은 무엇이며 어떤 용도로 사용되나요?")
    >>> print(answer)
```

    '쌀풀은 쌀을 가공하여 제작된 재료로, 친환경적이고 접착력이 밀풀에 비해 약 1.5배 좋으며 내구성이 좋은 재료입니다. 이러한 장점을 갖고 있지만, 부착면과 내부 마감용으로 사용되며, 가벼우면서도 부드러운 질감을 가지고 있어 인테리어에 활용됩니다.'

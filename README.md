# 🎨 GLM-Image Streamlit App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/jmpark333/glm-image)

Z.AI의 **GLM-Image** API를 사용하여 텍스트에서 이미지를 생성하는 Streamlit 웹 애플리케이션입니다.

GLM-Image는 오픈소스 이미지 생성 모델로, 특히 **텍스트 렌더링**과 **복잡한 레이아웃**에서 압도적인 성능을 발휘합니다. 포스터, PPT, 인포그래픽, 레시피 카드 등 텍스트가 많이 포함된 이미지 생성에 최적화되어 있습니다.

## ✨ 주요 기능

- 🔑 **사용자별 API Key 입력** - 각 사용자가 자신의 Z.AI API Key를 사용
- 🎨 **고품질 이미지 생성** - GLM-Image 모델을 통한 고품질 이미지 생성
- 📐 **다양한 크기 지원** - 1024x1024, 1280x1280, 1024x768, 768x1024
- 🖼️ **여러 이미지 동시 생성** - 한 번에 최대 4개의 이미지 생성
- 💾 **다운로드 기능** - 생성된 이미지를 PNG 형식으로 다운로드
- 🌐 **예제 프롬프트 제공** - 다양한 상황별 프롬프트 예제

## 🚀 온라인 체험

바로 사용해보세요: **[https://share.streamlit.io/jmpark333/glm-image](https://share.streamlit.io/jmpark333/glm-image)**

## 📦 로컬에서 실행하기

### 1. 리포지토리 클론

```bash
git clone https://github.com/jmpark333/glm-image.git
cd glm-image
```

### 2. Z.AI API Key 발급

1. [https://z.ai](https://z.ai) 방문
2. 회원가입 (무료)
3. 마이페이지 → API Keys → Create New API Key
4. 발급된 API Key 복사

### 3. Python 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 앱 실행

```bash
streamlit run app.py
```

### 5. API Key 입력

앱이 실행되면 왼쪽 사이드바에 발급받은 API Key를 입력하세요.

## 🔐 Streamlit Cloud에 배포하기

### 자동 배포 설정

이 앱은 GitHub와 Streamlit Cloud가 연동되어 있어, 코드를 푸시하면 자동으로 배포됩니다.

1. **Fork 또는 직접 연동**
   - 이 리포지토리를 Fork하거나, 자신의 GitHub 리포지토리와 연동

2. **Streamlit Cloud에서 배포**
   - [https://share.streamlit.io/new](https://share.streamlit.io/new) 방문
   - 리포지토리 선택: `jmpark333/glm-image` (또는 본인의 Fork)
   - 메인 파일: `app.py`
   - **Secrets 설정** (중요!):
     ```
     [secrets]
     zai_api_key = "zai_xxxxxxxxxxxxxxxx"
     ```

3. **배포 확인**
   - 약 1-2분 내에 자동 배포 완료
   - 배포된 URL에서 앱 접속 가능

### Secrets 설정 방법

Streamlit Cloud에서 API Key를 안전하게 관리하려면:

1. Streamlit Cloud Dashboard 접속
2. 해당 앱 선택 → Settings → Secrets
3. 다음 내용 추가:
```toml
zai_api_key = "zai_xxxxxxxxxxxxxxxx"
```

## 📖 사용법

1. **API Key 입력** - 왼쪽 사이드바에서 Z.AI API Key 입력
2. **프롬프트 작성** - 생성할 이미지를 영어로 설명
3. **설정 선택** - 이미지 크기, 생성 수 선택
4. **이미지 생성** - "이미지 생성" 버튼 클릭
5. **다운로드** - 생성된 이미지를 PNG로 다운로드

### 프롬프트 작성 팁

- **영어로 작성** - 더 좋은 결과를 얻을 수 있습니다
- **구체적일수록 좋음** - "a cat"보다 "a cute orange cat sitting on a windowsill"
- **레이아웃 명시** - "왼쪽 상단에 제목, 오른쪽에 이미지"
- **텍스트 포함** - GLM-Image는 텍스트 렌더링에 강점이 있습니다

### 예제 프롬프트

**상업용 포스터**
```
A modern sale event poster with '50% OFF' in bold text at the center,
clean design, vibrant colors, professional quality
```

**레시피 카드**
```
A beautifully designed recipe card for chocolate cake,
with title 'Chocolate Cake Recipe', ingredient list on the left,
step-by-step instructions on the right, magazine style
```

**PPT 슬라이드**
```
A professional business presentation slide about AI technology,
with title area, bullet points, and a simple chart illustration,
clean and modern corporate style
```

## 🛠️ 기술 스택

- **Streamlit** - Python 웹 애플리케이션 프레임워크
- **Requests** - HTTP 클라이언트
- **Pillow** - 이미지 처리
- **Z.AI API** - GLM-Image 이미지 생성 API

## 📚 관련 링크

- [Z.AI 공식 웹사이트](https://z.ai)
- [GLM-Image 문서](https://docs.z.ai/guides/image/glm-image)
- [GLM-Image Hugging Face](https://huggingface.co/zai-org/GLM-Image)
- [GLM-Image 블로그 포스트](https://z.ai/blog/glm-image)

## ⚠️ 참고사항

- **API 사용료**: Z.AI API는 사용량에 따라 과금됩니다. 무료 크레딧이 제공되지만, 초과 시 비용이 발생할 수 있습니다.
- **Rate Limit**: 무료 계정은 분당 호출 횟수 제한이 있습니다.
- **개인정보**: API Key는 절대 공개 저장소에 올리지 마세요. Streamlit Cloud Secrets를 사용하세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 제공됩니다.

## 🙏 acknowledgments

- [Z.AI](https://z.ai) - GLM-Image API 제공
- [Streamlit](https://streamlit.io) - 웹 애플리케이션 프레임워크

## 📞 문의

- GitHub Issues: [https://github.com/jmpark333/glm-image/issues](https://github.com/jmpark333/glm-image/issues)
- Email: jmpark333@gmail.com

---

Made with ❤️ by [jmpark333](https://github.com/jmpark333)

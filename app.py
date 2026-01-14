import streamlit as st
import requests
import os
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="GLM-Image 이미지 생성",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
<style>
    .main-header {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2196F3;
        margin: 20px 0;
    }
    .warning-box {
        background-color: #fff3e0;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff9800;
        margin: 10px 0;
    }
    .success-box {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin: 20px 0;
    }
    .generate-btn {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 40px;
        border-radius: 25px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s;
    }
    .generate-btn:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar - API Key Configuration
with st.sidebar:
    try:
        st.image("https://z.ai/favicon.ico", width=80)
    except:
        st.markdown("### 🎨")
    st.title("⚙️ 설정")

    # API Key input
    st.markdown("### 🔑 API Key")

    # Check if running on Streamlit Cloud with secrets
    api_key = None
    if hasattr(st, "secrets") and "zai_api_key" in st.secrets:
        api_key = st.secrets["zai_api_key"]
        st.success("✅ Streamlit Cloud API Key가 설정되어 있습니다.")
    else:
        api_key = st.text_input(
            "Z.AI API Key를 입력하세요",
            type="password",
            placeholder="zai_xxxxxxxxxxxxxxxx",
            help="https://z.ai에서 무료로 발급받을 수 있습니다.",
        )

    st.markdown("---")

    # API Key info
    st.markdown(
        """
    **📖 API Key 발급 방법**<br><br>
    1️⃣ [https://z.ai](https://z.ai) 방문<br>
    2️⃣ 회원가입 (무료)<br>
    3️⃣ 마이페이지 → API Keys → 발급<br>
    4️⃣ 발급된 키를 위에 입력하세요
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Model info
    st.markdown("### 📚 GLM-Image 정보")
    st.markdown(
        """
    **GLM-Image**는 Z.AI가 개발한 하이브리드 이미지 생성 모델입니다.<br><br>
    🔹 **강점**: 텍스트 렌더링, 복잡한 레이아웃<br>
    🔹 **아키텍처**: Auto-regressive + Diffusion<br>
    🔹 **용도**: 포스터, PPT, 인포그래픽 등
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>Made with ❤️ by <a href='https://github.com/jmpark333' target='_blank'>jmpark333</a></div>",
        unsafe_allow_html=True,
    )

# Main content
st.markdown(
    """
<div class="main-header">
    <h1>🎨 GLM-Image 이미지 생성</h1>
    <p>텍스트 설명만으로 고품질 이미지를 생성하세요</p>
</div>
""",
    unsafe_allow_html=True,
)

# Check if API key is provided
if not api_key:
    st.markdown(
        """
    <div class="warning-box">
        <b>⚠️ API Key가 필요합니다</b><br><br>
        왼쪽 사이드바에서 Z.AI API Key를 입력하세요.<br>
        API Key는 <a href="https://z.ai" target="_blank">https://z.ai</a>에서 무료로 발급받을 수 있습니다.
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.stop()

# Main generation interface
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### ✍️ 프롬프트 작성")

    # Prompt input
    prompt = st.text_area(
        "생성할 이미지를 설명하세요",
        height=150,
        placeholder="예: A beautifully designed poster with '50% OFF' text in the center, modern and clean style...",
        help="영어로 작성하면 더 좋은 결과를 얻을 수 있습니다. GLM-Image는 텍스트 렌더링에 특히 강력합니다.",
    )

    # Example prompts
    with st.expander("💡 예제 프롬프트"):
        st.markdown("""
        **1. 상업용 포스터**
        ```
        A modern sale event poster with '50% OFF' in bold text at the center,
        clean design, vibrant colors, professional quality
        ```

        **2. 레시피 카드**
        ```
        A beautifully designed recipe card for chocolate cake,
        with title 'Chocolate Cake Recipe', ingredient list on the left,
        step-by-step instructions on the right, magazine style
        ```

        **3. PPT 슬라이드**
        ```
        A professional business presentation slide about AI technology,
        with title area, bullet points, and a simple chart illustration,
        clean and modern corporate style
        ```

        **4. 인포그래픽**
        ```
        An infographic explaining climate change, with icons, text labels,
        and data visualizations, educational style with clear typography
        ```
        """)

with col2:
    st.markdown("### ⚙️ 생성 설정")

    # Image size
    size = st.selectbox(
        "이미지 크기",
        options=["1024x1024", "1280x1280", "1024x768", "768x1024"],
        index=1,
        help="이미지의 해상도를 선택하세요. 더 큰 크기는 더 많은 크레딧을 소모합니다.",
    )

    # Number of images
    n = st.slider(
        "생성할 이미지 수",
        min_value=1,
        max_value=4,
        value=1,
        help="한 번에 여러 이미지를 생성할 수 있습니다.",
    )

    # Advanced options
    with st.expander("🔧 고급 설정"):
        quality = st.selectbox(
            "품질",
            options=["standard", "high"],
            index=0,
            help="high 품질은 더 나은 결과를 제공하지만 더 오래 걸립니다.",
        )

# Generate button
st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🎨 이미지 생성", use_container_width=True, type="primary")

if generate_btn:
    if not prompt:
        st.markdown(
            """
        <div class="warning-box">
            <b>⚠️ 프롬프트를 입력하세요</b><br>
            생성할 이미지를 설명하는 텍스트를 입력해주세요.
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        # Show loading
        with st.spinner("🎨 이미지 생성 중... (약 30~60초 소요)"):
            try:
                # API call
                response = requests.post(
                    "https://api.z.ai/api/paas/v4/images/generations",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json={"model": "glm-image", "prompt": prompt, "size": size, "n": n},
                    timeout=120,
                )

                # Check response
                if response.status_code == 200:
                    result = response.json()

                    if "data" in result and len(result["data"]) > 0:
                        st.markdown(
                            f"""
                        <div class="success-box">
                            <b>✅ 이미지 생성 완료!</b><br>
                            {len(result["data"])}개의 이미지가 생성되었습니다.
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

                        # Display images
                        for i, img_data in enumerate(result["data"]):
                            st.markdown(f"### 🖼️ 이미지 {i + 1}")

                            # Display image
                            try:
                                # Download image data first
                                img_response = requests.get(img_data["url"])
                                img_response.raise_for_status()

                                # Store raw content for reuse
                                img_content = img_response.content

                                # Display image from fresh BytesIO
                                img = Image.open(BytesIO(img_content))
                                st.image(img, use_container_width=True)

                                # Download button with new BytesIO instance
                                img_bytes = BytesIO()
                                img.save(img_bytes, format="PNG")
                                img_bytes.seek(0)

                                st.download_button(
                                    label=f"📥 이미지 {i + 1} 다운로드",
                                    data=img_bytes,
                                    file_name=f"glm_image_{i + 1}.png",
                                    mime="image/png",
                                    use_container_width=True,
                                )

                                st.markdown("---")

                            except requests.exceptions.RequestException as e:
                                st.error(
                                    f"이미지 다운로드 중 오류가 발생했습니다: {str(e)}"
                                )
                            except Exception as e:
                                st.error(
                                    f"이미지 로드 중 오류가 발생했습니다: {str(e)}"
                                )

                        # Show prompt used
                        with st.expander("📝 사용된 프롬프트"):
                            st.text(prompt)

                    else:
                        st.markdown(
                            f"""
                        <div class="warning-box">
                            <b>⚠️ 이미지 생성 실패</b><br>
                            응답에서 이미지 데이터를 찾을 수 없습니다.<br>
                            API 크레딧이 충분한지 확인해주세요.<br><br>
                            응답 데이터: {result}
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

                elif response.status_code == 401:
                    st.markdown(
                        """
                    <div class="warning-box">
                        <b>⚠️ API Key 인증 실패</b><br><br>
                        API Key가 올바르지 않습니다.<br>
                        다시 확인해주세요.
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

                elif response.status_code == 429:
                    st.markdown(
                        """
                    <div class="warning-box">
                        <b>⚠️ Rate Limit 초과</b><br><br>
                        너무 많은 요청을 보냈습니다.<br>
                        잠시 후 다시 시도해주세요.
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

                else:
                    st.markdown(
                        f"""
                    <div class="warning-box">
                        <b>⚠️ 오류 발생</b><br><br>
                        상태 코드: {response.status_code}<br>
                        메시지: {response.text}
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

            except requests.exceptions.Timeout:
                st.markdown(
                    """
                <div class="warning-box">
                    <b>⚠️ 요청 시간 초과</b><br><br>
                    이미지 생성이 너무 오래 걸리고 있습니다.<br>
                    다시 시도해주세요.
                </div>
                """,
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.markdown(
                    f"""
                <div class="warning-box">
                    <b>⚠️ 오류 발생</b><br><br>
                    {str(e)}
                </div>
                """,
                    unsafe_allow_html=True,
                )

# Footer
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #666; padding: 20px;">
    <p>
        <b>GLM-Image Streamlit App</b><br><br>
        Powered by <a href="https://z.ai" target="_blank">Z.AI</a> |
        <a href="https://docs.z.ai/guides/image/glm-image" target="_blank">API 문서</a> |
        <a href="https://github.com/jmpark333/glm-image" target="_blank">GitHub</a>
    </p>
    <p><small>이 앱은 Z.AI API를 사용합니다. API 사용에 따른 비용이 발생할 수 있습니다.</small></p>
</div>
""",
    unsafe_allow_html=True,
)

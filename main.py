import streamlit as st
import replicate

st.markdown('# :rainbow[AI Генератор картинок]')

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]


def configure_sidebar():
    with st.sidebar:
        with st.form('my_form'):
            width = st.number_input('Ширина картинки', min_value=256, max_value=2048, value=1024, step=16)
            hight = st.number_input('Высота картинки', min_value=256, max_value=2048, value=1024, step=16)
            prompt = st.text_area("Введите промпт")
            submitted = st.form_submit_button("Отправить", type="primary")

        return {
            "width": width,
            "hight": hight,
            "prompt": prompt,
            "submitted": submitted,
        }


def main_page(width: int,
              hight: int,
              prompt: str,
              submitted: bool,
              ):
    if submitted:
        with st.spinner('В процессе...'):
            result = replicate.run(
                "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
                input={"width": width,
                       "hight": hight,
                       "prompt": prompt,
                       }
            )
            image = result[0]
            with st.container():
                st.image(image, caption='Ваше изображение')


def main():
    data = configure_sidebar()
    main_page(**data)


if __name__ == "__main__":
    main()

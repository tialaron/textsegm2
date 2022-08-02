import os

import streamlit as st
from PIL import Image


#cwd = os.getcwd()
#st.write(cwd)
image1 = Image.open('pipesegm.png')
spisok_doc = os.listdir('/app/original_docs/')

st.set_page_config(layout='wide')
st.header('Лабораторная работа:"Сегментация договоров".')
st.write('В юридической практике очень часто приходится иметь дело с текстовыми документами. Одним из направлений Искусственного Интеллекта, занимающегося изучением текстовых данных, является так называемая NER-задача.')
st.write('Сама по себе задача NER (Named Entity Recognition) сводится к обнаружению некоторых именованных сущностей в тексте. Примером таких сущностей может являться локация, личность, организация и др.')
st.write('В данной работе Вам предлагается посмотреть на функционирование готовой нейронной сети, которая была обучена распознавать параграфы документов отвечающие за одну из следующих "сущностей": Условия, Запреты, Цены, Сроки, Неустойки, Геолокации.')
with st.expander("Общая схема"):
  st.image(image1)
  st.markdown(
    '''
    \n**Этапы:**
    \n1. База данных типовых договоров:
    \nСодержит более 100 текстовых файлов типовых договоров купли, продажи, аренды, размещения вклада, банковского обслуживания и т.д.
    \n2. Библиотека слоев:
    \nСодержит набор слоев, используемых нейронной сетью.  [tensorflow](https://www.tensorflow.org/).
    \n3. Настройка модели:
    \nУстанавливается тип и количество слоев, а также количество нейронов в них.
    \n4. Обучение модели:
    \nВо время этого процесса нейросеть читает документы и обучается их воспроизводить.
    \n5. Проверка точности:
    \nНа этом этапе программист проверяет работу сети с помощью тестовых документов.
    \n6. Функция обработки текстового документа:
    \nПреобразует документ, который выдает нейронная сеть, в понятный для человека вид.
    \n7. Загрузка документа из нескольких предложенных:
    \nНа выбор студенту предлагается пять документов, которые можно отправить в нейронную сеть на обработку. В результате получается документ с выделенными цветными параграфами.
    \n8. Приложение Streamlit:
    \nОтображение документа.
    ''')
st.write('Каждый распознанный параграф выделяется своим цветом:')
st.markdown(f'<h1 style="color:#c71585;font-size:14px;">{"розовый  - Условия"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#ff0000;font-size:14px;">{"красный - Запреты"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#228b22;font-size:14px;">{"зеленый - Стоимость, всё про цены и деньги"}</h1>',unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#4169e1;font-size:14px;">{"синий   - Всё про сроки"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#ff8c00;font-size:14px;">{"оранжевый - Неустойка"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#00ffff;font-size:14px;">{"голубой - Всё про адреса и геолокации"}</h1>',unsafe_allow_html=True)


def doc_lines(textor_any):
  counter_str = 0
  for i in textor_any:
    if i == '\n':
      counter_str+=1
  return counter_str


counter2 = st.slider('Выберите номер документа для обработки с помощью слайдера',0,4,1)

col1, col2 = st.columns(2)
with col1:
  with st.container():
    st.subheader('Оригинал договора')
    filename1 = '/app/original_docs/'+spisok_doc[counter2]
    f = open(filename1 ,'r',encoding="utf8")
    textor = f.read()
    st.write(textor)

with col2:
  with st.container():
    st.subheader('Договор обработанный нейронной сетью.')
    filename2 = '/app/modified_docs/'+spisok_doc[counter2]
    f2 = open(filename2 , 'r', encoding="utf8")
    textor2 = f2.read()
    #st.write(textor2)
    all_lines = doc_lines(textor2)
    all_doc = []
    str_doc = ''
    for i in textor2:
      if i != '\n':
        str_doc+=i
      elif i == '\n':
        all_doc.append(str_doc)
        str_doc = ''
    for j in range(all_lines):
      if '<s1>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#c71585">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s2>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#ff0000">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s3>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#228b22">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s4>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#4169e1">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s5>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#ff8c00">{all_doc[j]}</h6>', unsafe_allow_html=True)
      elif '<s6>' in all_doc[j]:
        st.markdown(f'<h6 style="color:#00ffff">{all_doc[j]}</h6>', unsafe_allow_html=True)
      else:
        st.write(all_doc[j])

st.write('Ссылка на ноутбук для обучения сети')
st.write('https://colab.research.google.com/drive/1uyA2iJPC0QPIj4FAqs9irSmVh6sPXq7r?usp=sharing')

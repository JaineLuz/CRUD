import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    Cursos = ['Informática', 'Mineração']
    
    with st.form(key='insert'):
        input_course = st.selectbox(label='Insira o Curso', options=Cursos)
        input_mat = st.text_input(label='Insira a sua matrícula:')
        input_name = st.text_input(label='Insira o nome:')
        input_endereco = st.text_area(label='Insira o seu endereço:')
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_course, input_mat, input_name, input_endereco, input_age)
            st.success('Aluno incluido com sucesso')
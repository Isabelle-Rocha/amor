import streamlit as st


@st.dialog("<3")
def caixa_modal(texto):
    st.write(texto)
@st.dialog("Quer casar comigo?")
def pedido_namoro():
    if st.button("Sim", use_container_width= True):
        st.write('Te amo, amor')
# Using "with" notation
with st.sidebar:
    # Fotos de vocês dois aqui <3
    st.image("https://photos.fife.usercontent.google.com/pw/AP1GczM-7y074s9jBxvsCBUuP0nxpfmyR-xqwZSsaEeV9Mf9rvX61VyRxlIMzA=w696-h928-s-no-gm?authuser=0",
             caption="O dia que nos conhecemos.")
    st.image("https://photos.fife.usercontent.google.com/pw/AP1GczMW27IdTUrLMvYpZr_68XiSO0ur__f1Og1fohyOX8NlRTaDq3gUBuObvw=w308-h232-no?authuser=0",
             caption="Nosso primeiro porre.")
    st.image("https://photos.fife.usercontent.google.com/pw/AP1GczNeTcDOdNPi_rxBcOX_gnUXbqv66olE8p6lHWvQUc3xCJFpZ1sNYyn7Hw=w696-h928-s-no-gm?authuser=0",
             caption="A gata.")
    st.image("https://photos.fife.usercontent.google.com/pw/AP1GczNDy_TooCb7qAb8VjCNdWqBJkvuJ8ibWgR31nEB4IHcbnhWMg-yLbYKvA=w696-h928-s-no-gm?authuser=0",
             caption="Levando meu mundo nas costas.")
    st.image("https://i.pinimg.com/736x/40/5e/ee/405eee6b20478b5cc7e4c1f6b747cb28.jpg")
with st.container(border=True):
    st.header("Para o(a) mais especial.", divider="red")
    st.subheader("Play na nossa musiquinha?")
    st.audio("meu amor.mp3.mpeg", format="audio/mpeg", loop=True)
    st.header("Encontre a surpresa:", divider="red")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        btn1 = st.button(
            "![Heart](https://cdn.pixabay.com/photo/2016/02/04/11/57/heart-1179054_1280.png)",
            use_container_width= True, key=1)
        if btn1:
            caixa_modal('Você é uma branch do github? Porque quero dar um merge com você.')
    with col2:
        btn2 = st.button(
                "![Heart](https://cdn.pixabay.com/photo/2016/02/04/11/57/heart-1179054_1280.png)",
                use_container_width=True, key=2)
        if btn2:
            caixa_modal('Você deve ser uma função, porque toda vez que eu te chamo, retorno para você.')
    with col3:
        btn3 = st.button("![Heart](https://cdn.pixabay.com/photo/2016/02/04/11/57/heart-1179054_1280.png)",
                use_container_width=True, key=3)
        if btn3:
            # Arrumar aqui
            caixa_modal('Voce pode ser meu compilador(a)? Porque eu não rodo sem você.')
    with col4:
        btn4 = st.button(
                "![Heart](https://cdn.pixabay.com/photo/2016/02/04/11/57/heart-1179054_1280.png)",
                use_container_width=True, key=4)
        if btn4:
            pedido_namoro()
    with col5:
        btn5 = st.button(
                "![Heart](https://cdn.pixabay.com/photo/2016/02/04/11/57/heart-1179054_1280.png)",
                use_container_width=True, key=5)
        if btn5:
            caixa_modal('Você é um debugger? Porque você pode me ajudar com meus erros.')

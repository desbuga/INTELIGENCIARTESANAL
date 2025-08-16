import streamlit as st
import os
import random

# --- Configuração geral ---
st.set_page_config(page_title="DesbugaXuxu Unificado", layout="centered")
st.sidebar.title("Navegação")

# Inicializa contadores
if "modo_counts" not in st.session_state:
    st.session_state["modo_counts"] = {}
if "audio_counts" not in st.session_state:
    st.session_state["audio_counts"] = {}

def update_counts(modo, audio=None):
    st.session_state["modo_counts"][modo] = st.session_state["modo_counts"].get(modo, 0) + 1
    if audio:
        st.session_state["audio_counts"][audio] = st.session_state["audio_counts"].get(audio, 0) + 1

# Função para buscar MP3 em todas as subpastas
def listar_audios(base_dir):
    arquivos_mp3 = []
    for raiz, dirs, arquivos in os.walk(base_dir):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".mp3"):
                caminho_relativo = os.path.relpath(os.path.join(raiz, arquivo), base_dir)
                arquivos_mp3.append(caminho_relativo)
    return sorted(arquivos_mp3)

# --- Modos ---
def modo_desbugaxuxu_revolts():
    st.title("🧠 DesbugaXuxu (Revolts)")
    st.markdown("### Aperte o play e desbugue sua mente em até 33 segundos")
    st.image("https://example.com/julia_copacabana.gif", caption="Júlia de Copacabana na área! 🌴")

    base_dir = os.path.join(os.path.dirname(__file__), "audios", "revolts")
    audios = listar_audios(base_dir)

    if not audios:
        st.warning("⚠️ Nenhum áudio encontrado na pasta revolts.")
        return

    escolhido = st.selectbox("Escolha um áudio", audios)
    audio_path = os.path.join(base_dir, escolhido)

    try:
        with open(audio_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
        update_counts("Revolts", escolhido)
        st.balloons()
    except Exception as e:
        st.error(f"Erro ao carregar {escolhido}: {str(e)}")

def modo_desbugar_debochado():
    st.title("🌀 Desbugar com Deboche")
    st.caption("Caos, calmaria e zoeira. Escolhe aí.")
    st.image("https://example.com/china_deboche.gif", caption="China trazendo o deboche! 😜")

    base_dir = os.path.join(os.path.dirname(__file__), "audios", "debochado")
    audios = listar_audios(base_dir)

    if not audios:
        st.warning("⚠️ Nenhum áudio encontrado na pasta debochado.")
        return

    frases_por_audio = {
        "china_zebra.mp3": "Tô nem aí pra quem pintou a zebra, quero um pouco da tinta!",
        "calmaria_ilha.mp3": "Calmaria, tamo na ilha da magia, desbuga com sossego!"
    }

    if st.button("🎲 Sortear Áudio"):
        escolhido = random.choice(audios)
        st.session_state["audio_debochado"] = escolhido
        if "caotico" in escolhido.lower():
            st.balloons()
        else:
            st.snow()
        update_counts("Deboche", escolhido)

    if "audio_debochado" in st.session_state:
        audio_path = os.path.join(base_dir, st.session_state["audio_debochado"])
        try:
            with open(audio_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
            frase = frases_por_audio.get(st.session_state["audio_debochado"], "Zoeira sem legenda!")
            st.markdown(f"💬 {frase}")
        except Exception as e:
            st.error(f"Erro ao carregar {st.session_state["audio_debochado"]}: {str(e)}")

def modo_ravena():
    st.title("🖤 Modo Ravena 🚂🔥")
    st.markdown("Bugada com propósito. Aqui é pressão e bug.")
    st.image("https://example.com/ravena_bugada.gif", caption="Ravena bugando tudo! 🔥")

    base_dir = os.path.join(os.path.dirname(__file__), "audios", "ravena")
    audios = listar_audios(base_dir)

    if not audios:
        st.warning("⚠️ Nenhum áudio encontrado na pasta ravena.")
        return

    escolhido = st.selectbox("Escolha um áudio", audios)
    audio_path = os.path.join(base_dir, escolhido)

    try:
        with open(audio_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")
        update_counts("Ravena", escolhido)
        st.balloons()
    except Exception as e:
        st.error(f"Erro ao carregar {escolhido}: {str(e)}")

# --- Menu lateral ---
page = st.sidebar.radio("Selecione o Modo", ["DesbugaXuxu (Revolts)", "Desbugar com Deboche", "Modo Ravena"])

if st.sidebar.button("🎲 Aleatorizar Tudo"):
    page = random.choice(["DesbugaXuxu (Revolts)", "Desbugar com Deboche", "Modo Ravena"])
    st.sidebar.success(f"Modo sorteado: {page}")

st.sidebar.markdown("### 📊 Estatísticas")
for modo, count in st.session_state["modo_counts"].items():
    st.sidebar.write(f"{modo}: {count} usos")
st.sidebar.markdown("Áudios mais tocados:")
for audio, count in sorted(st.session_state["audio_counts"].items(), key=lambda x: x[1], reverse=True):
    st.sidebar.write(f"{audio}: {count}x")

if page == "DesbugaXuxu (Revolts)":
    modo_desbugaxuxu_revolts()
elif page == "Desbugar com Deboche":
    modo_desbugar_debochado()
elif page == "Modo Ravena":
    modo_ravena()


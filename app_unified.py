import streamlit as st
import os
import random

# --- Configurações Gerais --- #
st.set_page_config(page_title="DesbugaXuxu Unificado", layout="centered")
st.sidebar.title("Navegação")

# Inicializa contadores no session_state
if "modo_counts" not in st.session_state:
    st.session_state["modo_counts"] = {"DesbugaXuxu": 0, "Desbugar com Deboche": 0, "Modo Ravena": 0}
if "audio_counts" not in st.session_state:
    st.session_state["audio_counts"] = {}

# Função pra atualizar contadores
def update_counts(modo, audio=None):
    st.session_state["modo_counts"][modo] += 1
    if audio:
        st.session_state["audio_counts"][audio] = st.session_state["audio_counts"].get(audio, 0) + 1

# --- Funções para cada modo --- #

def desbugaxuxu_mode():
    st.title("🧠 DesbugaXuxu")
    st.markdown("### Aperte o play e desbugue sua mente em até 33 segundos")
    st.image("https://example.com/julia_copacabana.gif", caption="Júlia de Copacabana na área! 🌴")  # Placeholder pra imagem/GIF da Júlia

    AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audios", "revolts")

    if not os.path.exists(AUDIO_DIR):
        st.error("❌ Pasta de áudios (revolts) não encontrada.")
        st.stop()

    audio_files = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".mp3")]
    audio_files.sort()

    if not audio_files:
        st.warning("⚠️ Nenhum áudio disponível na pasta revolts.")
    else:
        selected_audio = st.selectbox("Escolha um áudio", audio_files)
        audio_path = os.path.join(AUDIO_DIR, selected_audio)
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success(f"✅ Tocando agora: **{selected_audio}**")
                update_counts("DesbugaXuxu", selected_audio)
                st.balloons()  # Efeito visual ao tocar
        else:
            st.warning("Áudio local não encontrado. Tentando fallback remoto...")
            audio_url = f"https://your-host.com/audios/revolts/{selected_audio}"  # Substitua por URL real
            st.audio(audio_url, format="audio/mp3")

def desbugar_debochado_mode():
    st.title("🌀 Desbugar com Deboche")
    st.caption("Caos, calmaria e zoeira. Escolhe aí.")
    st.image("https://example.com/china_deboche.gif", caption="China trazendo o deboche! 😜")  # Placeholder pra imagem/GIF da China

    if "modo" not in st.session_state:
        st.session_state["modo"] = "calmo"
    if "audio_atual" not in st.session_state:
        st.session_state["audio_atual"] = None
    if "frase_atual" not in st.session_state:
        st.session_state["frase_atual"] = ""

    # Áudios reais (substitua com os teus)
    audios_calmos = ["vouchamaradaChina.mp3", "outro_calmo.mp3"]
    audios_caoticos = ["calculadorasempilha.mp3", "outro_caotico.mp3"]

    # Frases personalizadas por áudio
    frases_por_audio = {
        "vouchamaradaadaChina.mp3": "China tá de boa, mas não confia no processo!",
        "calculadorasempilha.mp3": "Empilhando bugs como calculadoras? Caótico total.",
        # Adicione mais conforme teus áudios
    }

    audio_sub_dir = os.path.join(os.path.dirname(__file__), "audios", "debochado")
    if not os.path.exists(audio_sub_dir):
        st.error("❌ Pasta de áudios (debochado) não encontrada.")
        st.stop()

    if st.button("🌀 Desbugar Agora"):
        novo_modo = random.choice(["calmo", "caotico"])
        st.session_state["modo"] = novo_modo

        if novo_modo == "calmo":
            selected_audio_file = random.choice(audios_calmos)
            st.snow()  # Efeito calmo
        else:
            selected_audio_file = random.choice(audios_caoticos)
            st.balloons()  # Efeito caótico

        st.session_state["frase_atual"] = frases_por_audio.get(selected_audio_file, random.choice(["Frase padrão calminha.", "Frase padrão caótica."]))
        audio_path = os.path.join(audio_sub_dir, selected_audio_file)
        if os.path.exists(audio_path):
            st.session_state["audio_atual"] = audio_path
        else:
            st.error(f"Áudio não encontrado: {selected_audio_file}")
            st.session_state["audio_atual"] = None

        st.success(f"🎲 Modo agora é **{novo_modo.upper()}**!")
        update_counts("Desbugar com Deboche", selected_audio_file)

    if st.session_state["audio_atual"]:
        with open(st.session_state["audio_atual"], "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_name = os.path.basename(st.session_state["audio_atual"])
            st.markdown(f"🔊 Áudio sorteado: `{audio_name}`")
            st.audio(audio_bytes, format="audio/mp3")

    if st.session_state["frase_atual"]:
        st.markdown(f"💬 **{st.session_state.frase_atual}**")

def modo_ravena_mode():
    st.title("🧠 DesbugaXuxu — Modo Ravena 🚂🔥")
    st.markdown("Parece fofo, mas é bugado com propósito. 🖤🚂")
    st.markdown("### 💥 Frase do dia: Calma é pra quem tem tempo. Aqui é pressão e bug.")
    st.image("https://example.com/ravena_bugada.gif", caption="Ravena bugando tudo! 🔥")  # Placeholder pra imagem/GIF da Ravena

    AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audios", "ravena")

    if not os.path.exists(AUDIO_DIR):
        st.error("Nenhum arquivo de áudio encontrado na pasta \'audios/ravena\'.")
        st.stop()

    audio_files = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".mp3")]

    if not audio_files:
        st.warning("Nenhum áudio disponível na pasta ravena.")
    else:
        selected_audio = st.selectbox("Escolha um áudio", audio_files)
        audio_path = os.path.join(AUDIO_DIR, selected_audio)

        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

        st.success(f"🎵 Tocando agora: {selected_audio}")
        update_counts("Modo Ravena", selected_audio)
        st.balloons()  # Efeito ao tocar

# --- Navegação na Sidebar --- #
page = st.sidebar.radio("Selecione o Modo", ["DesbugaXuxu", "Desbugar com Deboche", "Modo Ravena"])

# Botão Aleatorizar Tudo
if st.sidebar.button("🎲 Aleatorizar Tudo"):
    modos = ["DesbugaXuxu", "Desbugar com Deboche", "Modo Ravena"]
    page = random.choice(modos)
    st.sidebar.success(f"Modo sorteado: {page}")
    # Aqui tu pode expandir pra sortear áudio dentro do modo, mas por agora só muda o modo

# Exibe contadores na sidebar
st.sidebar.markdown("### 📊 Estatísticas de Uso")
for modo, count in st.session_state["modo_counts"].items():
    st.sidebar.write(f"{modo}: {count} usos")
st.sidebar.markdown("Áudios mais tocados:")
for audio, count in sorted(st.session_state["audio_counts"].items(), key=lambda x: x[1], reverse=True):
    st.sidebar.write(f"{audio}: {count} toques")

if page == "DesbugaXuxu":
    desbugaxuxu_mode()
elif page == "Desbugar com Deboche":
    desbugar_debochado_mode()
elif page == "Modo Ravena":
    modo_ravena_mode()



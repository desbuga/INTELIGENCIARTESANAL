import time
import pyttsx3
import datetime

def fala_e_grava(texto, nome_arquivo="audio_ravena"):
    engine = pyttsx3.init()
    engine.setProperty(\'rate\', 150)  # Velocidade da fala
    engine.setProperty(\'volume\', 1.0)  # Volume máximo

    # Cria nome único com data e hora
    timestamp = datetime.datetime.now().strftime(\"%Y%m%d_%H%M%S\")
    nome_final = f\"{nome_arquivo}_{timestamp}.wav\"

    # Salva e fala
    engine.save_to_file(texto, nome_final)
    engine.runAndWait()

    print(f\"[✔️] Áudio salvo como: {nome_final}\")
    print(f\"[🗣️] Ravena disse: {texto}\")

def main():
    print(\"🔊 Gravador Galinha de Óculos v1.0 iniciado...\")
    time.sleep(1)

    # Texto da Ravena
    texto = \"Ravena na área, Xuxu! Tô afiada, pronta pra gravar e botar fogo no parquinho!\"
    fala_e_grava(texto, \"fala_ravena\")

if __name__ == \"__main__\":
    main()


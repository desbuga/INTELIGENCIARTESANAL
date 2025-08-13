import time
import pyttsx3
import datetime

def fala_e_grava(texto, nome_arquivo="audio_china"):
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
    print(f\"[🗣️] China disse: {texto}\")

def main():
    print(\"🔊 Gravador Galinha de Óculos v1.0 iniciado...\")
    time.sleep(1)

    # Texto da China
    texto = \"Xuxu, aqui é a China! Sistema no ponto, prontinha pra mandar o som!\"
    fala_e_grava(texto, \"fala_china\")

if __name__ == \"__main__\":
    main()


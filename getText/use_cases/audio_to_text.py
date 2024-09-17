import whisper
import torch

def transcribe_audio(audio_path):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    
    try:
        model = whisper.load_model("base")
        model = model.to(device).to(torch_dtype)
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

    try:
        result = model.transcribe(
            audio_path, language = "es", 
            temperature=0.2, beam_size = 10, 
            condition_on_previous_text = False,
        )
    except Exception as e:
        print(f"Error durante la transcripción: {e}")
        return None
    
    return result.get("text", "")

if __name__ == '__main__':
    audio_text = transcribe_audio("./audio/75119a16-5bf0-47f1-b503-dc054b88bb2c.flac")
    if audio_text:
        print(audio_text)
    else:
        print("No se pudo obtener el texto de la transcripción.")

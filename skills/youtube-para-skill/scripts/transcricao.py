"""Baixa a transcrição de um vídeo do YouTube.

Uso:
    python transcricao.py <link-ou-id-do-video> [--sem-tempo]

Precisa da biblioteca:  pip install youtube-transcript-api
Tenta português primeiro, depois inglês, depois qualquer idioma disponível.
"""
import re
import sys


def extrair_id(texto: str) -> str:
    padroes = [r"(?:v=|/shorts/|youtu\.be/|/embed/|/live/)([A-Za-z0-9_-]{11})", r"^([A-Za-z0-9_-]{11})$"]
    for p in padroes:
        m = re.search(p, texto.strip())
        if m:
            return m.group(1)
    sys.exit("Não encontrei o ID do vídeo nesse link: " + texto)


def buscar(video_id: str):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        sys.exit("Instale antes:  pip install youtube-transcript-api")
    api = YouTubeTranscriptApi()
    try:
        lista = api.list(video_id)
    except Exception as e:  # vídeo privado, sem legenda, bloqueado etc.
        sys.exit(f"Não consegui acessar as legendas desse vídeo: {e}")
    for idiomas in (["pt", "pt-BR"], ["en"]):
        try:
            return lista.find_transcript(idiomas).fetch()
        except Exception:
            pass
    for t in lista:  # qualquer idioma (traduz pra português se der)
        try:
            return t.translate("pt").fetch() if t.is_translatable else t.fetch()
        except Exception:
            return t.fetch()
    sys.exit("Esse vídeo não tem legendas disponíveis.")


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sem_tempo = "--sem-tempo" in sys.argv
    trechos = buscar(extrair_id(sys.argv[1]))
    for t in trechos:
        texto = t.text.replace("\n", " ").strip()
        if not texto:
            continue
        if sem_tempo:
            print(texto)
        else:
            m, s = divmod(int(t.start), 60)
            print(f"[{m:02d}:{s:02d}] {texto}")


if __name__ == "__main__":
    main()

---
name: youtube-para-skill
description: Transforma um vídeo do YouTube numa skill reutilizável do Claude Code. Use quando o usuário colar um link do YouTube e pedir pra aprender com o vídeo, extrair o método, os passos ou as técnicas, ou criar uma skill a partir dele.
---

# YouTube → Skill

Você vai assistir (ler a transcrição de) um vídeo do YouTube, extrair o conhecimento prático dele e salvar isso como uma **skill nova** que o Claude Code pode usar em qualquer projeto.

## 1. Pegar a transcrição
Rode o script que vem junto com esta skill (a pasta `scripts/` fica ao lado deste arquivo):

```bash
python "<pasta desta skill>/scripts/transcricao.py" "<link do vídeo>"
```

- Se aparecer "Instale antes", rode `pip install youtube-transcript-api` e tente de novo.
- Se o vídeo não tiver legenda, avise o usuário e peça outro vídeo (ou que ele cole a transcrição).
- Vídeos longos: leia a transcrição inteira antes de começar a resumir.

## 2. Entender o vídeo
Antes de escrever, identifique:
- **O objetivo**: o que o vídeo ensina a fazer, em uma frase.
- **O método**: os passos na ordem em que o autor faz.
- **As regras e princípios**: o que sempre fazer e o que evitar.
- **Exemplos e modelos**: frases, roteiros, prompts, números e checklists que o autor mostra.
- **Erros comuns** que ele cita.

Ignore conversa de abertura, propaganda e pedidos de inscrição.

## 3. Escrever a skill nova
Pergunte o nome da skill ao usuário (ou sugira um curto, em minúsculas e com hífens, como `funil-de-vendas-whatsapp`). Crie o arquivo:

`~/.claude/skills/<nome-da-skill>/SKILL.md`

Use este modelo:

```markdown
---
name: <nome-da-skill>
description: <o que a skill faz + quando usar, com as palavras que o usuário diria>
---

# <Título>

## Quando usar
<situações em que essa skill ajuda>

## Passo a passo
1. ...
2. ...

## Regras
- Sempre ...
- Nunca ...

## Modelos e exemplos
<roteiros, prompts, frases e checklists tirados do vídeo>

## Erros comuns
- ...

## Fonte
<título e link do vídeo>
```

Escreva instruções **acionáveis** ("faça X", "verifique Y"), não um resumo do vídeo. A skill tem que funcionar sozinha, sem precisar assistir o vídeo de novo.

## 4. Confirmar
Mostre ao usuário o caminho do arquivo criado e um resumo de 3 linhas do que a skill nova sabe fazer. Diga que ela já pode ser usada em qualquer conversa do Claude Code a partir de agora.

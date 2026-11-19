# YouTube → Skill para o Claude Code

Cole o link de qualquer vídeo do YouTube e o Claude assiste (pela transcrição), extrai o método e salva tudo como uma **skill nova**, que você reutiliza em qualquer projeto.

Feito por [@eu.souwesley](https://www.instagram.com/eu.souwesley/).

## Instalação (no Claude Code)

```
/plugin marketplace add EYVOASSISTENTE/youtube-para-skill
/plugin install youtube-para-skill@eu-souwesley
```

Depois, uma vez só, no terminal:

```
pip install youtube-transcript-api
```

## Como usar

No Claude Code, escreva:

> Analise este vídeo, extraia os principais ensinamentos e transforme esse conhecimento em uma skill reutilizável: https://www.youtube.com/watch?v=...

O Claude baixa a transcrição, organiza o passo a passo, as regras e os exemplos, e cria a skill em `~/.claude/skills/`.

## Ideias de uso
- Aulas de vendas e negociação → uma skill de atendimento
- Vídeos de copywriting → uma skill de roteiros e legendas
- Tutoriais de tráfego pago → uma skill de checklist de campanha
- Palestras e podcasts → uma skill com os princípios do autor

## Limites
- Funciona com vídeos que têm legenda (a maioria tem legenda automática).
- O Claude Code precisa de uma assinatura do Claude.

Licença: MIT.

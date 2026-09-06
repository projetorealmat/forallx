# Política de releases

Este repositório segue o padrão de releases do REALMat para livros mantidos em repositórios independentes.

## Versionamento

As tags seguem `vMAJOR.MINOR.PATCH`:

- `v1.0.0`: primeira tradução aprovada;
- `v1.0.1`: correção técnica ou editorial pequena, sem mudança de edição;
- `v1.1.0`: adaptação, acréscimo ou alteração compatível com a mesma edição;
- `v2.0.0`: nova edição, com mudança estrutural ou editorial ampla.

Uma release é um retrato imutável do livro naquele ponto do histórico. Uma correção nunca deve sobrescrever uma release existente: deve receber uma nova tag.

## Conteúdo de cada release

O workflow publica automaticamente:

- `forallx.pdf`;
- o pacote-fonte correspondente à tag;
- `forallx-<versão>-metadata.txt`;
- `SHA256SUMS`;
- as notas da versão geradas pelo GitHub.

O PDF publicado em uma release é a referência estável para leitores, citações e bifurcações. O `main` continua sendo a linha de desenvolvimento.

## Publicar uma versão

Antes de criar a tag:

1. confirme que o conteúdo foi revisado e mesclado em `main`;
2. confirme que o workflow **Build and Validate PDF** passou;
3. confirme o número da versão conforme as regras acima;
4. crie a tag a partir de `main`:

~~~sh
git fetch origin main
git switch main
git pull --ff-only origin main
git tag --annotate v1.0.0 --message "forallx v1.0.0 — primeira tradução aprovada"
git push origin v1.0.0
~~~

Não crie antes um rascunho de Release pela interface do GitHub: a própria automação criará a Release depois de validar a compilação. Se uma Release com a tag já existir, o workflow recusará sobrescrever seus arquivos.

O workflow **Publicar release do livro** validará a tag, compilará o PDF e criará a release. Para uma nova correção, use a próxima versão; não reutilize `v1.0.0`.

## Relação com o portal REALMat

O portal deve apontar para uma versão específica, por exemplo:

~~~text
https://github.com/projetorealmat/forallx/releases/download/v1.0.0/forallx.pdf
~~~

O portal pode manter um arquivo de catálogo com a versão atualmente recomendada e links para as versões anteriores. Uma eventual release agregadora do REALMat será apenas um índice de versões dos livros, não substituirá as releases individuais.

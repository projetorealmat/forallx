# Política de releases

Este repositório segue o padrão de releases do REALMat para livros mantidos em repositórios independentes.

## Versionamento

As tags seguem `vMAJOR.MINOR.PATCH`:

- `v0.x.y`: tradução em revisão;
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

O PDF publicado em uma release é a referência estável para leitores, citações e bifurcações. O `main` continua sendo a linha de desenvolvimento. A release `v0.x.y` é uma referência pública em revisão; a primeira referência aprovada será `v1.0.0`.

## Publicar uma versão pela interface do GitHub

Antes de publicar:

1. confirme que o conteúdo foi revisado e está em `main`;
2. confirme que o workflow **Build and Validate PDF** passou;
3. escolha a próxima versão conforme as regras acima.

Na página do repositório:

1. abra **Releases** e clique em **Draft a new release**;
2. em **Choose a tag**, digite a versão, por exemplo `v0.1.0`;
3. selecione **Create new tag on publish** e mantenha `main` como destino;
4. use um título como `forallx v0.1.0 — versão intermediária`;
5. escreva as notas da versão;
6. não anexe o PDF manualmente: o workflow o compilará e anexará os arquivos;
7. clique em **Publish release**.

A publicação da tag acionará o workflow **Publicar release do livro**, que validará a tag, compilará o PDF, criará o pacote-fonte, calculará os checksums e completará a Release com os arquivos gerados. Se a Release já tiver sido criada pela interface, a automação preservará suas notas e enviará apenas os arquivos ausentes.

Para uma nova correção, use a próxima versão; não reutilize uma tag existente.

## Relação com o portal REALMat

O portal deve apontar para uma versão específica, por exemplo:

~~~text
https://github.com/projetorealmat/forallx/releases/download/v1.0.0/forallx.pdf
~~~

O portal pode manter um arquivo de catálogo com a versão atualmente recomendada e links para as versões anteriores. Uma eventual release agregadora do REALMat será apenas um índice de versões dos livros, não substituirá as releases individuais.

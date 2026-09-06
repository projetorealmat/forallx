# forallx — Introdução à lógica formal

Este repositório contém uma tradução e adaptação brasileira de *forall x: An Introduction to Formal Logic*, de P.D. Magnus, baseada na edição mantida pelo [Open Logic Project](https://github.com/OpenLogicProject/forallx).

**Tradutor e adaptador:** Carlos André Duarte Costa.

A tradução está em revisão editorial. Sugestões e correções são bem-vindas por meio das [issues](https://github.com/projetorealmat/forallx/issues) e dos *pull requests*.

## Arquivos principais

- [Fonte principal em LaTeX](forallx.tex)
- [Metadados da edição](forallx-metadata.tex)
- [PDF da última versão publicada](https://github.com/projetorealmat/forallx/releases/latest/download/forallx.pdf)
- [Releases e versões anteriores](https://github.com/projetorealmat/forallx/releases)
- [Política de releases](RELEASE.md)
- [Execuções dos workflows](https://github.com/projetorealmat/forallx/actions)

O PDF oficial é publicado automaticamente em uma Release quando uma tag no formato `vMAJOR.MINOR.PATCH` é criada. O arquivo `forallx.pdf` não é mantido como arquivo versionado na raiz do repositório.

## Versões publicadas e arquivos-fonte

A primeira tradução aprovada será publicada como `v1.0.0`. A partir dela, o versionamento seguirá estas regras:

- `v1.0.0`: primeira tradução aprovada;
- `v1.0.1`: correção técnica ou editorial pequena;
- `v1.1.0`: adaptação ou acréscimo compatível com a mesma edição;
- `v2.0.0`: nova edição, com mudança estrutural ou editorial ampla.

Cada Release preserva:

- o PDF correspondente à versão;
- os arquivos-fonte automáticos da tag;
- o pacote-fonte reproduzível;
- os metadados usados na compilação;
- o arquivo `SHA256SUMS`.

Para consultar uma versão anterior, abra [Releases](https://github.com/projetorealmat/forallx/releases), escolha a versão desejada e baixe o PDF ou os arquivos-fonte. Os commits e as tags preservam também estados intermediários do projeto.

## Compilação local

Com uma instalação do TeX Live que inclua XeLaTeX e **latexmk**, execute na raiz do repositório:

~~~sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error forallx.tex
~~~

O comando gera `forallx.pdf` e os arquivos auxiliares da compilação. Para limpar esses arquivos, use:

~~~sh
latexmk -C forallx.tex
~~~

Em uma compilação local, o PDF será identificado como uma versão de desenvolvimento e receberá a data da compilação. O workflow de Release substitui automaticamente esses dados pela tag, pela data de publicação e pelo status editorial da versão.

## Publicação de uma versão

Depois de revisar o conteúdo em `main`, abra **Releases** no GitHub e clique em **Draft a new release**. Digite a versão, por exemplo `v0.1.0`, selecione **Create new tag on publish**, mantenha `main` como destino, escreva as notas e publique a Release.

Não anexe o PDF manualmente. O workflow **Publicar release do livro** será acionado pela nova tag, compilará o livro, criará o pacote-fonte, calculará os checksums e anexará os arquivos gerados. Para uma nova correção, use a próxima versão; não reutilize uma tag existente.

## Créditos e licença

A obra original é de P.D. Magnus e foi disponibilizada sob a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Esta tradução e adaptação deve manter a atribuição ao autor original e ao tradutor.

A edição brasileira não é uma publicação oficial do Open Logic Project; ela é uma obra derivada distribuída sob os termos da licença aplicável.

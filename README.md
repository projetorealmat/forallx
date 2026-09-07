# forallx — Introdução à lógica formal

[![Build and Validate PDF](https://github.com/projetorealmat/forallx/actions/workflows/latex.yml/badge.svg)](https://github.com/projetorealmat/forallx/actions/workflows/latex.yml)
[![Verificar links externos](https://github.com/projetorealmat/forallx/actions/workflows/check-links.yml/badge.svg)](https://github.com/projetorealmat/forallx/actions/workflows/check-links.yml)

Este repositório contém uma tradução e adaptação brasileira de *forall x: An Introduction to Formal Logic*, de P.D. Magnus, baseada no repositório mantido pelo [Open Logic Project](https://github.com/OpenLogicProject/forallx). A revisão foi conferida contra o commit [`b9a8724`](https://github.com/OpenLogicProject/forallx/commit/b9a872431eb97287fa039103db92a4bf27768b4b).

**Tradutor e adaptador:** Carlos André Duarte Costa.

A tradução está em revisão editorial. Sugestões e correções são bem-vindas por meio das [issues](https://github.com/projetorealmat/forallx/issues) e dos *pull requests*.

## Arquivos principais

- [Fonte principal em LaTeX](forallx.tex)
- [Metadados da edição](forallx-metadata.tex)
- [Metadados de citação](CITATION.cff)
- [PDF da versão atualmente recomendada](https://github.com/projetorealmat/forallx/releases/download/v0.1.0/forallx.pdf) (v0.1.0, em revisão)
- [Releases e versões anteriores](https://github.com/projetorealmat/forallx/releases)
- [Política de releases](RELEASE.md)
- [Fluxo editorial do projeto](EDITORIAL_WORKFLOW.md)
- [Execuções dos workflows](https://github.com/projetorealmat/forallx/actions)

O PDF oficial é publicado automaticamente em uma Release quando uma tag no formato `vMAJOR.MINOR.PATCH` é criada. O arquivo `forallx.pdf` não é mantido como arquivo versionado na raiz do repositório.

## Versões publicadas e arquivos-fonte

A versão `v0.1.0` existente é uma tradução em revisão e foi preservada como registro histórico. Após esta revisão ser incorporada, a próxima correção deverá ser publicada como `v0.1.1`; a primeira tradução aprovada será publicada como `v1.0.0`. A partir dela, o versionamento seguirá estas regras:

- `v0.x.y`: tradução em revisão;
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

Em uma compilação local, o PDF será identificado como uma versão de desenvolvimento e receberá a data da compilação. O workflow de Release substitui automaticamente esses dados pela tag, pela data de publicação e pelo status editorial da versão. Releases `v0.x.y` são pré-releases em revisão e não são consideradas pela URL `releases/latest` do GitHub.

## Publicação de uma versão

Depois de revisar o conteúdo em `main`, atualize a versão e a data em `CITATION.cff` para a próxima tag (por exemplo, `0.1.1` e `v0.1.1`). Em seguida, abra **Releases** no GitHub e clique em **Draft a new release**. Digite `v0.1.1`, selecione **Create new tag on publish**, mantenha `main` como destino, escreva as notas e publique a Release. O workflow verifica que a versão do `CITATION.cff` coincide com a tag.

Não anexe o PDF manualmente. O workflow **Publicar release do livro** será acionado pela nova tag, compilará o livro, criará o pacote-fonte, calculará os checksums e anexará os arquivos gerados. Para uma nova correção, use a próxima versão; não reutilize uma tag existente.

## Créditos e licença

A obra original é de P.D. Magnus e foi disponibilizada sob a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Esta tradução e adaptação deve manter a atribuição ao autor original e ao tradutor, indicar que houve tradução/adaptação e preservar o link da licença.

A edição brasileira não é uma publicação oficial do Open Logic Project; ela é uma obra derivada distribuída sob os termos da licença aplicável.

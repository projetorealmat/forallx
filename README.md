# forallx — Introdução à lógica formal

Este repositório contém uma tradução e adaptação brasileira de *forall x: An Introduction to Formal Logic*, de P.D. Magnus, baseada na edição mantida pelo [Open Logic Project](https://github.com/OpenLogicProject/forallx).

**Tradutor e adaptador:** Carlos André Duarte Costa.

A tradução está em revisão editorial. Sugestões e correções são bem-vindas por meio das [issues](https://github.com/CarlosCostaMath/forallx/issues) e dos *pull requests*.

## Arquivos principais

- [Fonte principal em LaTeX](forallx.tex)
- [Metadados da edição](forallx-metadata.tex)
- [PDF da última versão publicada](https://github.com/CarlosCostaMath/forallx/releases/latest/download/forallx.pdf)
- [Releases e versões anteriores](https://github.com/CarlosCostaMath/forallx/releases)
- [Execuções dos workflows](https://github.com/CarlosCostaMath/forallx/actions)

O PDF oficial é publicado automaticamente em uma Release quando uma tag de versão, como **v0.1.1**, é criada. O link acima sempre aponta para a Release marcada pelo GitHub como mais recente. O arquivo **forallx.pdf** é produzido durante a compilação e não é mantido como arquivo versionado na raiz do repositório.

## Versões publicadas e arquivos-fonte

A página de [Releases](https://github.com/CarlosCostaMath/forallx/releases) é o catálogo das versões publicadas. Cada Release preserva:

- o PDF correspondente à versão;
- os arquivos-fonte da tag nos links automáticos **Source code (zip)** e **Source code (tar.gz)**;
- nas Releases produzidas pelo workflow atualizado, o pacote **forallx-vX.Y.Z-source.tar.gz**, que também contém os metadados usados na compilação do PDF.

A Release **v0.1.0** foi criada antes dessa melhoria e já preserva o PDF e os arquivos-fonte automáticos do GitHub. A partir da próxima Release, o pacote-fonte reproduzível também será anexado.

Para consultar uma versão anterior, abra [Releases](https://github.com/CarlosCostaMath/forallx/releases), escolha a versão desejada e baixe o PDF ou um dos arquivos-fonte. Os commits e as tags do repositório também preservam estados intermediários do projeto.

## Compilação local

Com uma instalação do TeX Live que inclua XeLaTeX e **latexmk**, execute na raiz do repositório:

~~~sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error forallx.tex
~~~

O comando gera **forallx.pdf** e os arquivos auxiliares da compilação. Para limpar esses arquivos, use:

~~~sh
latexmk -C forallx.tex
~~~

Em uma compilação local, o PDF será identificado como uma versão de desenvolvimento e receberá a data da compilação. O workflow de Release substitui automaticamente esses dados pela tag e pela data da publicação.

## Publicação de uma versão

Depois de revisar e mesclar as alterações na **master**, crie uma tag seguindo o formato **vMAJOR.MINOR.PATCH**. Para a próxima publicação depois de **v0.1.0**, use:

~~~sh
git tag v0.1.1
git push origin v0.1.1
~~~

O workflow **Publish PDF Release** será executado automaticamente. Se a compilação passar, o GitHub criará ou atualizará a Release, anexará o **forallx.pdf**, anexará o pacote-fonte reproduzível e gerará as notas da versão.

## Créditos e licença

A obra original é de P.D. Magnus e foi disponibilizada sob a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Esta tradução e adaptação deve manter a atribuição ao autor original e ao tradutor.

A edição brasileira não é uma publicação oficial do Open Logic Project; ela é uma obra derivada distribuída sob os termos da licença aplicável.

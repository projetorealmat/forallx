# forallx — Introdução à lógica formal

[![REALMat — verificar livro](https://github.com/projetorealmat/forallx/actions/workflows/book-ci.yml/badge.svg)](https://github.com/projetorealmat/forallx/actions/workflows/book-ci.yml)

Este repositório contém uma tradução e adaptação brasileira de *forall x: An Introduction to Formal Logic*, de P.D. Magnus, baseada no repositório mantido pelo [Open Logic Project](https://github.com/OpenLogicProject/forallx). A revisão foi conferida contra o commit [`b9a8724`](https://github.com/OpenLogicProject/forallx/commit/b9a872431eb97287fa039103db92a4bf27768b4b).

**Tradutor e adaptador:** Carlos André Duarte Costa.

A tradução está em revisão editorial. Sugestões e correções são bem-vindas por meio das [issues](https://github.com/projetorealmat/forallx/issues) e dos *pull requests*.

## Arquivos principais

- [Fonte principal em LaTeX](forallx.tex)
- [Metadados da edição](forallx-metadata.tex)
- [Metadados de citação](CITATION.cff)
- [Configuração de integração do REALMat](.realmat/book.json)
<!-- realmat-release:start -->
- [PDF da versão atualmente recomendada](https://github.com/projetorealmat/forallx/releases/download/v0.1.3/forallx.pdf) (v0.1.3)
<!-- realmat-release:end -->
- [Releases e versões anteriores](https://github.com/projetorealmat/forallx/releases)
- [Política de releases](RELEASE.md)
- [Fluxo editorial do projeto](EDITORIAL_WORKFLOW.md)
- [Execuções dos workflows](https://github.com/projetorealmat/forallx/actions)

O PDF oficial de cada versão é compilado e publicado automaticamente depois do merge da respectiva **Release PR**. O arquivo `forallx.pdf` não é mantido como arquivo versionado na raiz do repositório.

## Versões publicadas e arquivos-fonte

A versão atualmente recomendada é `v0.1.3`, ainda em revisão editorial. Versões anteriores permanecem preservadas como registro histórico. A primeira tradução aprovada será publicada como `v1.0.0`.

O versionamento segue estas regras:

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

A publicação usa o padrão **Release PR**.

1. Incorpore primeiro em `main`, por PRs normais, todas as alterações de conteúdo que devem fazer parte da versão.
2. Abra **Actions → Preparar Release PR → Run workflow**.
3. Informe a próxima versão, sem o prefixo `v`, e a data da publicação.
4. A automação cria a branch `release/vMAJOR.MINOR.PATCH`, atualiza `CITATION.cff`, atualiza neste README as referências à versão recomendada e abre a Release PR.
5. Revise os checks e o PDF candidato.
6. O **merge da Release PR** é a autorização explícita para publicar.
7. Depois do merge, o workflow compila o PDF final, cria a tag, monta a GitHub Release como draft, anexa os artefatos e publica a Release.
8. O portal REALMat recebe o evento da nova versão, abre a PR do catálogo e solicita auto-merge; a PR só entra em `main` depois dos checks obrigatórios do portal.

Não crie a tag, o GitHub Release nem anexe o PDF manualmente. Para uma nova correção, use uma nova versão; nunca reutilize uma tag existente.

Detalhes, validações e procedimento de recuperação em caso de falha estão em [RELEASE.md](RELEASE.md).

## Créditos e licença

A obra original é de P.D. Magnus e foi disponibilizada sob a [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Esta tradução e adaptação deve manter a atribuição ao autor original e ao tradutor, indicar que houve tradução/adaptação e preservar o link da licença.

A edição brasileira não é uma publicação oficial do Open Logic Project; ela é uma obra derivada distribuída sob os termos da licença aplicável.

## Integração com o REALMat

Este repositório integra o projeto [REALMat](https://projetorealmat.github.io/). O catálogo e as demais edições podem ser consultados no [portal REALMat](https://projetorealmat.github.io/).

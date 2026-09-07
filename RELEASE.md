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

O workflow aplica automaticamente o status da release: versões `v0.x.x` são publicadas como **pre-release**; `v1.0.0` e versões posteriores são releases estáveis, salvo regra editorial documentada em contrário.

## Conteúdo de cada release

O workflow publica automaticamente:

- `forallx.pdf`;
- o pacote-fonte correspondente à tag;
- `forallx-<versão>-metadata.txt`;
- `SHA256SUMS`;
- `forallx-build-environment.txt`, com o ambiente efetivo usado na compilação;
- as notas da versão geradas pelo GitHub.

O PDF publicado em uma release é a referência estável para leitores, citações e bifurcações. O `main` continua sendo a linha de desenvolvimento. A release `v0.x.y` é uma referência pública em revisão; a primeira referência aprovada será `v1.0.0`.

## Como publicar uma versão

A publicação é controlada pela alteração da versão no `CITATION.cff`. Você não precisa criar a tag nem o GitHub Release manualmente.

1. Crie uma branch a partir de `main`.
2. Faça as alterações do conteúdo que devem entrar na publicação.
3. Atualize no mesmo branch:
   - `version`, usando a próxima versão;
   - `date-released`, usando a data prevista da publicação.
4. Abra um pull request para `main` e aguarde a revisão.
5. Depois que o pull request for mesclado, o workflow:
   - valida a nova versão;
   - cria a tag correspondente;
   - cria ou completa o GitHub Release;
   - compila e anexa o PDF;
   - gera o pacote-fonte e os checksums;
   - propõe a atualização do catálogo do portal REALMat.

Não crie a tag pelo menu **Releases**, não anexe o PDF manualmente e não altere a versão diretamente na `main`.

O workflow compara a versão atual do `CITATION.cff` com a versão do commit anterior. Alterações em autores, ORCID, título ou outros metadados, sem mudança de `version`, não criam uma nova release.

Se a compilação falhar, corrija o problema no conteúdo e abra um novo PR. Se a execução falhar depois de criar a tag, ela pode ser reexecutada: a automação verifica se a tag já aponta para o mesmo commit e preserva os arquivos e as notas existentes.

## Relação com o portal REALMat

O portal aponta para versões específicas, por exemplo:

~~~text
https://github.com/projetorealmat/forallx/releases/download/v0.1.0/forallx.pdf
~~~

O catálogo mantém a versão atualmente recomendada e os links para versões anteriores. Uma eventual release agregadora do REALMat será apenas um índice de versões dos livros, não substituirá as releases individuais.

Depois de publicar a release, o workflow calcula o SHA-256 do PDF e envia um evento ao portal REALMat. O portal transforma esse evento em um pull request de atualização do catálogo; ele não publica diretamente na `main`.

Para ativar essa integração, o proprietário do repositório deve manter o secret de Actions `PORTAL_DISPATCH_TOKEN`, com permissão de conteúdo para o repositório `projetorealmat/projetorealmat.github.io`. Sem esse secret, a release continua funcionando normalmente e a atualização do catálogo pode ser feita manualmente por pull request.

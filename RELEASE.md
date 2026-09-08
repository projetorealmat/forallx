# Política de releases

Este repositório segue o padrão de releases do REALMat para livros mantidos em repositórios independentes.

## Princípio: Release PR

O desenvolvimento normal e a publicação de uma versão são operações diferentes.

- **PR normal:** altera o conteúdo, o LaTeX, a tradução ou a infraestrutura do livro.
- **Release PR:** representa a intenção explícita de publicar uma nova versão.

Alterar `CITATION.cff` em um PR normal não deve ser usado como mecanismo de publicação. A versão e a data da próxima publicação são preparadas por um workflow específico, que abre uma Release PR. **O merge da Release PR é a autorização humana para publicar.**

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

O PDF publicado em uma release é a referência estável para leitores, citações e bifurcações. O `main` continua sendo a linha de desenvolvimento.

## Como preparar e publicar uma versão

Antes de preparar uma release, todas as alterações de conteúdo que devem entrar nela devem estar em `main`, com os respectivos checks aprovados.

### 1. Preparar a Release PR

Na página **Actions** do repositório:

1. abra o workflow **Preparar Release PR**;
2. clique em **Run workflow**;
3. informe:
   - a próxima versão, sem o prefixo `v`, por exemplo `0.1.2`;
   - a data de publicação em `AAAA-MM-DD`;
4. execute o workflow.

A automação:

- valida que a versão segue `MAJOR.MINOR.PATCH` e é maior que a versão atual;
- valida a data;
- verifica que a tag e a branch de release ainda não existem;
- cria a branch `release/vMAJOR.MINOR.PATCH`;
- atualiza `version` e `date-released` em `CITATION.cff`;
- atualiza o bloco de PDF recomendado e a frase de versão deste README;
- cria um commit de preparação;
- abre a Release PR para `main`.

A Release PR deve ser usada apenas para preparar a publicação. Mudanças de tradução, conteúdo ou código devem entrar antes, por PRs normais.

### 2. Revisar a Release PR

A Release PR passa pelo workflow **Build and Validate PDF**, como qualquer PR.

Revise:

- versão;
- data;
- resultado dos checks;
- PDF candidato produzido pelo CI;
- se o estado atual de `main` é realmente o que deve ser publicado.

Se algo no conteúdo ainda precisar ser corrigido, faça a correção em um PR normal e só depois atualize/recrie a Release PR conforme necessário.

### 3. Fazer merge da Release PR

**O merge da Release PR é o ato explícito de autorizar a publicação.**

Somente PRs mescladas cuja branch segue `release/vMAJOR.MINOR.PATCH` podem disparar o workflow de publicação. O workflow ainda verifica que:

- a PR foi efetivamente mesclada;
- a branch pertence ao próprio repositório;
- a versão do `CITATION.cff` coincide com o nome da branch;
- a versão mudou em relação ao estado anterior de `main`;
- uma tag eventualmente já existente aponta para o mesmo commit autorizado pela Release PR.

Depois dessas validações, o workflow:

1. compila novamente o PDF final a partir do commit mesclado;
2. verifica os metadados incorporados ao PDF;
3. gera o pacote-fonte e os checksums;
4. cria ou valida a tag anotada correspondente ao commit da release;
5. cria o GitHub Release inicialmente como **draft**;
6. anexa todos os artefatos;
7. publica o Release;
8. envia ao portal um evento autenticado pela GitHub App organizacional `REALMat Automation`.

Não crie a tag, o GitHub Release nem anexe o PDF manualmente.

## Falhas, recuperação e imutabilidade

A tag só é criada depois que a compilação final e a geração dos artefatos foram concluídas com sucesso.

Uma versão publicada não deve ser reutilizada. Se uma release pública precisar de correção editorial ou técnica, prepare uma nova versão.

Se o workflow falhar **depois do merge da Release PR**, não altere `CITATION.cff`, não crie uma nova versão apenas para contornar a falha e não mova tags manualmente. Primeiro corrija a infraestrutura em um PR normal.

Depois da correção, a publicação pode ser recuperada explicitamente em **Actions → Publicar release do livro → Run workflow**, informando o número da Release PR originalmente mesclada. A recuperação:

- consulta novamente a PR original no GitHub;
- exige que ela esteja mesclada em `main` e tenha branch `release/vMAJOR.MINOR.PATCH`;
- usa exatamente o commit de merge e o commit-base daquela PR;
- revalida a alteração de versão no `CITATION.cff`;
- se a tag já existir, exige que ela aponte para o mesmo commit;
- pode completar uma Release ainda em draft;
- não substitui silenciosamente assets de uma Release já publicada.

Assim, repetir a execução é uma **recuperação idempotente da mesma decisão editorial**, e não uma nova publicação.

## Relação com o portal REALMat

O portal aponta para versões específicas. Como exemplo de uma release já publicada:

~~~text
https://github.com/projetorealmat/forallx/releases/download/v0.1.1/forallx.pdf
~~~

Depois de publicar a release, o workflow calcula o SHA-256 do PDF publicado e envia um evento ao portal REALMat.

O portal transforma esse evento em um **pull request de atualização do catálogo**; ele não publica diretamente na `main`. A PR é criada pela mesma identidade de automação, solicita auto-merge e só pode ser mesclada depois dos checks obrigatórios do portal.

O fluxo completo é:

~~~text
PRs normais → main
                 ↓
        Preparar Release PR
                 ↓
          Release PR
                 ↓
              merge
                 ↓
       tag + PDF + Release
                 ↓
        PR automático do portal
                 ↓
       checks + auto-merge
                 ↓
          GitHub Pages
~~~

Para ativar a integração, a organização deve instalar a GitHub App `REALMat Automation` nos repositórios do REALMat e configurar a variável `REALMAT_AUTOMATION_APP_ID` e o secret `REALMAT_AUTOMATION_PRIVATE_KEY` em nível organizacional. A chave privada não pertence a este repositório. O portal também deve permitir auto-merge e exigir seus checks de build e links na branch `main`.

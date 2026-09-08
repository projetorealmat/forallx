# Fluxo editorial do forallx

O repositório separa o trabalho editorial do ato de publicar uma versão. Cada alteração deve passar por uma issue ou por um pull request claramente descrito; a `main` representa o estado de desenvolvimento revisável, enquanto uma tag representa um retrato imutável do livro.

## Organização de tarefas

Quando o GitHub Project do REALMat estiver criado, cada issue ou pull request deve receber:

- **Livro:** `forallx`;
- **Tipo:** tradução, terminologia, revisão linguística, revisão matemática, revisão editorial, LaTeX, build ou release;
- **Etapa:** triagem, em tradução, revisão linguística, revisão matemática, revisão editorial, aprovado ou publicado;
- **Release-alvo:** por exemplo, `v0.2.0` ou `v1.0.0`;
- **Capítulo/seção** e responsável, quando aplicável.

Labels recomendadas: `tradução`, `terminologia`, `revisão-linguística`, `revisão-matemática`, `revisão-editorial`, `latex`, `build`, `release` e `bloqueado`.

Pull requests ainda incompletos devem permanecer como **draft**. Quando o texto estiver pronto para revisão, converta-o em **ready for review**, vincule a issue com `Fixes #n` ou `Relates to #n` e indique exatamente quais capítulos e critérios foram verificados.

## Relação entre revisão e releases

- `v0.x.y`: tradução ou edição em revisão;
- `v1.0.0`: primeira tradução aprovada;
- `v1.x.y`: correção ou revisão compatível com a edição aprovada;
- `v2.0.0` ou superior: nova edição ou adaptação estrutural.

Uma release nunca é sobrescrita. A publicação deve ocorrer somente depois de o conteúdo estar na `main`, o workflow de compilação estar verde e a revisão editorial correspondente estar registrada.

Os workflows comuns são mantidos em [`projetorealmat/.github`](https://github.com/projetorealmat/.github). Este repositório mantém apenas a configuração específica do livro em `.realmat/book.json` e a validação/compilação própria da obra. A autenticação entre repositórios usa a GitHub App organizacional `REALMat Automation`, nunca um PAT armazenado no livro.

## Revisões complementares

O GitHub Actions verifica a compilação, referências não resolvidas, espaços indevidos e marcadores provisórios como `TODO`, `FIXME` e `TBD`. Essas verificações não substituem a revisão matemática ou linguística humana.

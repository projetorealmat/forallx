# Notas sobre intervenções relevantes

Este documento registra apenas intervenções que afetam a precisão linguística, o conteúdo formal, a leitura técnica ou a relação com a obra-fonte. Ele **não é um inventário exaustivo das adaptações** naturais de uma tradução para o português brasileiro.

A edição permanece em estágio de tradução inicial não revisada. As decisões abaixo são provisórias e devem ser consideradas novamente na revisão humana. O documento serve para manter a rastreabilidade das intervenções relevantes; não é conteúdo destinado ao leitor do livro e não substitui notas de rodapé.

**Bases cotejadas nesta verificação:** tradução em `main` no commit `1da59af443d55c6d279b5462177d4d8f6f2863eb` e obra-fonte em `master` no commit `b9a872431eb97287fa039103db92a4bf27768b4b`.

## Correções aplicadas diretamente

### R-01 — Resíduo de idioma na indicação de objetivos de prova

- **Localização:** `forallx.sty`, macro `\want`.
- **Problema:** a macro produzia a palavra inglesa `want` nas anotações de objetivos das provas.
- **Intervenção:** a saída foi traduzida para `quer`, preservando o identificador técnico `\want`.
- **Decisão:** correção linguística voltada ao leitor; não requer nota de rodapé.
- **Status:** aplicada; pendente de validação humana.

### R-02 — Terminologia de teoria da prova

- **Localização:** `forallx-ch6-proofs.tex`, seção sobre a corretude do sistema de prova.
- **Problema:** `argumento provável` traduzia inadequadamente *provable argument* e podia ser entendido como “argumento provável” no sentido de probabilidade.
- **Intervenção:** substituição por `argumento demonstrável`.
- **Decisão:** correção terminológica direta; não requer nota de rodapé.
- **Status:** aplicada; pendente de validação humana.

### R-08 — Correções linguísticas locais confirmadas

Foram corrigidos os seguintes problemas claros:

- `é determinada` → `é determinado`, em `forallx-ch5-semantics.tex`;
- `Ele significa` → `Ela significa`, em `forallx-ch4-predicate.tex`;
- `seguinitos` → `seguintes`, em `forallx-ch6-proofs.tex`.

Essas correções são linguísticas e não necessitam de nota de rodapé. A ocorrência `contem` em `forallx-ch4-predicate.tex` foi mantida: nesse contexto, trata-se do subjuntivo do verbo `contar` (“contar como bem formadas”), e não do verbo `conter`.

## Intervenções relevantes herdadas da tradução

### R-03 — Correção de erro na fonte em eliminação da disjunção

Na segunda demonstração de eliminação da disjunção em `forallx-app-quickreference.tex`, a fonte usa `\oe{ab,nb}` embora a hipótese disponível seja `\enot A`, identificada por `na`. A tradução usa `\oe{ab,na}`, que é a justificação correta.

Trata-se de uma correção de erro da fonte, não de uma diferença de tradução. A correção foi mantida sem nota de rodapé porque o erro é evidente no contexto formal; fica registrada aqui para rastreabilidade.

### R-04 — Fórmulas genéricas para cardinalidade

Na fórmula genérica para “pelo menos `n`”, a fonte escreve apenas uma sequência abreviada de desigualdades entre variáveis consecutivas. Para `n` geral, isso não garante que todos os objetos escolhidos sejam distintos. A tradução usa a conjunção indexada

```text
bigwedge_{1 <= i < j <= n} x_i != x_j
```

e emprega a forma análoga com `bigvee` nas fórmulas de “no máximo `n`”. Essa é uma correção matemática relevante de um problema da fonte. A formulação corrigida permanece no texto; não foi acrescentada nota de rodapé.

### R-05 — Inconsistência no domínio de uma interpretação

A fonte descreve o domínio como “whole numbers less than 10”, mas logo depois fornece o conjunto `{1,2,3,4,5,6,7,8,9}`. A tradução adotou `números inteiros de 1 a 9`, seguindo o conjunto explicitamente apresentado e mantendo coerência com as extensões dos predicados.

Essa escolha corrige uma inconsistência matemática da fonte. Não foi acrescentada nota de rodapé, pois a própria descrição e o conjunto do domínio tornam a decisão verificável; a intervenção fica registrada neste documento.

### R-06 — Identificadores internos associados às siglas portuguesas

Os identificadores `SLconventions`, `pr.wiffSL` e `pr.justifySLproof` foram ajustados para `LSconventions`, `pr.wiffLS` e `pr.justifyLSproof`, acompanhando a adoção das siglas portuguesas `LS` e `LQ`. As referências internas foram atualizadas e permanecem consistentes.

Essa alteração não exige nota ao leitor. Em futuras revisões técnicas, deve-se considerar a possível existência de consumidores externos desses identificadores.

### R-07 — Adaptação conceitual localizada

A edição brasileira amplia brevemente a passagem sobre lógicas não bivalentes, incluindo a distinção entre lacunas de valor de verdade, lógicas paraconsistentes e dialeteísmo. Essa intervenção é uma adaptação conceitual, não um erro de tradução. Ela é registrada por alterar o conteúdo explicativo, embora este documento não pretenda listar todas as adaptações culturais ou estilísticas da obra.

A apresentação da obra já informa que se trata de uma tradução e adaptação. Por isso, não foi acrescentada nota de rodapé específica.

## Critério para notas ao leitor

Não foram inseridas notas de rodapé para as intervenções acima. A política adotada nesta etapa é reservar notas ao leitor para casos em que uma alteração substancial não possa ser compreendida pelo próprio texto ou em que seja necessário explicar uma decisão editorial controversa. Correções linguísticas, normalizações de estilo e correções evidentes de erros formais da fonte permanecem no texto e são registradas seletivamente aqui.

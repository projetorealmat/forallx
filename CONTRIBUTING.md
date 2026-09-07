# Como contribuir

Obrigado por contribuir com a edição brasileira de *forallx: Introdução à lógica formal*.

## Tipos de contribuição

Você pode contribuir com:

- revisão da tradução e da terminologia;
- revisão matemática, lógica e editorial;
- correções de digitação, referências e formatação;
- melhorias no código LaTeX, nos workflows e na documentação;
- sugestões para futuras adaptações.

Para uma correção específica, abra uma issue antes de alterar muitos arquivos. Para uma proposta pronta, envie um pull request descrevendo o problema e a solução.

## Fluxo recomendado

1. Abra uma issue ou escolha uma tarefa existente.
2. Crie uma branch a partir de `main`, com nome descritivo, como `fix/termo-secao-2` ou `review/capitulo-3`.
3. Faça alterações pequenas e relacionadas ao mesmo objetivo.
4. Execute localmente:

   ```sh
   latexmk -xelatex -interaction=nonstopmode -halt-on-error forallx.tex
   ```

5. Abra um pull request para `main` e preencha o checklist.
6. Aguarde a revisão apropriada: linguística/terminológica, matemática/editorial ou técnica.
7. Só crie uma tag de release depois que o conteúdo estiver em `main` e os workflows passarem.

## Critérios editoriais

Uma alteração de tradução deve indicar, quando possível, o trecho original, a proposta em português e a justificativa. Uma alteração matemática deve preservar o significado formal, a notação e a coerência com as definições, proposições e exemplos do livro.

Traduções e adaptações devem manter a atribuição à obra original e indicar as modificações realizadas, conforme a [licença CC BY 4.0](LICENSE.md).

## Releases

- `v0.x.y`: tradução ou edição ainda em revisão;
- `v1.0.0`: primeira tradução aprovada;
- `v1.x.y`: correções ou alterações compatíveis com a edição aprovada;
- `v2.0.0` ou superior: nova edição ou alteração estrutural ampla.

Cada release é imutável. Não reutilize tags nem substitua os arquivos de uma release existente.

## Conduta

A revisão deve se concentrar no texto, na matemática e no funcionamento do projeto. Comentários devem ser claros, verificáveis e respeitosos.

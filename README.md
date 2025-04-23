# Projeto-Mercado-Inteligente

```
 O_
    \__________________________
      \   CP 2 - Supermercado  |
        \      Inteligente     |
          \___________________|
          /                 \
        ()                    ()
```

Programa de Otimização de Mercados

- Ideia: Um detector será inserido na entrada e na saída do super mercado, numerando o número de clientes que entraram e saíram. E de acordo com o número de clientes, um número x de caixas será solicitado. 
      Ex: Número de clientes >= 30, portanto, 5 caixas seram solicitados. Número de clientes é <= 10, 2 dos 5 caixas seram fechados, para que os funcionários possam executar outras funções.

  Além disso, integrar a numeração de itens dentro dos carrinhos, poderia trazer uma otimização ainda maior. Haveria um número x de itens que quando alcançados faria com que o programa solicitasse mais um caixa. 
   Ex: Se o número de itens total nos carrinhos do mercado for >= 500, 6 caixas são solicitados. Suponhamos que há 440 itens no total nos carrinhos em circulação, e um cliente novo chega e coloca 60 itens em seu carrinho atingindo 500, o programa automaticamente solicitaria a abertura de mais um caixa, visando a otimização de circulação de clientes no mercado. 

OBS: Com isso, haveria a possibilidade de estimar estatisticamente, qual é o número máximo de clientes e produtos no carrinhos que possibilita uma circulação otimizada no mercado. 

# Implementação Curva Cúbica de Bezier
Trabalho Prático com o objetivo da implementação de uma curva paramétrica.

## Requisitos
Para conseguir rodar o algoritmo é necessário possuir o Python instalado  juntamente com as bibliotecas Tkinter 

`pip install Tkinter `

Para rodar o algoritmo bastar executar na linha de comando

`python curva_bezier.py`

## Estrutura do código

O código é estruturado com os containers que equivalem as janelas de layout da interface. Os cálculos para a curva Bezier foram baseados e adaptados a partir do código implementado em https://github.com/NikolaiT/CunningCaptcha/blob/master/python_tests/bezier.py. Os métodos são:

* **initialize_points()**: chama o método *getPoints()* que guarda a posição do local em que o usuário clica na tela, nas variavéis *x* e *y* 
* **calculate_bezier()**: verifica se o usuário escolheu os 4 pontos na tela e chama o método *draw_cubic_bez*, caso contrário o programa exibe um pop-up informando quantos pontos o usuário ainda precisa selecionar na tela
* **draw_cubic_bez()**: a variável *t* é um valor de parametrização para percorrer a curva e calcular os novos valores dos pontos da reta *Bezier* através de uma estrutura de repetição que varia o valor de *t* = 0 até *t* = 1, sempre acrescentando +0.001 ao valor de *t*. Esse método chama o *cubic_bezier_sum* enviando como parâmetro os pontos de controle, para calcular o somatório de *Bezier*. A variação do parâmetro *t* pode ser observada na figura abaixo:

![alt text](https://upload.wikimedia.org/wikipedia/commons/d/db/B%C3%A9zier_3_big.gif)

* **cubic_bezier_sum()**: cálcula os novos pontos da curva de *Bezier* através do somatório da curva cúbica de Bezier, como demonstrado na fórmula abaixo. Foi utilizado o binômio ![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/88f3522b9f6208078c7fed701ecfcc0e5bf63de1) através de 4 pontos de controle para obter-se as curvas cúbicas

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/0596e1dae2ec55d157c28785267b434742f53ee3)

* **plot_pixel()**: plota os pixels na posição informada
* **reset_points()**: limpa os pontos da tela


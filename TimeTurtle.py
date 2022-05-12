import turtle
from svg_turtle import SvgTurtle

# Criando a tartaruga e definindo atributos
lapis = SvgTurtle(500, 500)
# lapis = turtle.Turtle()  # Para testar deixar essa linha on e comentar a de cima
lapis.shape('turtle')
lapis.color('black')
lapis.speed(10)

# Configurando tela
tela = turtle.Screen()

# Desenhando triangulo de fundo
lapis.penup()
lapis.right(90)
lapis.forward(180)
lapis.pendown()
lapis.right(180)
lapis.setpos(-200, 100)
lapis.forward(90)
lapis.right(90)
lapis.forward(400)
lapis.right(90)
lapis.forward(90)
lapis.setpos(0, -180)
lapis.right(180)
lapis.penup()

# Desenhando triangulo vermelho - lado esquerdo
lapis.forward(70)
lapis.left(90)
lapis.fd(20)
lapis.pendown()
lapis.color('red')
lapis.begin_fill()
lapis.setpos(-170, 100)
lapis.right(180)
lapis.fd(149)
lapis.right(90)
lapis.forward(70)
lapis.end_fill()
lapis.penup()

# Desenhando triangulo preto - lado direito
lapis.setpos(20, -110)
lapis.color('black')
lapis.right(180)
lapis.pendown()
lapis.begin_fill()
lapis.forward(210)
lapis.right(90)
lapis.forward(150)
lapis.setpos(20, -110)
lapis.end_fill()
lapis.penup()

# Desenhando retangulo preto para letreiro
lapis.setpos(-170, 115)
lapis.begin_fill()
lapis.pendown()
lapis.forward(340)
lapis.left(90)
lapis.forward(60)
lapis.left(90)
lapis.forward(340)
lapis.left(90)
lapis.forward(60)
lapis.end_fill()
lapis.penup()

# Fazendo letras do time (SPFC)
fonte1 = ('Times New Roman', 42, 'bold')
lapis.color('white')
lapis.left(90)
lapis.fd(180)
lapis.write('SPFC', False, 'center', fonte1)
lapis.penup()
lapis.shape('blank')

# tela.exitonclick()  # Para testar deixar essa linha on
lapis.save_as('TimeTurtle.svg')  # Para salvar Svg deixar essa linha on

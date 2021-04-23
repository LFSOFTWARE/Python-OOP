"""
Exercicios orientação a objetos

    Ex 1


class Pessoa:
    def __init__(self, nome, altura, idade):
        self.__nome = nome
        self.__altura = altura
        self.__idade = idade

    def dados_pessoa(self):
        print(f'Nome:{self.__nome}')
        print(f'Idade:{self.__idade}')
        print(f'Altura:{self.__altura}')


pes1 = Pessoa('luiz', 1.80, 18)

pes1.dados_pessoa()


    Ex2


class Agenda:
    fila = []

    @staticmethod
    def armazena_pessoa(nome, alura, idade):

        pessoa = [nome, alura, idade]
        Agenda.fila.append(pessoa)

    @staticmethod
    def remove_pessoa(nome):
        j = 0
        for x in Agenda.fila:
            if nome in x:
                indice = x.index(nome)
                Agenda.fila.pop(j)
            else:
                j += 1

    @staticmethod
    def busa_pessoa(nome):
        j = 0
        for x in Agenda.fila:
            if nome in x:
                indice = x.index(nome)
                return j+1
            else:
                j += 1

    @staticmethod
    def imprime_dados():
        for posicao,pessoa in enumerate(Agenda.fila):
            print(f'{posicao+1} Nome:{pessoa[0].title()} Idade: {pessoa[2]} Altura: {pessoa[1]}')

    @staticmethod
    def dados_pessoal(indice):
        indice -=1
        print(f'{indice+1} Nome:{Agenda.fila[indice][0].title()} Idade: {Agenda.fila[indice][2]} Altura: {Agenda.fila[indice][1]}')






    Ex3




class Elevador:
    pessoas_dentro = 0

    def __init__(self, capacidade, total_andares,andar=0):
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.andar = andar

    @staticmethod
    def inicia(capacidade, total_andares):
        Elevador.andar = 0
        Elevador.pessoas_dentro = 0

    def entra(self,qqd_pessoa):
        if self.pessoas_dentro + qqd_pessoa > self.capacidade:
            return 'lotado'
        else:
            self.pessoas_dentro += qqd_pessoa

    def sair(self, qqd_sair):
        if self.pessoas_dentro > 0:
            if 0 < qqd_sair < self.capacidade:
                self.pessoas_dentro -= qqd_sair

    def sobe(self):
        if self.andar is not self.total_andares:
            if self.andar + 1 <= self.total_andares:
                self.andar += 1
        else:
            print('voce ja esta no ultimo andar')

    def desce(self):
        if self.andar != 0:
            if self.andar - 1 >=0:
                self.andar -= 1
        else:
            print('voce ja esta no terrio')


#testando instancia


elevador1 = Elevador(5, 5)
print(elevador1.__dict__)
elevador1.entra(4)
print(elevador1.__dict__)

elevador1.sair(4)


elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
elevador1.desce()
print(elevador1.__dict__)
elevador1.sobe()


elevador1.desce()
elevador1.desce()
elevador1.desce()



print(elevador1.__dict__)


Ex 4


class Televisao:
    canal = 1
    volume = 0


class Controle:
    @staticmethod
    def aumentar_volume():
        if Televisao.volume < 10:
            Televisao.volume += 1
        else:
            print('volume maximo')

    @staticmethod
    def diminuir_volme():
        if Televisao.volume > 0:
            Televisao.volume -= 1

    @staticmethod
    def subir_canal():
        if Televisao.canal == 20:
            Televisao.canal = 1
        else:
            Televisao.canal += 1

    @staticmethod
    def descer_canal():
        if Televisao.canal == 1:
            Televisao.canal = 20
        else:
            Televisao.canal -= 1

    @staticmethod
    def chanel_specific(canal):
        if canal >= 1:
            if canal <= 20:
                Televisao.canal = canal

    @staticmethod
    def volume_atual():
        return Televisao.canal

    @staticmethod
    def canal_atual():
        return Televisao.volume

    Ex5


class Bola:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material

    def show_color(self):
        return self.cor

    def change_color(self, cor):
        self.cor = cor


bool = Bola('azul' , 9.8 , 'madeira')


print(bool.show_color())
print(bool.show_color())

Ex6



class Quadrado:
    def __init__(self, width_side):
        self.width_side = width_side

    def change_width_side(self, value):
        if value > 0:
            self.width_side = value

    def return_side(self):
        return self.width_side

    def cal_area(self):
        return self.width_side * self.width_side



mona = Quadrado(10)
mona.change_width_side(15)
print(mona.return_side())
print(mona.cal_area())
print(mona.__dict__)


EX7


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def change_sides(self, comp, larg):
        self.comprimento = comp
        self.largura = larg

    def retunr_sides(self):
        return f'comprimento: {self.comprimento} largura: {self.largura}'

    def cal_area(self):
        return self.comprimento * self.largura

    def cal_perimetro(self):
        return (self.comprimento *2)+(self.largura*2)

r = Retangulo(10,5)


print(r.cal_perimetro())


print(r.__dict__)

EX 8


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def comer(self):
        self.__engordar()

    def correr(self):
        self.emagrecer()

    def __engordar(self):
        self.peso += 10

    def emagrecer(self):
        self.peso -= 0.5

    def __crescer(self):
        self.altura += 0.5

    def envelhecer(self):
        if self.idade <= 21:
            self.__crescer()




fernando = Pessoa('luiz',18,65,1.75)

fernando.comer()
fernando.comer()
fernando.correr()
fernando.correr()
fernando.correr()
fernando.correr()

fernando.envelhecer()
print(fernando.__dict__)


Ex 9




class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome_correntista = nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor




conta1 = ContaCorrente(4521,'luiz',6000)

print(conta1.saldo)
conta1.alterar_nome('luiz fernando')

conta1.deposito(6000)
conta1.saque(5000)
print(conta1.__dict__)


Ex 10




class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def return_name(self):
        return self.nome

    def return_saude(self):
        return self.saude

    def return_fome(self):
        return self.fome

    def retur_idade(self):
        return self.idade

    def change_nome(self, nome):
        self.nome = nome

    def change_idade(self, idade):
        self.idade = idade

    def change_fome(self, fome):
        self.fome = fome

    def change_saude(self, saude):
        self.saude = saude

    def humor(self):
        if self.fome == 'cheio' and self.saude == 'saudavel':
            return "Estou feliz !!"

        elif self.fome == 'cheio':
            return "estou quase feliz... mais estou com a saude fraca "

        elif self.saude == 'saudavel':
            return "estou quase feliz...preciso de mais comida. EBA !!"


bicho = Tamagushi('xaimicu', 'cheio', 'saudavel', 10)
bicho.change_saude('fraco')
print(bicho.humor())
print(bicho.__dict__)

EX11



class Macaco:
    fila = 0
    estomago = {}

    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, comida):
        self.estomago.append(comida)

    def verbucho(self):
        return self.estomago

    def digerir(self):
        self.estomago.pop(self.fila)

    def __str__(self):
        return self.nome


# criando dois macacos

m = Macaco('luiz')
m2 = Macaco("pedro")



# comendo

m.comer('manga')
m.comer('pao')


m2.comer('macarrao')
m2.comer(m.nome)



print(m.verbucho())
print(m2.verbucho())
EX 12


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def return_y(self):
        return self.y

    def return_x(self):
        return self.x

    def info(self):

        print(f"X:{self.x} Y:{self.y}")

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def return_altura(self):
        return self.altura

    def return_largura(self):
        return self.largura

    def meio(self):
        y = self.altura / 2
        x = self.largura / 2

        return Ponto(x, y).info()



rat = Retangulo(10,5)


print(rat.meio())

EX13



class Bomba_combustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerporValor(self, valor):
        litros = valor / self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return f"{litros} L"
        else:
            return False

    def abastecerporLitro(self, litros):
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return f"R$ {self.valorLitro * litros}"
        else:
            return False

    def alterarvalor(self, valor_comb):
        self.valorLitro = valor_comb

    def alterarcombustivel(self, tipo_comb):
        self.tipoCombustivel = tipo_comb

    def alterarquantidadecombustivel(self, qqd_comb):
        self.quantidadeCombustivel = qqd_comb


b1 = Bomba_combustivel('gasolina', 1.5, 100)

print(b1.abastecerporValor(150))

b1.alterarcombustivel("diesel")


print(b1.__dict__)
EX 14



class Carro:
    tanque = 0

    def __init__(self, consumo, tanque=0):
        self.consumo = consumo
        self.tanque = tanque

    def andar(self,km):
        autonomia = self.tanque * self.consumo
        falta = 0
        resto =0
        if autonomia <= km:
            falta = km-autonomia
            self.tanque = 0
            print(f"Autonomia: {autonomia}")
            print(f"Andei: {km}")
            print(f"Falta:{falta}")
        else:
            resto = autonomia - km

            self.tanque -= km / self.consumo
            print(f"Autonomia: {autonomia}")
            print(f"Andei: {km}")
            print(f"tanque:{self.tanque}")

    def abastecer(self,qq_gasolina):
        self.tanque += qq_gasolina


    def ponteiro(self):
        return self.tanque


c = Carro(10)
c.abastecer(10)
print(c.andar(99))

print(c.__dict__)

class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def return_nome(self):
        return self.nome

    def return_salario(self):
        return self.salario


    def aumentar_salary(self,valor):
        self.salario = ((valor/100)*self.salario)+self.salario

"""






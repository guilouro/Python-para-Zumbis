#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
"""
user = input("Nome de usuario: ")
senha = input("Senha: ")

while senha == user:
	senha = input("Digite uma senha diferente do nome de usuário: ")

print ("Usuário: %s | Senha: %s" %(user, senha))
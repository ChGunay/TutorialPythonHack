# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:54:21 2020

@author: chgun
"""
def func1 ():
        
        print("Example Functuion 1")
        print("Örnek fonksiyon 1")

func1()

if __name__ == '__main__':#The if condition that tests how the function is executed.--İşlevin nasıl yürütüldüğünü test eden if koşulu.
    
    def func1 ():
        print("Python file executed directly--Python dosyası doğrudan yürütüldü")
        print("Example Functuion 1")
        print("Örnek fonksiyon 1")
else:
    
    def func1 ():
        print("Python file (ex1) executed by importing--İçe aktarılarak yürütülen Python dosyası")    
        
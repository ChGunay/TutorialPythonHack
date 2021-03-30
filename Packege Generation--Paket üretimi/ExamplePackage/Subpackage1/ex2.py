# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:56:21 2020

@author: chgun
"""

def func2 ():
    print("Example Functuion 2")
    print("Örnek fonksiyon 2")
func2()

if __name__ == '__main__':#The if condition that tests how the function is executed.--İşlevin nasıl yürütüldüğünü test eden if koşulu.
    
    def func2 ():
        print("Python file executed directly--Python dosyası doğrudan yürütüldü")
        print("Example Functuion 1")
        print("Örnek fonksiyon 1")
else:
    
    def func2 ():
        print("Python file(ex2) executed by importing--İçe aktarılarak yürütülen Python dosyası")    
        
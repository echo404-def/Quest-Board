#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 23:01:03 2023

@author: echo
"""


import tkinter as tk

class Processer:
    def read_file(self):
        file = self.entry1.get()
        try:
            #with open(file,"r") as r:l = r.read()
            f = open(file,"r")
            l = f.read()
            f.close()
        except:
            self.label2["text"] = "エラー: ファイルの読込に失敗しました"
            return()
        l = l.split("\n\n")
        self.ls = list()
        for i in l:
            self.ls += i.split("\n",1)
        self.ls = [i for i in self.ls if i != ""]
        self.i = -2
        self.display_next()
    
    def display_next(self):
        if self.i < len(self.ls)-2:
            self.i += 2
        self.label2["text"] = self.ls[self.i]
        self.label3["text"] = self.ls[self.i+1]
            
    def display_back(self):
        if self.i > 0:
            self.i -= 2
        self.label2["text"] = self.ls[self.i]
        self.label3["text"] = self.ls[self.i+1]
        
    def clear_filename(self):
        self.entry1.delete(0,tk.END)

    def main(self):
        root = tk.Tk()
        root.title("-Quest Board-")
        root.geometry("500x400")
        
        frame1 = tk.Frame(root)
        frame1.pack()
        
        label1 = tk.Label(frame1,text = "File",fg="gray")
        label1.grid(column=0,row=0)
        
        self.entry1 = tk.Entry(frame1,width=20)
        self.entry1.grid(column=1,row=0)
        
        self.btn1 = tk.Button(frame1,text="Load",command=self.read_file)
        self.btn1.grid(column=2,row=0)
        
        self.btn4 = tk.Button(frame1,text="Clear",command=self.clear_filename)
        self.btn4.grid(column=3,row=0)
        
        space = tk.Label(root,text="\nTitle",font=("",10),fg="gray")
        space.pack()
        
        self.label2 = tk.Label(root,text="No Data",font=("",25))
        self.label2.pack()
        
        space2 = tk.Label(root,text="\nContents",font=("",10),fg="gray")
        space2.pack()
        
        self.label3 = tk.Label(root,text="No Data")
        self.label3.pack()
        
        frame2 = tk.Frame(root)
        frame2.pack()
        
        self.btn2 = tk.Button(frame2,text="Next",command=self.display_next)
        self.btn2.grid(column=1,row=0)
        
        self.btn3 = tk.Button(frame2,text="Back",command=self.display_back)
        self.btn3.grid(column=0,row=0)
        
        root.mainloop()
        
        
if __name__ == "__main__":
    Processer().main()
        

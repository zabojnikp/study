﻿#!/usr/bin/env python3
# Copyright (c) 2008-9 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import dbm
import os
import pickle
import shelve
import sys
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import webbrowser


class AddEditForm(tkinter.Toplevel):

    def __init__(self, parent, name=None, url=None):
        super().__init__(parent)
        self.parent = parent
        self.accepted = False
        self.transient(self.parent)
        self.title("Záložky - " + (
                   "Úprava" if name is not None else "Přidání"))

        self.nameVar = tkinter.StringVar()
        if name is not None:
            self.nameVar.set(name)
        self.urlVar = tkinter.StringVar()
        self.urlVar.set(url if url is not None else "http://")

        frame = tkinter.Frame(self)
        nameLabel = tkinter.Label(frame, text="Název:", underline=0)
        nameEntry = tkinter.Entry(frame, textvariable=self.nameVar)
        nameEntry.focus_set()
        urlLabel = tkinter.Label(frame, text="Adresa URL:", underline=0)
        urlEntry = tkinter.Entry(frame, textvariable=self.urlVar)
        okButton = tkinter.Button(frame, text="OK", command=self.ok)
        cancelButton = tkinter.Button(frame, text="Storno",
                                      command=self.close)

        nameLabel.grid(row=0, column=0, sticky=tkinter.W, pady=3,
                       padx=3)
        nameEntry.grid(row=0, column=1, columnspan=3,
                       sticky=tkinter.EW, pady=3, padx=3)
        urlLabel.grid(row=1, column=0, sticky=tkinter.W, pady=3,
                      padx=3)
        urlEntry.grid(row=1, column=1, columnspan=3,
                      sticky=tkinter.EW, pady=3, padx=3)
        okButton.grid(row=2, column=2, sticky=tkinter.EW,
                      pady=3, padx=3)
        cancelButton.grid(row=2, column=3, sticky=tkinter.EW,
                          pady=3, padx=3)

        frame.grid(row=0, column=0, sticky=tkinter.NSEW)
        frame.columnconfigure(1, weight=1)
        window = self.winfo_toplevel()
        window.columnconfigure(0, weight=1)

        self.bind("<Alt-n>", lambda *ignore: nameEntry.focus_set())
        self.bind("<Alt-a>", lambda *ignore: urlEntry.focus_set())
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.close)

        self.protocol("WM_DELETE_WINDOW", self.close)
        self.grab_set()
        self.wait_window(self)


    def ok(self, event=None):
        self.name = self.nameVar.get()
        self.url = self.urlVar.get()
        self.accepted = True
        self.close()


    def close(self, event=None):
        self.parent.focus_set()
        self.destroy()


class MainWindow:

    def __init__(self, parent):
        self.parent = parent

        self.filename = None
        self.dirty = False
        self.data = {}

        menubar = tkinter.Menu(self.parent)
        self.parent["menu"] = menubar

        fileMenu = tkinter.Menu(menubar)
        for label, command, shortcut_text, shortcut in (
                ("Nový...", self.fileNew, "Ctrl+N", "<Control-n>"),
                ("Otevřít...", self.fileOpen, "Ctrl+O", "<Control-o>"),
                ("Uložit", self.fileSave, "Ctrl+U", "<Control-u>"),                
                (None, None, None, None),
                ("Import", self.fileImport, "Ctrl+I", "<Control-i>"),
                ("Export", self.fileExport, "Ctrl+E", "<Control-x>"),
                (None, None, None, None),
                ("Konec", self.fileQuit, "Ctrl+K", "<Control-k>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                        command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        menubar.add_cascade(label="Soubor", menu=fileMenu, underline=0)

        editMenu = tkinter.Menu(menubar)
        for label, command, shortcut_text, shortcut in (
                ("Přidat...", self.editAdd, "Ctrl+P", "<Control-p>"),
                ("Upravit...", self.editEdit, "Ctrl+U", "<Control-u>"),
                ("Vymazat...", self.editDelete, "Del", "<Delete>"),
                (None, None, None, None),
                ("Zobrazit webovou stránku...", self.editShowWebPage, "Ctrl+W",
                 "<Control-w>")):
            if label is None:
                editMenu.add_separator()
            else:
                editMenu.add_command(label=label, underline=0,
                        command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        menubar.add_cascade(label="Úpravy", menu=editMenu, underline=0)

        frame = tkinter.Frame(self.parent)
        self.toolbar_images = []
        toolbar = tkinter.Frame(frame)
        for image, command in (
                ("images/filenew.gif", self.fileNew),
                ("images/fileopen.gif", self.fileOpen),
                ("images/filesave.gif", self.fileSave),
                ("images/fileimport.gif", self.fileImport),
                ("images/fileexport.gif", self.fileExport),
                ("images/editadd.gif", self.editAdd),
                ("images/editedit.gif", self.editEdit),
                ("images/editdelete.gif", self.editDelete),
                ("images/editshowwebpage.gif", self.editShowWebPage)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tkinter.Button(toolbar, image=image,
                                        command=command)
                button.grid(row=0, column=len(self.toolbar_images)-1)
            except tkinter.TclError as err:
                print(err)
        toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NW)

        scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
        self.listBox = tkinter.Listbox(frame,
                                       yscrollcommand=scrollbar.set)
        self.listBox.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.listBox.focus_set()
        scrollbar["command"] = self.listBox.yview
        scrollbar.grid(row=1, column=1, sticky=tkinter.NS)

        self.statusbar = tkinter.Label(frame, text="Připraven...",
                                       anchor=tkinter.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.grid(row=2, column=0, columnspan=2,
                            sticky=tkinter.EW)

        frame.grid(row=0, column=0, sticky=tkinter.NSEW)

        frame.columnconfigure(0, weight=999)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=999)
        frame.rowconfigure(2, weight=1)

        window = self.parent.winfo_toplevel()
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        self.parent.geometry("{0}x{1}+{2}+{3}".format(400, 500,
                                                      0, 50))
        self.parent.title("Záložky - Bez názvu")


    def setStatusBar(self, text, timeout=5000):
        self.statusbar["text"] = text
        if timeout:
            self.statusbar.after(timeout, self.clearStatusBar)


    def clearStatusBar(self):
        self.statusbar["text"] = ""


    def fileNew(self, *ignore):
        if not self.okayToContinue():
            return
        self.listBox.delete(0, tkinter.END)
        self.dirty = False
        self.filename = None
        self.data = {}
        self.parent.title("Záložky - Bez názvu")


    def fileOpen(self, *ignore):
        if not self.okayToContinue():
            return
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        filename = tkinter.filedialog.askopenfilename(
                        title="Záložky - Otevřít soubor",
                        initialdir=dir,
                        filetypes=[("Soubory se záložkami", "*.bmf")],
                        defaultextension=".bmf", parent=self.parent)
        if filename:
            self.loadFile(filename)


    def loadFile(self, filename):
        self.filename = filename
        self.listBox.delete(0, tkinter.END)
        self.dirty = False
        try:
            with open(self.filename, "rb") as fh:
                self.data = pickle.load(fh)
            for name in sorted(self.data, key=str.lower):
                self.listBox.insert(tkinter.END, name)
            self.setStatusBar("Načteno {0} záložek ze souboru {1}".format(
                              self.listBox.size(), self.filename))
            self.parent.title("Záložky - {0}".format(
                              os.path.basename(self.filename)))
        except (EnvironmentError, pickle.PickleError) as err:
            tkinter.messagebox.showwarning("Záložky - Chyba",
                    "Nemohu načíst soubor {0}:\n{1}".format(
                    self.filename, err), parent=self.parent)


    def fileSave(self, *ignore):
        if self.filename is None:
            filename = tkinter.filedialog.asksaveasfilename(
                            title="Záložky - Uložit soubor",
                            initialdir=".",
                            filetypes=[("Soubory se záložkami", "*.bmf")],
                            defaultextension=".bmf",
                            parent=self.parent)
            if not filename:
                return False
            self.filename = filename
            if not self.filename.endswith(".bmf"):
                self.filename += ".bmf"
        try:
            with open(self.filename, "wb") as fh:
                pickle.dump(self.data, fh, pickle.HIGHEST_PROTOCOL)
            self.dirty = False
            self.setStatusBar("Uloženo {0} prvků do souboru {1}".format(
                              len(self.data), self.filename))
            self.parent.title("Záložky - {0}".format(
                              os.path.basename(self.filename)))
        except (EnvironmentError, pickle.PickleError) as err:
            tkinter.messagebox.showwarning("Záložky - Chyba",
                    "Nemohu uložit soubor {0}:\n{1}".format(
                    self.filename, err), parent=self.parent)
        return True


    def fileImport(self, *ignore):
        if not self.okayToContinue():
            return
        dir = (os.path.dirname(self.filename)
                if self.filename is not None else ".")
        suffix = ".dbm.dat" if sys.platform.startswith("win") else ".dbm"
        filename = tkinter.filedialog.askopenfilename(
                        title="Záložky - Importovat soubor",
                        initialdir=dir,
                        filetypes=[("Konzolové soubory záložek",
                                    "*" + suffix)],
                        defaultextension=suffix, parent=self.parent)
        if filename:
            if sys.platform.startswith("win"):
                filename = filename[:-4]
            db = None
            try:
                db = shelve.open(filename,
                                 protocol=pickle.HIGHEST_PROTOCOL)
                self.dirty = True
                for name, url in db.items():
                    self.data[name] = url
                self.listBox.delete(0, tkinter.END)
                for name in sorted(self.data, key=str.lower):
                    self.listBox.insert(tkinter.END, name)
                self.setStatusBar("Imported {0} bookmarks from {1}"
                            .format(self.listBox.size(), filename))
            except dbm.error as err:
                tkinter.messagebox.showwarning("Záložky - Chyba",
                        "Nemohu importovat soubor {0}:\n{1}".format(
                        filename, err), parent=self.parent)
            finally:
                if db is not None:
                    db.close()


    def fileExport(self, *ignore):
        suffix = ".dbm.dat" if sys.platform.startswith("win") else ".dbm"
        filename = tkinter.filedialog.asksaveasfilename(
                        title="Záložky - Exportovat soubor",
                        initialdir=".",
                        filetypes=[("Konzolové soubory záložek",
                                    "*" + suffix)],
                        defaultextension=suffix, parent=self.parent)
        if filename:
            if sys.platform.startswith("win"):
                filename = filename[:-4]
            db = None
            try:
                db = shelve.open(filename,
                                 protocol=pickle.HIGHEST_PROTOCOL)
                for name, url in self.data.items():
                    db[name] = url
                db.sync()
                self.setStatusBar("Exportováno {0} záložek do souboru {1}"
                        .format(self.listBox.size(), filename))
            except dbm.error as err:
                tkinter.messagebox.showwarning("Záložky - Chyba",
                        "Nemohu exportovat soubor {0}:\n{1}".format(
                        filename, err), parent=self.parent)
            finally:
                if db is not None:
                    db.close()


    def editAdd(self, *ignore):
        form = AddEditForm(self.parent)
        if form.accepted and form.name:
            self.data[form.name] = form.url
            self.listBox.delete(0, tkinter.END)
            for name in sorted(self.data, key=str.lower):
                self.listBox.insert(tkinter.END, name)
            self.dirty = True


    def editEdit(self, *ignore):
        indexes = self.listBox.curselection()
        if not indexes or len(indexes) > 1:
            return
        index = indexes[0]
        name = self.listBox.get(index)
        form = AddEditForm(self.parent, name, self.data[name])
        if form.accepted and form.name:
            self.data[form.name] = form.url
            if form.name != name:
                del self.data[name]
                self.listBox.delete(0, tkinter.END)
                for name in sorted(self.data, key=str.lower):
                    self.listBox.insert(tkinter.END, name)
            self.dirty = True


    def editDelete(self, *ignore):
        indexes = self.listBox.curselection()
        if not indexes or len(indexes) > 1:
            return
        index = indexes[0]
        name = self.listBox.get(index)
        if tkinter.messagebox.askyesno("Záložky - Vymazání",
                                 "Vymazat '{0}'?".format(name)):
            self.listBox.delete(index)
            self.listBox.focus_set()
            del self.data[name]
            self.dirty = True


    def editShowWebPage(self, *ignore):
        indexes = self.listBox.curselection()
        if not indexes or len(indexes) > 1:
            return
        index = indexes[0]
        url = self.data[self.listBox.get(index)]
        webbrowser.open_new_tab(url)


    def fileQuit(self, event=None):
        if self.okayToContinue():
            self.parent.destroy()


    def okayToContinue(self):
        if not self.dirty:
            return True
        reply = tkinter.messagebox.askyesnocancel(
                        "Záložky - Neuložené změny",
                        "Uložit změny?", parent=self.parent)
        if reply is None:
            return False
        if reply:
            return self.fileSave()
        return True


application = tkinter.Tk()
path = os.path.join(os.path.dirname(__file__), "images/")
if sys.platform.startswith("win"):
    icon = path + "bookmark.ico"
    application.iconbitmap(icon, default=icon)
else:
    application.iconbitmap("@" + path + "bookmark.xbm")
window = MainWindow(application)
application.protocol("WM_DELETE_WINDOW", window.fileQuit)
application.mainloop()


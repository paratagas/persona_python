# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 10:47:49 2014

@author: Eugene Sviridenko (Евгений Свириденко)
"""

# Для компиляции из QtDesigner в *.py открыть папку:
# ...\python-3.3.5.amd64\Lib\site-packages\PyQt4\uic
# скопировать туда файл формы *.ui
# и выполнить команду:
# pyuic.py Form.ui -o ui_MyForm.py
# Ui_MyForm


from PyQt4 import QtCore, QtGui
import sys, ui_MyForm
import sqlite3
import time
import hashlib
import datetime

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
ui = ui_MyForm.Ui_MyForm()
ui.setupUi(window)


# Запрет на оступ к остальным вкладкам до авторизации на входе

ui.tab_input.setEnabled(False)
ui.tab_output.setEnabled(False)
ui.tab_edit.setEnabled(False)
ui.tab_admin.setEnabled(False)

# Переопределение шрифтов
font = QtGui.QFont("Tahoma", 12)

ui.login_login_label.setFont(font)
ui.login_pass_label.setFont(font)
ui.login_login.setFont(font)
ui.login_pass.setFont(font)


ui.name_input_label.setFont(font)
ui.sur_input_label.setFont(font)
ui.name_lat_input_label.setFont(font)
ui.sur_lat_input_label.setFont(font)
ui.birth_input_label.setFont(font)
ui.civil_input_label.setFont(font)
ui.pass_input_label.setFont(font)
ui.number_input_label.setFont(font)
ui.auto_input_label.setFont(font)

ui.name_input.setFont(font)
ui.sur_input.setFont(font)
ui.name_lat_input.setFont(font)
ui.sur_lat_input.setFont(font)
ui.birth_input.setFont(font)
ui.civil_input.setFont(font)
ui.pass_input.setFont(font)
ui.number_input.setFont(font)
ui.number_auto_input.setFont(font)

ui.info_date_input_label.setFont(font)
ui.info_country_input_label.setFont(font)
ui.info_dir_input_label.setFont(font)
ui.info_ppr_input_label.setFont(font)
ui.info_who_input_label.setFont(font)

ui.info_date_input.setFont(font)
ui.info_country_input.setFont(font)
ui.info_dir_input_in.setFont(font)
ui.info_dir_input_out.setFont(font)
ui.info_ppr_input.setFont(font)
ui.info_who_input.setFont(font)

ui.sort_input_label.setFont(font)
ui.quant_input_label.setFont(font)
ui.price_input_label.setFont(font)
ui.quant_input_select.setFont(font)
ui.price_input_select.setFont(font)
ui.sort_input.setFont(font)
ui.quant_input.setFont(font)
ui.price_input.setFont(font)

ui.fab_input_text.setFont(font)

ui.sur_output_label.setFont(font)
ui.sur_lat_output_label.setFont(font)
ui.sur_output.setFont(font)
ui.sur_lat_output.setFont(font)

ui.pass_output_label.setFont(font)
ui.auto_output_label.setFont(font)
ui.pass_output.setFont(font)
ui.auto_output.setFont(font)

ui.info_date_output_label_from.setFont(font)
ui.info_date_output_label_to.setFont(font)
ui.info_ppr_output_label.setFont(font)
ui.info_dir_output_label.setFont(font)

ui.info_date_output_from.setFont(font)
ui.info_date_output_to.setFont(font)
ui.info_ppr_output.setFont(font)
ui.info_dir_output_in.setFont(font)
ui.info_dir_output_out.setFont(font)

ui.info_date_output_date_label_from.setFont(font)
ui.info_date_output_date_label_to.setFont(font)
ui.info_date_output_date_from.setFont(font)
ui.info_date_output_date_to.setFont(font)

ui.output_data_total_label.setFont(font)
ui.output_data_total.setFont(font)
ui.output_data_sur_label.setFont(font)
ui.output_data_sur.setFont(font)
ui.output_data_text.setFont(font)

# tab_edit
ui.name_edit_label.setFont(font)
ui.sur_edit_label.setFont(font)
ui.name_lat_edit_label.setFont(font)
ui.sur_lat_edit_label.setFont(font)
ui.birth_edit_label.setFont(font)
ui.civil_edit_label.setFont(font)
ui.pass_edit_label.setFont(font)
ui.number_edit_label.setFont(font)
ui.auto_edit_label.setFont(font)

ui.name_edit.setFont(font)
ui.sur_edit.setFont(font)
ui.name_lat_edit.setFont(font)
ui.sur_lat_edit.setFont(font)
ui.birth_edit.setFont(font)
ui.civil_edit.setFont(font)
ui.pass_edit.setFont(font)
ui.number_edit.setFont(font)
ui.number_auto_edit.setFont(font)

ui.info_date_edit_label.setFont(font)
ui.info_country_edit_label.setFont(font)
ui.info_dir_edit_label.setFont(font)
ui.info_ppr_edit_label.setFont(font)
ui.info_who_edit_label.setFont(font)

ui.info_date_edit.setFont(font)
ui.info_country_edit.setFont(font)
ui.info_dir_edit.setFont(font)
ui.info_ppr_edit.setFont(font)
ui.info_who_edit.setFont(font)

ui.sort_edit_label.setFont(font)
ui.quant_edit_label.setFont(font)
ui.price_edit_label.setFont(font)
ui.quant_edit_select.setFont(font)
ui.price_edit_select.setFont(font)
ui.sort_edit.setFont(font)
ui.quant_edit.setFont(font)
ui.price_edit.setFont(font)
ui.fab_edit_text.setFont(font)

ui.admin_new_name_label.setFont(font)
ui.admin_new_pass_label.setFont(font)
ui.admin_new_conf_pass_label.setFont(font)
ui.admin_new_name.setFont(font)
ui.admin_new_pass.setFont(font)
ui.admin_new_conf_pass.setFont(font)

ui.chahge_pass_sel_user_old_label.setFont(font)
ui.chahge_pass_sel_user_new_label.setFont(font)
ui.chahge_pass_sel_user_conf_label.setFont(font)
ui.chahge_pass_sel_user_old.setFont(font)
ui.chahge_pass_sel_user_new.setFont(font)
ui.chahge_pass_sel_user_conf.setFont(font)


# Фон для вкладок
ui.tab_login.setStyleSheet("background-image: url(images/met-patt-04.jpg)")
ui.login_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.login_label_persona.setStyleSheet("background-image: url(images/no_image.png)")
ui.login_label_persona.setPixmap(QtGui.QPixmap("images/logo.png"))

ui.tab_input.setStyleSheet("background-image: url(images/met-patt-04.jpg)")
ui.pers_input_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.info_input_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.tmc_input_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.fab_input_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.input_write.setStyleSheet("background-image: url(images/no_image.png)")
ui.input_reset.setStyleSheet("background-image: url(images/no_image.png)")
ui.intput_progressBar.setStyleSheet("background-image: url(images/no_image.png)")

ui.tab_output.setStyleSheet("background-image: url(images/met-patt-04.jpg)")
ui.pers_output_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_find_sur.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_reset_sur.setStyleSheet("background-image: url(images/no_image.png)")
ui.pers_output_group_2.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_find_num.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_reset_num.setStyleSheet("background-image: url(images/no_image.png)")
ui.info_output_group_2.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_find_ppr.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_reset_ppr.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_find_all.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_export.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_reset_output.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_export_pdf.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_progressBar.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_data_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.info_output_group_date.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_find_date.setStyleSheet("background-image: url(images/no_image.png)")
ui.output_reset_date.setStyleSheet("background-image: url(images/no_image.png)")

ui.tab_edit.setStyleSheet("background-image: url(images/met-patt-04.jpg)")
ui.pers_edit_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.info_edit_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.tmc_edit_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.fab_edit_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.edit_write.setStyleSheet("background-image: url(images/no_image.png)")
ui.edit_reset.setStyleSheet("background-image: url(images/no_image.png)")
ui.edit_delete.setStyleSheet("background-image: url(images/no_image.png)")
ui.edit_progressBar.setStyleSheet("background-image: url(images/no_image.png)")

ui.tab_admin.setStyleSheet("background-image: url(images/met-patt-04.jpg)")
ui.admin_new_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.admin_chahge_pass_group.setStyleSheet("background-image: url(images/no_image.png)")
ui.admin_del_user_group.setStyleSheet("background-image: url(images/no_image.png)")

ui.tab_about.setStyleSheet("background-image: url(images/met-patt-04.jpg)")


# Переопределение и добавление атрибутов класса

# Установка тул-типов

# Календарь
tool_date = "Для открытия календаря нажмите на стрелку справа\n\
            Для выбора месяца нажмите на название месяца\n\
            Для ввода года нажмите на название года"
ui.birth_input.setToolTip(tool_date)
ui.info_date_input.setToolTip(tool_date)
ui.info_date_output_from.setToolTip(tool_date)
ui.info_date_output_to.setToolTip(tool_date)
ui.info_date_output_date_from.setToolTip(tool_date)
ui.info_date_output_date_to.setToolTip(tool_date)

# Количество ТМЦ
tool_quant = "Введите целое число без пробелов"
ui.quant_input.setToolTip(tool_quant)
ui.price_input.setToolTip(tool_quant)
ui.quant_edit.setToolTip(tool_quant)
ui.price_edit.setToolTip(tool_quant)

# Вариантность ППр
tool_ppr_sel = "Уберите галочку, если нарушение произошло не в ППр"
ui.info_ppr_input_label.setToolTip(tool_ppr_sel)

# Груп-боксы поиска
tool_search_sur = "Введите фамилию на русском и (или) латиницей"
ui.pers_output_group.setToolTip(tool_search_sur)

tool_search_num = "Введите № паспорта и (или) автомобиля"
ui.pers_output_group_2.setToolTip(tool_search_num)

tool_search_info = "Заполните все поля блока"
ui.info_output_group_2.setToolTip(tool_search_info)

tool_search_date = "Введите промежуток времени, в который произошло задержание"
ui.info_output_group_date.setToolTip(tool_search_date)

# Кнопки
tool_output_all = "Нажмите для вывода всех записей в базе данных"
ui.output_find_all.setToolTip(tool_output_all)

tool_edit_new = "Нажмите, чтобы внести изменения в информацию о лице"
ui.edit_write.setToolTip(tool_edit_new)

tool_edit_clear = "Нажмите, чтобы очистить все поля формы"
ui.edit_reset.setToolTip(tool_edit_clear)

tool_delete = "Нажмите, чтобы полностью удалить запись о лице"
ui.edit_delete.setToolTip(tool_delete)

tool_delete_user = "Удалить пользователя может только администратор"
ui.admin_del_user_group.setToolTip(tool_delete_user)



# Эл. табло
ui.output_data_total.setSegmentStyle(QtGui.QLCDNumber.Flat)

# Установка иконок
style = window.style()

login_enter = QtGui.QIcon("icons/login_enter.png")
ui.login_enter.setIcon(login_enter)
ui.login_enter.setIconSize(QtCore.QSize(24, 24))

icon_input_write = style.standardIcon(QtGui.QStyle.SP_DialogOkButton)
ui.input_write.setIcon(icon_input_write)
ui.input_write.setIconSize(QtCore.QSize(24, 24))

icon_output_find = QtGui.QIcon("icons/icon_search.png")
ui.output_find_sur.setIcon(icon_output_find)
ui.output_find_num.setIcon(icon_output_find)
ui.output_find_ppr.setIcon(icon_output_find)
ui.output_find_date.setIcon(icon_output_find)

ui.output_find_sur.setIconSize(QtCore.QSize(24, 24))
ui.output_find_num.setIconSize(QtCore.QSize(24, 24))
ui.output_find_ppr.setIconSize(QtCore.QSize(24, 24))
ui.output_find_date.setIconSize(QtCore.QSize(24, 24))

icon_output_all = QtGui.QIcon("icons/icon_search_all.png")
ui.output_find_all.setIcon(icon_output_all)
ui.output_find_all.setIconSize(QtCore.QSize(24, 24))

icon_output_export = QtGui.QIcon("icons/icon_word.png")
ui.output_export.setIcon(icon_output_export)
ui.output_export.setIconSize(QtCore.QSize(24, 24))

icon_output_export_pdf = QtGui.QIcon("icons/icon_pdf.png")
ui.output_export_pdf.setIcon(icon_output_export_pdf)
ui.output_export_pdf.setIconSize(QtCore.QSize(24, 24))

icon_edit_write = style.standardIcon(QtGui.QStyle.SP_BrowserReload)
ui.edit_write.setIcon(icon_edit_write)
ui.edit_write.setIconSize(QtCore.QSize(24, 24))

icon_edit_delete = style.standardIcon(QtGui.QStyle.SP_DialogDiscardButton)
ui.edit_delete.setIcon(icon_edit_delete)
ui.edit_delete.setIconSize(QtCore.QSize(24, 24))

icon_admin_new_write = QtGui.QIcon("icons/icon_user.png")
ui.admin_new_write.setIcon(icon_admin_new_write)
ui.admin_new_write.setIconSize(QtCore.QSize(24, 24))

icon_chahge_pass_user = QtGui.QIcon("icons/icon_private.png")
ui.chahge_pass_user.setIcon(icon_chahge_pass_user)
ui.chahge_pass_user.setIconSize(QtCore.QSize(24, 24))

icon_admin_del_user = style.standardIcon(QtGui.QStyle.SP_DialogDiscardButton)
ui.admin_del_user.setIcon(icon_admin_del_user)
ui.admin_del_user.setIconSize(QtCore.QSize(24, 24))

icon_reset = style.standardIcon(QtGui.QStyle.SP_DialogResetButton)
ui.login_reset.setIcon(icon_reset)
ui.input_reset.setIcon(icon_reset)
ui.output_reset_sur.setIcon(icon_reset)
ui.output_reset_num.setIcon(icon_reset)
ui.output_reset_ppr.setIcon(icon_reset)
ui.output_reset_date.setIcon(icon_reset)
ui.output_reset_output.setIcon(icon_reset)
ui.edit_reset.setIcon(icon_reset)
ui.admin_new_reset.setIcon(icon_reset)
ui.login_reset.setIconSize(QtCore.QSize(24, 24))
ui.input_reset.setIconSize(QtCore.QSize(24, 24))
ui.output_reset_sur.setIconSize(QtCore.QSize(24, 24))
ui.output_reset_num.setIconSize(QtCore.QSize(24, 24))
ui.output_reset_ppr.setIconSize(QtCore.QSize(24, 24))
ui.output_reset_date.setIconSize(QtCore.QSize(24, 24))
ui.output_reset_output.setIconSize(QtCore.QSize(24, 24))
ui.edit_reset.setIconSize(QtCore.QSize(24, 24))
ui.admin_new_reset.setIconSize(QtCore.QSize(24, 24))

# Сокрытие паролей при вводе за "звездочками"
ui.login_pass.setEchoMode(QtGui.QLineEdit.Password)
ui.admin_new_pass.setEchoMode(QtGui.QLineEdit.Password)
ui.admin_new_conf_pass.setEchoMode(QtGui.QLineEdit.Password)
ui.chahge_pass_sel_user_old.setEchoMode(QtGui.QLineEdit.Password)
ui.chahge_pass_sel_user_new.setEchoMode(QtGui.QLineEdit.Password)
ui.chahge_pass_sel_user_conf.setEchoMode(QtGui.QLineEdit.Password)
ui.admin_del_user_pass_text.setEchoMode(QtGui.QLineEdit.Password)

# Подсказка для пользователя ао вкладке "Редактировать данные"
def set_edit():
    edit_text = "ВЫБЕРИТЕ ФАМИЛИЮ ИЗ СПИСКА ВО ВКЛАДКЕ 'НАЙТИ ДАННЫЕ'\
                            И ВЕРНИТЕСЬ К РЕДАКТИРОВАНИЮ"
    ui.fab_edit_text.setPlainText(edit_text)
set_edit()
# Добавление стран в комбо-боксы
def fill_civil():
    ui.civil_input.addItem("...")
    with open (r"txt/countries.txt", "r", encoding="utf-8") as f:
        item = f.readlines()
        for line in item:
            ui.civil_input.addItem(line.rstrip("\n"))
    f.close()
fill_civil()

# Добавление СГ в комбо-боксы
def fill_country():
    items = ("...", "Латвия", "Литва", "Польша", "Украина", "Россия", "Авиа") 
    for item in items:
        ui.info_country_input.addItem(item)
fill_country()

# Добавление ППР в комбо-боксы
def fill_ppr():
    ui.info_ppr_input.addItem("...")
    ui.info_ppr_output.addItem("...")
    with open (r"txt/ppr.txt", "r", encoding="utf-8") as f:
        item = f.readlines()
        for line in item:
            ui.info_ppr_input.addItem(line.rstrip("\n"))
            ui.info_ppr_output.addItem(line.rstrip("\n"))
    f.close()
fill_ppr()

# Добавление ед. измерения в количество
def fill_quant():
    items = ("...", "пачек", "грамм", "кг", "литров", "тонн", "бутылок", "единиц",
             "упаковок", "коробок", "голов", "туш") 
    for item in items:
        ui.quant_input_select.addItem(item)
fill_quant()


# Добавление ед. измерения в стоимость
def fill_price():
    items = ("...", "долларов США", "евро", "литов", "злотых",
             "гривен", "бел. рублей", "рос. рублей") 
    for item in items:
        ui.price_input_select.addItem(item)
fill_price()

# Добавление вида ТМЦ
def fill_sort():
    items = ("...", "сигареты и табак", "алкоголь", "автомобильное топливо",
             "наркотические средства", "психотропные вещества", "лекарственные препараты",
             "оружие и боеприпасы", "валюта", "драгоценности", "предметы искусства",
             "стройматериалы", "одежда", "продукты питания", "мобильные телефоны",
             "компьютеры", "бытовая техника", "агитационные материалы", "кино- видео- фотоматериалы",
             "лом цветных (черных) металлов", "транспортные средства",
             "ядовитые, радиоактивные вещества", "природные богатства", "животные", "туши животных",
             "научные разработки", "государственные секреты", "иное") 
    for item in items:
        ui.sort_input.addItem(item)
fill_sort()


# Добавление логинов в комбо-боксы для изменений и удалений
def fill_admin():
    ui.admin_del_user_select_2.clear()
    ui.admin_del_user_select.clear()
    ui.admin_del_user_select_2.addItem("...")
    ui.admin_del_user_select.addItem("...")    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
                
    sql_req = "SELECT * FROM users\
                ORDER BY users.user_id;"
    
    try:
        cur.execute(sql_req)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:       
        print("Ошибка: ", err)
    else:
        con.commit()
    
    cur.close()
    con.close()
    
      
    
    # Очистка поля вывода
#    ui.change_pass_status_label.clear()        
    
    # Компоновка полученных данных    
    # Вывод логинов в список    
    sur_combo = ""    
    for item in arr_output:
        sur_combo = item[1]
        ui.admin_del_user_select_2.addItem(sur_combo.rstrip("\n"))
        ui.admin_del_user_select.addItem(sur_combo.rstrip("\n"))


# Переопределение и добавление функций класса

# "Включение радио-кнопок"
def set_checked_direction():
    ui.info_dir_input_out.setChecked(True)
    ui.info_dir_output_out.setChecked(True)
set_checked_direction()

# Установление даты во всех вкладках
def reset_date():
    dt = datetime.datetime.today()
    ui.birth_input.setDate(dt.date())
    ui.info_date_input.setDate(dt.date())
    ui.info_date_output_from.setDate(dt.date())
    ui.info_date_output_to.setDate(dt.date())
    ui.info_date_output_date_from.setDate(dt.date())
    ui.info_date_output_date_to.setDate(dt.date())
reset_date()

# Установка режима календаря во всех полях даты
ui.birth_input.setCalendarPopup(True)
ui.info_date_input.setCalendarPopup(True)
ui.info_date_output_from.setCalendarPopup(True)
ui.info_date_output_to.setCalendarPopup(True)
ui.info_date_output_date_from.setCalendarPopup(True)
ui.info_date_output_date_to.setCalendarPopup(True)

# Для поиска по ППр
ui.info_ppr_output_label.setEnabled(False)

# Для вывода фамилий в поиске
ui.output_data_sur.addItem("...")

# Функция для прогресс-бара

def progress_bar():
    ui.intput_progressBar.setValue(0)
    t = 0
    for i in range(1, 11):
        t += 10
        ui.login_progressBar.setValue(t)        
        ui.intput_progressBar.setValue(t)
        ui.output_progressBar.setValue(t)
        ui.edit_progressBar.setValue(t)
        time.sleep(0.1)


# Функции объектов вкладки "Вход" (tab_login)

def login_enter():
    login_login = (ui.login_login.text()).upper()
    login_pass = ui.login_pass.text()
    
    if login_login == "" or login_pass == "":
        login_text = "ВЫ НЕ ВВЕЛИ ЛОГИН И(ИЛИ) ПАРОЛЬ"
        ui.login_info_label.setText(login_text)
    else:
        login_pass = login_pass.encode("utf-8")        
        login_pass = hashlib.md5(login_pass)
        login_pass = login_pass.hexdigest()
        
        con = sqlite3.connect("persona.db")
        cur = con.cursor()
        
        sql_arr = (login_login, login_pass)
        
        sql_req = "SELECT * FROM users\
                WHERE users.login=? AND\
                users.password=?\
                ORDER BY users.user_id;"
        
        try:
            cur.execute(sql_req, sql_arr)
            arr_output = cur.fetchall()
        except sqlite3.DatabaseError as err:
            admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
            ui.login_info_label.setText(admin_new_text)            
            print("Ошибка: ", err)
        else:
            login = ""
            passw = ""            
            for item in arr_output:
                login = item[1]
                passw = item[2]
            if login_login == login and login_pass == passw:
                text = "ДОБРО ПОЖАЛОВАТЬ, " + login_login.upper()
                ui.login_info_label.setText(text)
                con.commit()
                # Доступ к остальным вкладкам    
                ui.tab_input.setEnabled(True)
                ui.tab_output.setEnabled(True)
                ui.tab_edit.setEnabled(True)
                ui.tab_admin.setEnabled(True)
                ui.login_login.clear()
                ui.login_pass.clear()
                fill_admin()
                progress_bar()
            else:
                text = "ВЫ ОШИБЛИСЬ ПРИ ВВОДЕ ЛОГИНА ИЛИ ПАРОЛЯ"
                ui.login_info_label.setText(text)
        
        cur.close()
        con.close()
    

def login_reset():
    progress_bar()
    ui.login_login.clear()
    ui.login_pass.clear()

# Функции объектов вкладки "Ввести данные" (tab_input)


def input_write():      
    # Определение переменных с данными пользователя
    # Проверка типов и полноты данных (только основы)
    # Перевод в единый (верхний) регистр
    # Обработка ошибок
    name_input = (ui.name_input.text()).upper()
    if name_input == "":
        name_input = "Не указано"
        
    sur_input = (ui.sur_input.text()).upper()
    if sur_input == "":
        sur_input = "БЕЗ ФАМИЛИИ (РУС)"
        
    name_lat_input = (ui.name_lat_input.text()).upper()
    if name_lat_input == "":
        name_lat_input = "Не указано"
        
    sur_lat_input = (ui.sur_lat_input.text()).upper()
    if sur_lat_input == "":
        sur_lat_input = "БЕЗ ФАМИЛИИ (ЛАТ)"
        
    birth_input = ui.birth_input.dateTime().toPyDateTime().date().strftime("%d.%m.%Y")
        
    civil_input = ui.civil_input.currentText()
    if civil_input == "...":
        civil_input = "Не указано"
        
    pass_input = (ui.pass_input.text()).upper()
    if pass_input == "":
        pass_input = "Не указано"
        
    number_input = (ui.number_input.text()).upper()
    if number_input == "":
        number_input = "Не указано"
        
    number_auto_input = (ui.number_auto_input.text()).upper()
    if number_auto_input == "":
        number_auto_input = "Не указано"
   
    info_date_input = ui.info_date_input.dateTime().toPyDateTime().date().strftime("%d.%m.%Y")
    
    info_country_input = ui.info_country_input.currentText()
    if info_country_input == "...":
        info_country_input = "Не указано"
    
    def get_info_dir_input():   
        if ui.info_dir_input_in.isChecked():
            info_dir_input = "Въезд"
            return info_dir_input
        else:
            info_dir_input = "Выезд"
            return info_dir_input
    info_dir_input = get_info_dir_input()
    
    info_ppr_input = ui.info_ppr_input.currentText()
    if info_ppr_input == "...":
        info_ppr_input = "Не указано"
        
    info_who_input = (ui.info_who_input.text()).upper()
    if info_who_input == "":
        info_who_input = "Не указано"
        
    fab_input_text = ui.fab_input_text.toPlainText()
    if fab_input_text == "":
        fab_input_text = "Без описания правонарушения"
    
    quant_input_select = ui.quant_input_select.currentText()
    if quant_input_select == "...":
        quant_input_select = "Не указано"
        
    price_input_select = ui.price_input_select.currentText()
    if price_input_select == "...":
        price_input_select = "Не указано"
        
    sort_input = ui.sort_input.currentText()
    if sort_input == "...":
        sort_input = "Не указано"
    
    quant_input = ui.quant_input.text()
    if quant_input == "":
        quant_input = "0"
    quant_input = int(quant_input, 10)
    
    price_input = ui.price_input.text()
    if price_input == "":
        price_input = "0"
    price_input = int(price_input, 10)
    
    info_date_sys = ui.info_date_input.dateTime().toPyDateTime().date().strftime("%Y-%m-%d")
    
    # Подключение к БД и отправка запроса
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (name_input, sur_input, name_lat_input, sur_lat_input,
            birth_input, civil_input, pass_input, number_input,
            number_auto_input, info_date_input, info_country_input,
            info_dir_input, info_ppr_input, info_who_input, fab_input_text,
            sort_input, quant_input_select, quant_input, price_input_select,
            price_input, info_date_sys)
    
    sql_req = "INSERT INTO pers_data (pers_id, name, sur, name_lat,\
                sur_lat, birth, civil, passport, number_pers, number_auto,\
                date_info, country, direction, ppr, who, fab,\
                sort, quant_sel, quant, price_sel, price, date_sys)\
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                ?, ?, ?, ?, ?);"
    
    try:
        cur.execute(sql_req, sql_arr)
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.fab_input_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        text = "ЗАПИСЬ УСПЕШНО ДОБАВЛЕНА"
        ui.fab_input_text.setPlainText(text)
        con.commit()
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()
    
    # Очистка всех полей и сброс комбо-боксов
    input_reset()
    
    
def input_reset():
    # Имитация прогресса записи
    progress_bar()
    ui.name_input.clear()
    ui.sur_input.clear()
    ui.name_lat_input.clear()
    ui.sur_lat_input.clear()
    ui.pass_input.clear()
    ui.number_input.clear()
    ui.number_auto_input.clear()
    ui.info_who_input.clear()
    ui.quant_input.clear()
    ui.price_input.clear()
    ui.fab_input_text.clear() 
    reset_date()
    set_checked_direction()
    # Сброс комбо-боксов с последующим заполнением
    ui.civil_input.clear()
    fill_civil()
    ui.info_country_input.clear()
    fill_country()
    ui.info_ppr_input.clear()
    fill_ppr()
    ui.quant_input_select.clear()
    fill_quant()
    ui.price_input_select.clear()
    fill_price()
    ui.sort_input.clear()
    fill_sort()
    
# Функции объектов вкладки "Найти информацию" (tab_output)

def output_find_sur():
    # Получение данных от пользователя и сохранения их в переменные
    # Приведение к нужному типу и виду
    sur_output = (ui.sur_output.text()).upper()
    sur_lat_output = (ui.sur_lat_output.text()).upper()
    if sur_output == "БЕЗ ФАМИЛИИ (РУС)":
        sur_lat_output = "%" + sur_lat_output + "%"
    elif sur_lat_output == "БЕЗ ФАМИЛИИ (ЛАТ)":
        sur_output = "%" + sur_output + "%"
    elif sur_output == "":
        sur_output = "---"
        sur_lat_output = "%" + sur_lat_output + "%"
    elif sur_lat_output == "":
        sur_lat_output = "---"
        sur_output = "%" + sur_output + "%"
    else:
        sur_output = "%" + sur_output + "%"
        sur_lat_output = "%" + sur_lat_output + "%"
    
    # Запрос к базе данных
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (sur_output, sur_lat_output)
    
                
    sql_req = "SELECT * FROM pers_data\
                WHERE pers_data.sur LIKE ? OR\
                pers_data.sur_lat LIKE ?\
                ORDER BY pers_data.sur;"
    
    try:
        cur.execute(sql_req, sql_arr)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.output_data_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        if len(arr_output) != 0:
            text = "ДАННЫЕ УСПЕШНО НАЙДЕНЫ"
            ui.output_data_text.setPlainText(text)
            con.commit()
        else:
            text = "ПОИСК НЕ ДАЛ СООТВЕТСТВИЙ"
            ui.output_data_text.setPlainText(text)
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()    
    
    # Очистка поля вывода
    ui.output_data_text.clear()        
    
    # Компоновка полученных данных    
    output = ""   
    for item in arr_output:
        name = item[1]
        sur = item[2]    
        name_lat = item[3] 
        sur_lat = item[4] 
        birth = item[5] 
        civil = item[6] 
        passport = item[7] 
        number_pers = item[8] 
        number_auto = item[9] 
        date_info = item[10] 
        country = item[11]  
        direction = item[12] 
        ppr = item[13] 
        who = item[14]
        who = who.capitalize()
        fab = item[15] 
        sort = item[16] 
        quant_sel = item[17] 
        quant = item[18] 
        price_sel = item[19] 
        price = item[20]
        
        
        output += "Имя: " + name + "\n"
        output += "Фамилия: " + sur + "\n"
        output += "Имя (лат): " + name_lat + "\n"
        output += "Фамилия (лат): " + sur_lat + "\n"
        output += "Дата рождения: " + birth + "\n"
        output += "Гражданство: " + civil + "\n"
        output += "Номер паспорта: " + passport + "\n"
        output += "Личный номер: " + number_pers + "\n"
        output += "Номер автомобиля: " + number_auto + "\n"
        output += "Дата задержания: " + date_info + "\n"
        output += "Сопредельное государство: " + country + "\n"
        output += "Направление: " + direction + "\n"
        output += "Пункт пропуска: " + ppr + "\n"
        output += "Кем задержан: " + who + "\n"
        output += "Вид ТМЦ: " + sort + "\n"
        output += "В количестве: " + str(quant) + " " + quant_sel + "\n"
        output += "Стоимостью: " + str(price) + " " + price_sel + "\n"
        output += "Описание:\n"
        output += fab + "\n"
        output += "--------------------------------------------------------------\n"
        
    ui.output_data_text.setPlainText(output)
        

    
    # Вывод фамилий в список    
    sur_combo = ""    
    for item in arr_output:
        sur_combo = item[2]
        ui.output_data_sur.addItem(sur_combo.rstrip("\n"))
           
    # Количество
    count = 0
    for item in arr_output:
        count += 1        
    ui.output_data_total.display(count) 
    

def output_find_num():
    # Получение данных от пользователя и сохранения их в переменные
    # Приведение к нужному типу и виду
    pass_output = (ui.pass_output.text()).upper()
    auto_output = (ui.auto_output.text()).upper()
    if pass_output == "":
        pass_output = "String"
        auto_output = "%" + auto_output + "%"
    elif auto_output == "":
        auto_output = "String"
        pass_output = "%" + pass_output + "%"
    else:
        pass_output = "%" + pass_output + "%"
        auto_output = "%" + auto_output + "%"
    
    
    # Запрос к базе данных
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (pass_output, auto_output)
    
    sql_req = "SELECT * FROM pers_data\
                WHERE pers_data.passport LIKE ? OR\
                pers_data.number_auto LIKE ?\
                ORDER BY pers_data.sur;"
    
    try:
        cur.execute(sql_req, sql_arr)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.output_data_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        if len(arr_output) != 0:
            text = "ДАННЫЕ УСПЕШНО НАЙДЕНЫ"
            ui.output_data_text.setPlainText(text)
            con.commit()
        else:
            text = "ПОИСК НЕ ДАЛ СООТВЕТСТВИЙ"
            ui.output_data_text.setPlainText(text)
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()    
    
    # Очистка поля вывода
    ui.output_data_text.clear()        
    
    # Компоновка полученных данных    
    output = ""    
    for item in arr_output:
        name = item[1]
        sur = item[2]    
        name_lat = item[3] 
        sur_lat = item[4] 
        birth = item[5] 
        civil = item[6] 
        passport = item[7] 
        number_pers = item[8] 
        number_auto = item[9] 
        date_info = item[10] 
        country = item[11]  
        direction = item[12] 
        ppr = item[13] 
        who = item[14]
        who = who.capitalize()
        fab = item[15] 
        sort = item[16] 
        quant_sel = item[17] 
        quant = item[18] 
        price_sel = item[19] 
        price = item[20]
        
        output += "Имя: " + name + "\n"
        output += "Фамилия: " + sur + "\n"
        output += "Имя (лат): " + name_lat + "\n"
        output += "Фамилия (лат): " + sur_lat + "\n"
        output += "Дата рождения: " + birth + "\n"
        output += "Гражданство: " + civil + "\n"
        output += "Номер паспорта: " + passport + "\n"
        output += "Личный номер: " + number_pers + "\n"
        output += "Номер автомобиля: " + number_auto + "\n"
        output += "Дата задержания: " + date_info + "\n"
        output += "Сопредельное государство: " + country + "\n"
        output += "Направление: " + direction + "\n"
        output += "Пункт пропуска: " + ppr + "\n"
        output += "Кем задержан: " + who + "\n"
        output += "Вид ТМЦ: " + sort + "\n"
        output += "В количестве: " + str(quant) + " " + quant_sel + "\n"
        output += "Стоимостью: " + str(price) + " " + price_sel + "\n"
        output += "Описание:\n"
        output += fab + "\n"
        output += "--------------------------------------------------------------\n"        
        
    ui.output_data_text.setPlainText(output)

    
    # Вывод фамилий в список    
    sur_combo = ""    
    for item in arr_output:
        sur_combo = item[2]
        ui.output_data_sur.addItem(sur_combo.rstrip("\n"))
    
    # Количество
    count = 0
    for item in arr_output:
        count += 1        
    ui.output_data_total.display(count)   
      
def output_find_ppr():
    # Получение данных от пользователя и сохранения их в переменные
    # Приведение к нужному типу и виду
    def get_info_dir_output():   
        if ui.info_dir_output_in.isChecked():
            info_dir_output = "Въезд"
            return info_dir_output
        else:
            info_dir_output = "Выезд"
            return info_dir_output
    info_dir_output = get_info_dir_output()

    info_ppr_output = ui.info_ppr_output.currentText()
    
    info_date_output_from = ui.info_date_output_from.dateTime().toPyDateTime().date().strftime("%Y-%m-%d")
    info_date_output_to = ui.info_date_output_to.dateTime().toPyDateTime().date().strftime("%Y-%m-%d")
    
    # Запрос к базе данных
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (info_dir_output, info_ppr_output, info_date_output_from, info_date_output_to)
    
    sql_req = "SELECT * FROM pers_data\
                WHERE pers_data.direction=? AND\
                pers_data.ppr=? AND\
                pers_data.date_sys>=? AND\
                pers_data.date_sys<=?\
                ORDER BY pers_data.sur;"
    
    try:
        cur.execute(sql_req, sql_arr)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.output_data_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        if len(arr_output) != 0:
            text = "ДАННЫЕ УСПЕШНО НАЙДЕНЫ"
            ui.output_data_text.setPlainText(text)
            con.commit()
        else:
            text = "ПОИСК НЕ ДАЛ СООТВЕТСТВИЙ"
            ui.output_data_text.setPlainText(text)
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()    
    
    # Очистка поля вывода
    ui.output_data_text.clear()        
    
    # Компоновка полученных данных    
    output = ""    
    for item in arr_output:
        name = item[1]
        sur = item[2]    
        name_lat = item[3] 
        sur_lat = item[4] 
        birth = item[5] 
        civil = item[6] 
        passport = item[7] 
        number_pers = item[8] 
        number_auto = item[9] 
        date_info = item[10] 
        country = item[11]  
        direction = item[12] 
        ppr = item[13] 
        who = item[14]
        who = who.capitalize()
        fab = item[15] 
        sort = item[16] 
        quant_sel = item[17] 
        quant = item[18] 
        price_sel = item[19] 
        price = item[20]
        
        output += "Имя: " + name + "\n"
        output += "Фамилия: " + sur + "\n"
        output += "Имя (лат): " + name_lat + "\n"
        output += "Фамилия (лат): " + sur_lat + "\n"
        output += "Дата рождения: " + birth + "\n"
        output += "Гражданство: " + civil + "\n"
        output += "Номер паспорта: " + passport + "\n"
        output += "Личный номер: " + number_pers + "\n"
        output += "Номер автомобиля: " + number_auto + "\n"
        output += "Дата задержания: " + date_info + "\n"
        output += "Сопредельное государство: " + country + "\n"
        output += "Направление: " + direction + "\n"
        output += "Пункт пропуска: " + ppr + "\n"
        output += "Кем задержан: " + who + "\n"
        output += "Вид ТМЦ: " + sort + "\n"
        output += "В количестве: " + str(quant) + " " + quant_sel + "\n"
        output += "Стоимостью: " + str(price) + " " + price_sel + "\n"
        output += "Описание:\n"
        output += fab + "\n"
        output += "--------------------------------------------------------------\n"
        
    ui.output_data_text.setPlainText(output)

    
    # Вывод фамилий в список    
    sur_combo = ""   
    for item in arr_output:
        sur_combo = item[2]
        ui.output_data_sur.addItem(sur_combo.rstrip("\n"))
    
    # Количество
    count = 0
    for item in arr_output:
        count += 1        
    ui.output_data_total.display(count)  
    

def output_find_date():
    # Получение данных от пользователя и сохранения их в переменные
    # Приведение к нужному типу и виду
    info_date_output_date_from = ui.info_date_output_date_from.dateTime().toPyDateTime().date().strftime("%Y-%m-%d")
    info_date_output_date_to = ui.info_date_output_date_to.dateTime().toPyDateTime().date().strftime("%Y-%m-%d")
    
    # Запрос к базе данных
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (info_date_output_date_from, info_date_output_date_to)
    
    sql_req = "SELECT * FROM pers_data\
                WHERE pers_data.date_sys>=? AND\
                pers_data.date_sys<=?\
                ORDER BY pers_data.sur;"
    
    try:
        cur.execute(sql_req, sql_arr)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.output_data_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        if len(arr_output) != 0:
            text = "ДАННЫЕ УСПЕШНО НАЙДЕНЫ"
            ui.output_data_text.setPlainText(text)
            con.commit()
        else:
            text = "ПОИСК НЕ ДАЛ СООТВЕТСТВИЙ"
            ui.output_data_text.setPlainText(text)
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()    
    
    # Очистка поля вывода
    ui.output_data_text.clear()        
    
    # Компоновка полученных данных    
    output = ""    
    for item in arr_output:
        name = item[1]
        sur = item[2]    
        name_lat = item[3] 
        sur_lat = item[4] 
        birth = item[5] 
        civil = item[6] 
        passport = item[7] 
        number_pers = item[8] 
        number_auto = item[9] 
        date_info = item[10] 
        country = item[11]  
        direction = item[12] 
        ppr = item[13] 
        who = item[14]
        who = who.capitalize()
        fab = item[15] 
        sort = item[16] 
        quant_sel = item[17] 
        quant = item[18] 
        price_sel = item[19] 
        price = item[20]
        
        output += "Имя: " + name + "\n"
        output += "Фамилия: " + sur + "\n"
        output += "Имя (лат): " + name_lat + "\n"
        output += "Фамилия (лат): " + sur_lat + "\n"
        output += "Дата рождения: " + birth + "\n"
        output += "Гражданство: " + civil + "\n"
        output += "Номер паспорта: " + passport + "\n"
        output += "Личный номер: " + number_pers + "\n"
        output += "Номер автомобиля: " + number_auto + "\n"
        output += "Дата задержания: " + date_info + "\n"
        output += "Сопредельное государство: " + country + "\n"
        output += "Направление: " + direction + "\n"
        output += "Пункт пропуска: " + ppr + "\n"
        output += "Кем задержан: " + who + "\n"
        output += "Вид ТМЦ: " + sort + "\n"
        output += "В количестве: " + str(quant) + " " + quant_sel + "\n"
        output += "Стоимостью: " + str(price) + " " + price_sel + "\n"
        output += "Описание:\n"
        output += fab + "\n"
        output += "--------------------------------------------------------------\n"
        
    ui.output_data_text.setPlainText(output)

    
    # Вывод фамилий в список    
    sur_combo = ""   
    for item in arr_output:
        sur_combo = item[2]
        ui.output_data_sur.addItem(sur_combo.rstrip("\n"))
    
    # Количество
    count = 0
    for item in arr_output:
        count += 1        
    ui.output_data_total.display(count)  
    
def output_find_all():
    # Получение данных от пользователя и сохранения их в переменные
    # Приведение к нужному типу и виду
    # Запрос к базе данных
    
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
                
    sql_req = "SELECT * FROM pers_data\
                ORDER BY pers_data.sur;"
    
    try:
        cur.execute(sql_req)
        arr_output = cur.fetchall()
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.output_data_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        if len(arr_output) != 0:
            text = "ДАННЫЕ УСПЕШНО НАЙДЕНЫ"
            ui.output_data_text.setPlainText(text)
            con.commit()
        else:
            text = "ПОИСК НЕ ДАЛ СООТВЕТСТВИЙ"
            ui.output_data_text.setPlainText(text)
    
    cur.close()
    con.close()
    
    # Имитация прогресса записи
    progress_bar()    
    
    # Очистка поля вывода
    ui.output_data_text.clear()        
    
    # Компоновка полученных данных    
    output = ""   
    for item in arr_output:
        name = item[1]
        sur = item[2]    
        name_lat = item[3] 
        sur_lat = item[4] 
        birth = item[5] 
        civil = item[6] 
        passport = item[7] 
        number_pers = item[8] 
        number_auto = item[9] 
        date_info = item[10] 
        country = item[11]  
        direction = item[12] 
        ppr = item[13] 
        who = item[14]
        who = who.capitalize()
        fab = item[15] 
        sort = item[16] 
        quant_sel = item[17] 
        quant = item[18] 
        price_sel = item[19] 
        price = item[20]
        
        
        output += "Имя: " + name + "\n"
        output += "Фамилия: " + sur + "\n"
        output += "Имя (лат): " + name_lat + "\n"
        output += "Фамилия (лат): " + sur_lat + "\n"
        output += "Дата рождения: " + birth + "\n"
        output += "Гражданство: " + civil + "\n"
        output += "Номер паспорта: " + passport + "\n"
        output += "Личный номер: " + number_pers + "\n"
        output += "Номер автомобиля: " + number_auto + "\n"
        output += "Дата задержания: " + date_info + "\n"
        output += "Сопредельное государство: " + country + "\n"
        output += "Направление: " + direction + "\n"
        output += "Пункт пропуска: " + ppr + "\n"
        output += "Кем задержан: " + who + "\n"
        output += "Вид ТМЦ: " + sort + "\n"
        output += "В количестве: " + str(quant) + " " + quant_sel + "\n"
        output += "Стоимостью: " + str(price) + " " + price_sel + "\n"
        output += "Описание:\n"
        output += fab + "\n"
        output += "--------------------------------------------------------------\n"
        
    ui.output_data_text.setPlainText(output)
        

    
    # Вывод фамилий в список    
    sur_combo = ""    
    for item in arr_output:
        sur_combo = item[2]
        ui.output_data_sur.addItem(sur_combo.rstrip("\n"))
           
    # Количество
    count = 0
    for item in arr_output:
        count += 1        
    ui.output_data_total.display(count) 
    

def output_reset_sur():
    # Имитация прогресса записи
    progress_bar()
    ui.sur_output.clear()
    ui.sur_lat_output.clear()

def output_reset_num():
    # Имитация прогресса записи
    progress_bar()
    ui.pass_output.clear()
    ui.auto_output.clear()
    
def output_reset_ppr():
    # Имитация прогресса записи
    progress_bar()
    ui.info_ppr_output.clear()
    fill_ppr()
    set_checked_direction()
    reset_date()
    
def output_reset_date():
    # Имитация прогресса записи
    progress_bar()
    reset_date()    
    
def output_reset_output():
    # Имитация прогресса записи
    progress_bar()
    ui.output_data_text.clear()
    ui.output_data_total.display(0)
    ui.output_data_sur.clear()
    ui.output_data_sur.addItem("...")
    
def output_export():
    data = ui.output_data_text.toPlainText()
    with open (r"Persona.doc", "w", encoding="utf-8") as f:
        f.write(data)
    f.close()
    progress_bar()
    
def output_export_pdf():
    data = ui.output_data_text.toPlainText()    
    printer = QtGui.QPrinter()
    printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
    printer.setOutputFileName("Persona.pdf")
    document = QtGui.QTextDocument()
    document.setPlainText(data)
    ui.output_data_text.setDocument(document)    
    ui.output_data_text.document().print_(printer)
    progress_bar()

# Функция комбо-бокса со списком найденных фамилий
def find_selected_sur():
    sur_find = ui.output_data_sur.currentText()
    cursor = ui.output_data_text.document().find(sur_find, position=0)
    ui.output_data_text.setTextCursor(cursor)
 
# Функции объектов вкладки "Редактировать данные" (tab_edit)	
	
def edit_fill():
    if ui.output_data_sur.currentText() == "...":
        edit_text = "ВЫБЕРИТЕ ФАМИЛИЮ ИЗ СПИСКА ВО ВКЛАДКЕ 'НАЙТИ ДАННЫЕ'\
                        И ВЕРНИТЕСЬ К РЕДАКТИРОВАНИЮ"
        ui.fab_edit_text.setPlainText(edit_text)
    else:
        edit_id = 0        
        edit_sur = ui.output_data_sur.currentText()
        # Запрос к базе данных
        con = sqlite3.connect("persona.db")
        cur = con.cursor()
        
        sql_arr = (edit_id, edit_sur)
        
                    
        sql_req = "SELECT * FROM pers_data\
                    WHERE pers_data.pers_id>? AND\
                    pers_data.sur=?\
                    ORDER BY pers_data.sur;"
        
        try:
            cur.execute(sql_req, sql_arr)
            arr_output = cur.fetchall()
        except sqlite3.DatabaseError as err:
            text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
            ui.fab_edit_text.setPlainText(text)        
            print("Ошибка: ", err)
        else:
            if len(arr_output) != 0:
                text = "ДАННЫЕ ДЛЯ РЕДАКТИРОВАНИЯ НАЙДЕНЫ"
                ui.fab_edit_text.setPlainText(text)
                con.commit()
            else:
                text = "НЕТ ДАННЫХ ДЛЯ РЕДАКТИРОВАНИЯ"
                ui.fab_edit_text.setPlainText(text)
        
        cur.close()
        con.close()
        
        
        # Очистка поля вывода
        ui.fab_edit_text.clear()        
        
        # Компоновка полученных данных
        for item in arr_output:
            name = item[1]
            sur = item[2]    
            name_lat = item[3] 
            sur_lat = item[4] 
            birth = item[5] 
            civil = item[6] 
            passport = item[7] 
            number_pers = item[8] 
            number_auto = item[9] 
            date_info = item[10] 
            country = item[11]  
            direction = item[12] 
            ppr = item[13] 
            who = item[14]
            fab = item[15] 
            sort = item[16] 
            quant_sel = item[17] 
            quant = item[18]
            quant = str(quant)
            price_sel = item[19] 
            price = item[20]
            price = str(price)
            
        ui.name_edit.setText(name)
        ui.sur_edit.setText(sur)
        ui.name_lat_edit.setText(name_lat)
        ui.sur_lat_edit.setText(sur_lat)
        ui.birth_edit.setText(birth)
        ui.civil_edit.setText(civil)
        ui.pass_edit.setText(passport)
        ui.number_edit.setText(number_pers)
        ui.number_auto_edit.setText(number_auto)
        ui.info_date_edit.setText(date_info)
        ui.info_country_edit.setText(country)
        ui.info_dir_edit.setText(direction)
        ui.info_ppr_edit.setText(ppr)
        ui.info_who_edit.setText(who)
        ui.fab_edit_text.setPlainText(fab)
        ui.sort_edit.setText(sort)
        ui.quant_edit_select.setText(quant_sel)
        ui.quant_edit.setText(quant)
        ui.price_edit_select.setText(price_sel)
        ui.price_edit.setText(price)
        
def edit_write():
    name = (ui.name_edit.text()).upper()
    if name == "":
        name = "Не указано"
        
    sur = (ui.sur_edit.text()).upper()
    if sur == "":
        sur = "Не указано"
        
    name_lat = (ui.name_lat_edit.text()).upper()
    if name_lat == "":
        name_lat = "Не указано"
        
    sur_lat = (ui.sur_lat_edit.text()).upper()
    if sur_lat == "":
        sur_lat = "Не указано"
        
    birth = ui.birth_edit.text()
    if birth == "":
        birth = "Не указано"
        
    civil = ui.civil_edit.text()
    if civil == "":
        civil = "Не указано"
        
    passport = (ui.pass_edit.text()).upper()
    if passport == "":
        passport = "Не указано"
        
    number_pers = (ui.number_edit.text()).upper()
    if number_pers == "":
        number_pers = "Не указано"
        
    number_auto = (ui.number_auto_edit.text()).upper()
    if number_auto == "":
        number_auto = "Не указано"
        
    date_info = ui.info_date_edit.text()
    if date_info == "":
        date_info = "Не указано"
        
    country = ui.info_country_edit.text()
    if country == "":
        country = "Не указано"
        
    direction = ui.info_dir_edit.text()
    if direction != "Выезд":
        direction = "Въезд"
    
    ppr = ui.info_ppr_edit.text()
    if ppr == "":
        ppr = "Не указано"
        
    who = ui.info_who_edit.text()
    if who == "":
        who = "Не указано"
        
    fab = ui.fab_edit_text.toPlainText()
    if fab == "":
        fab = "Без описания правонарушения"
    
    sort = ui.sort_edit.text()
    if sort == "":
        sort = "Не указано"
        
    quant_sel = ui.quant_edit_select.text()
    if quant_sel == "":
        quant_sel = "Не указано"
    
    quant = ui.quant_edit.text()
    if quant == "":
        quant = "0"
    quant = int(quant, 10)    
    
    price_sel = ui.price_edit_select.text()
    if price_sel == "":
        price_sel = "Не указано"
    
    price = ui.price_edit.text()
    if price == "":
        price = "0"
    price = int(price, 10)
    
    # Запрос к базе данных
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (name, sur, name_lat, sur_lat, birth, civil, passport,
               number_pers, number_auto, date_info, country, direction,
               ppr, who, fab, sort, quant_sel, quant, price_sel, price,
               sur)

    sql_req = "UPDATE pers_data SET\
                name=?, sur=?, name_lat=?, sur_lat=?, birth=?, civil=?, passport=?,\
                number_pers=?, number_auto=?, date_info=?, country=?, direction=?,\
                ppr=?, who=?, fab=?, sort=?, quant_sel=?, quant=?, price_sel=?, price=?\
                WHERE sur=?;"
    
    try:
        cur.execute(sql_req, sql_arr)
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.fab_edit_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        text = "ДАННЫЕ УСПЕШНО ОБНОВЛЕНЫ"
        ui.fab_edit_text.setPlainText(text)
        con.commit()
    
    cur.close()
    con.close()

     # Имитация прогресса записи
    progress_bar()        
	
def edit_reset():
    ui.name_edit.clear()
    ui.sur_edit.clear()
    ui.name_lat_edit.clear()
    ui.sur_lat_edit.clear()
    ui.birth_edit.clear()
    ui.civil_edit.clear()
    ui.pass_edit.clear()
    ui.number_edit.clear()
    ui.number_auto_edit.clear()
    ui.info_date_edit.clear()
    ui.info_country_edit.clear()
    ui.info_dir_edit.clear()
    ui.info_ppr_edit.clear()
    ui.info_who_edit.clear()
    ui.fab_edit_text.clear()
    ui.sort_edit.clear()
    ui.quant_edit_select.clear()
    ui.quant_edit.clear()
    ui.price_edit_select.clear()
    ui.price_edit.clear()
    # Имитация прогресса записи
    progress_bar()
    set_edit()

def edit_delete():
    sur = (ui.sur_edit.text()).upper()
    if sur == "":
        sur = "Не указано"
        
    date_info = ui.info_date_edit.text()
    if date_info == "":
        date_info = "Не указано"

    country = ui.info_country_edit.text()
    if country == "":
        country = "Не указано"
        
    direction = ui.info_dir_edit.text()
    if direction != "Выезд":
        direction = "Въезд"
    
    # Запрос к базе данных
    con = sqlite3.connect("persona.db")
    cur = con.cursor()
    
    sql_arr = (sur, date_info, country, direction)

    sql_req = "DELETE FROM pers_data WHERE\
                sur=? AND date_info=? AND\
                country=? AND direction=?;"
    
    try:
        cur.execute(sql_req, sql_arr)
    except sqlite3.DatabaseError as err:
        text = "ОШИБКА ПРИ ПОДКЛЮЧЕНИИ К БАЗЕ ДАННЫХ"
        ui.fab_edit_text.setPlainText(text)        
        print("Ошибка: ", err)
    else:
        text = "ЗАПИСЬ УСПЕШНО УДАЛЕНА"
        ui.fab_edit_text.setPlainText(text)
        con.commit()
    
    cur.close()
    con.close()
    
     # Имитация прогресса записи
    progress_bar()
	
# Функции объектов вкладки "Панель администратора" (tab_admin)
    
def admin_new_write():
    admin_new_name = (ui.admin_new_name.text()).upper()
    admin_new_pass = ui.admin_new_pass.text()
    admin_new_conf_pass = ui.admin_new_conf_pass.text()
    
    if admin_new_name == "" or admin_new_pass == "":
        admin_new_text = "ВЫ НЕ ВВЕЛИ ЛОГИН И(ИЛИ) ПАРОЛЬ"
        ui.add_user_status_label.setText(admin_new_text)
    elif admin_new_pass != admin_new_conf_pass:
        admin_new_text = "ПАРОЛЬ И ЕГО ПОДТВЕРЖДЕНИЕ НЕ СОВПАДАЮТ"
        ui.add_user_status_label.setText(admin_new_text)
    else:
        admin_new_pass = admin_new_pass.encode("utf-8")        
        admin_new_pass = hashlib.md5(admin_new_pass)
        admin_new_pass = admin_new_pass.hexdigest()
        
        con = sqlite3.connect("persona.db")
        cur = con.cursor()
        
        sql_arr = (admin_new_name, admin_new_pass)
        
        sql_req = "INSERT INTO users (user_id, login, password)\
                    VALUES (NULL, ?, ?);"
        
        try:
            cur.execute(sql_req, sql_arr)
        except sqlite3.DatabaseError as err:
            admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
            ui.add_user_status_label.setText(admin_new_text)            
            print("Ошибка: ", err)
        else:
            admin_new_text = "ПОЛЬЗОВАТЕЛЬ УСПЕШНО ДОБАВЛЕН"
            ui.add_user_status_label.setText(admin_new_text)
            con.commit()
        
        cur.close()
        con.close()
        
        
    
def admin_new_reset():
    ui.admin_new_name.clear()
    ui.admin_new_pass.clear()
    ui.admin_new_conf_pass.clear()
    ui.add_user_status_label.clear()
    

    
def chahge_pass_user():
    login_login = ui.admin_del_user_select_2.currentText()
    login_pass = ui.chahge_pass_sel_user_old.text()
    
    if login_login == "..." or login_pass == "":
        login_text = "ВЫ НЕ ВВЕЛИ ЛОГИН ИЛИ СТАРЫЙ ПАРОЛЬ"
        ui.change_pass_status_label.setText(login_text)
    else:
        login_pass = login_pass.encode("utf-8")        
        login_pass = hashlib.md5(login_pass)
        login_pass = login_pass.hexdigest()
        
        con = sqlite3.connect("persona.db")
        cur = con.cursor()
        
        sql_arr = (login_login, login_pass)
        
        sql_req = "SELECT * FROM users\
                WHERE users.login=? AND\
                users.password=?\
                ORDER BY users.user_id;"
        
        try:
            cur.execute(sql_req, sql_arr)
            arr_output = cur.fetchall()
        except sqlite3.DatabaseError as err:
            admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
            ui.change_pass_status_label.setText(admin_new_text)            
            print("Ошибка: ", err)
        else:
            login = ""
            passw = ""            
            for item in arr_output:
                login = item[1]
                passw = item[2]
            if login_login == login and login_pass == passw:
                # Запрос к базе данных
                pass_new = ui.chahge_pass_sel_user_new.text()
                pass_conf = ui.chahge_pass_sel_user_conf.text()
                
                if pass_new == "" or pass_conf == "":
                    login_text = "ВЫ НЕ ВВЕЛИ НОВЫЙ ПАРОЛЬ"
                    ui.change_pass_status_label.setText(login_text)
                elif pass_new != pass_conf:
                    login_text = "ПАРОЛЬ И ПОДТВЕРЖДЕНИЕ НЕ СОВПАДАЮТ"
                    ui.change_pass_status_label.setText(login_text)
                else:
                    con.commit()                         
                    cur.close()
                    con.close()
                    
                    con = sqlite3.connect("persona.db")
                    cur = con.cursor()
                    
                    pass_new = pass_new.encode("utf-8")        
                    pass_new = hashlib.md5(pass_new)
                    pass_new = pass_new.hexdigest()
                    
                    sql_arr = (pass_new, login)
        
                    sql_req = "UPDATE users\
                                SET password=?\
                                WHERE login=?;"
                                
                    try:
                        cur.execute(sql_req, sql_arr)
                    except sqlite3.DatabaseError as err:
                        admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
                        ui.change_pass_status_label.setText(admin_new_text)            
                        print("Ошибка: ", err)
                    else:
                        admin_new_text = "ПАРОЛЬ ДЛЯ " + login + " ИЗМЕНЕН"
                        ui.change_pass_status_label.setText(admin_new_text)
                        con.commit()                    
                        ui.chahge_pass_sel_user_old.clear()
                        ui.chahge_pass_sel_user_new.clear()
                        ui.chahge_pass_sel_user_conf.clear()
                        fill_admin()
                    
                    cur.close()
                    con.close()    
    
def admin_del_user():
    login_login = ui.admin_del_user_select.currentText()
    login_pass = ui.admin_del_user_pass_text.text()
    
    if login_login == "..." or login_pass == "":
        login_text = "ВЫ НЕ ВВЕЛИ ЛОГИН ИЛИ ПАРОЛЬ"
        ui.del_user_status_label.setText(login_text)
    elif login_login == "ADMIN":
        login_text = "НЕЛЬЗЯ УДАЛИТЬ ADMIN"
        ui.del_user_status_label.setText(login_text)         
    else:
        login_admin = "ADMIN"
        login_pass = login_pass.encode("utf-8")        
        login_pass = hashlib.md5(login_pass)
        login_pass = login_pass.hexdigest()
        
        con = sqlite3.connect("persona.db")
        cur = con.cursor()
        
        sql_arr = (login_admin, login_pass)
        
        sql_req = "SELECT * FROM users\
                WHERE users.login=? AND\
                users.password=?\
                ORDER BY users.user_id;"
        
        try:
            cur.execute(sql_req, sql_arr)
            arr_output = cur.fetchall()
        except sqlite3.DatabaseError as err:
            admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
            ui.del_user_status_label.setText(admin_new_text)            
            print("Ошибка: ", err)
        else:
            login = ""
            passw = ""            
            for item in arr_output:                
                login = item[1]
                passw = item[2]
            if login_admin == login and login_pass == passw:
                con.commit()                         
                cur.close()
                con.close()
                
                con = sqlite3.connect("persona.db")
                cur = con.cursor()
                
                login_idn = 0
                
                sql_arr = (login_idn, login_login)
    
                sql_req = "DELETE FROM users\
                            WHERE user_id>? AND\
                            login=?;"
                            
                try:
                    cur.execute(sql_req, sql_arr)
                except sqlite3.DatabaseError as err:
                    admin_new_text = "ОШИБКА ДОСТУПА К БАЗЕ ДАННЫХ"
                    ui.del_user_status_label.setText(admin_new_text)            
                    print("Ошибка: ", err)
                else:
                    admin_new_text = "ПОЛЬЗОВАТЕЛЬ " + login_login + " УДАЛЕН"
                    ui.del_user_status_label.setText(admin_new_text)
                    con.commit()                    
                    ui.admin_del_user_pass_text.clear()
                    fill_admin()
                
                cur.close()
                con.close()            


# Функции объектов вкладки "О программе" (tab_about)

# Общие функции для нескольких вкладок

# Установка зависимости выбора ППР от флажка-лэйбла в трех вкладках

def active_ppr_input():
    if ui.info_ppr_input_label.checkState() == 2:
        ui.info_ppr_input.setEnabled(True)
    else:
        ui.info_ppr_input.setEnabled(False)
        ui.info_ppr_input.clear()
        fill_ppr()
        
def active_ppr_output():
    if ui.info_ppr_output_label.checkState() == 2:
        ui.info_ppr_output.setEnabled(True)
    else:
        ui.info_ppr_output.setEnabled(False)
        ui.info_ppr_output.clear()
        fill_ppr()



    

# СИГНАЛЫ

# Сигналы объектов вкладки "Вход" (tab_login)

QtCore.QObject.connect(ui.login_enter, QtCore.SIGNAL("clicked()"),
                      login_enter)
                      
QtCore.QObject.connect(ui.login_reset, QtCore.SIGNAL("clicked()"),
                      login_reset)  

# Сигналы объектов вкладки "Ввести данные" (tab_input)  

QtCore.QObject.connect(ui.input_write, QtCore.SIGNAL("clicked()"),
                      input_write)
                      
QtCore.QObject.connect(ui.input_reset, QtCore.SIGNAL("clicked()"),
                      input_reset)
                            


# Сигналы объектов вкладки "Найти информацию" (tab_output)

QtCore.QObject.connect(ui.output_find_sur, QtCore.SIGNAL("clicked()"),
                      output_find_sur)
                      
QtCore.QObject.connect(ui.output_find_num, QtCore.SIGNAL("clicked()"),
                      output_find_num)

QtCore.QObject.connect(ui.output_find_ppr, QtCore.SIGNAL("clicked()"),
                      output_find_ppr)
                      
QtCore.QObject.connect(ui.output_find_date, QtCore.SIGNAL("clicked()"),
                      output_find_date)                      
                      
QtCore.QObject.connect(ui.output_find_all, QtCore.SIGNAL("clicked()"),
                      output_find_all)                      
                      
                      
QtCore.QObject.connect(ui.output_reset_sur, QtCore.SIGNAL("clicked()"),
                      output_reset_sur)
                      
QtCore.QObject.connect(ui.output_reset_num, QtCore.SIGNAL("clicked()"),
                      output_reset_num)

QtCore.QObject.connect(ui.output_reset_ppr, QtCore.SIGNAL("clicked()"),
                      output_reset_ppr)
                      
QtCore.QObject.connect(ui.output_reset_date, QtCore.SIGNAL("clicked()"),
                      output_reset_date)                      

QtCore.QObject.connect(ui.output_reset_output, QtCore.SIGNAL("clicked()"),
                      output_reset_output)
                      

QtCore.QObject.connect(ui.output_export, QtCore.SIGNAL("clicked()"),
                      output_export)
                
QtCore.QObject.connect(ui.output_export_pdf, QtCore.SIGNAL("clicked()"),
                      output_export_pdf)            
                      
# Сигнал комбо-бокса со списком найденных фамилий
QtCore.QObject.connect(ui.output_data_sur, QtCore.SIGNAL("activated(int)"),
                      find_selected_sur)
                      
QtCore.QObject.connect(ui.output_data_sur, QtCore.SIGNAL("activated(int)"),
                      edit_fill)                    


					  
# Сигналы объектов вкладки "Редактировать данные" (tab_edit)

QtCore.QObject.connect(ui.edit_write, QtCore.SIGNAL("clicked()"),
                      edit_write)
                      
QtCore.QObject.connect(ui.edit_reset, QtCore.SIGNAL("clicked()"),
                      edit_reset)

QtCore.QObject.connect(ui.edit_delete, QtCore.SIGNAL("clicked()"),
                      edit_delete)
                      
# Сигналы объектов вкладки "Панель администратора" (tab_admin)
                      
QtCore.QObject.connect(ui.admin_new_write, QtCore.SIGNAL("clicked()"),
                      admin_new_write)
                      
QtCore.QObject.connect(ui.admin_new_reset, QtCore.SIGNAL("clicked()"),
                      admin_new_reset)                      
                      
QtCore.QObject.connect(ui.chahge_pass_user, QtCore.SIGNAL("clicked()"),
                      chahge_pass_user)   
                      
QtCore.QObject.connect(ui.admin_del_user, QtCore.SIGNAL("clicked()"),
                      admin_del_user)                                          
                      
                      
# Сигналы объектов вкладки "О программе" (tab_about)

with open (r"txt/about.txt", "r", encoding="utf-8") as f:
        about_text = f.read()
        ui.about_label.setPixmap(QtGui.QPixmap("icons/icon_about_2.png"))
        ui.about_label_2.setPixmap(QtGui.QPixmap("icons/icon_about.png"))
        ui.about_label_3.setText(about_text)
f.close()

#ui.about_label.setPixmap(QtGui.QPixmap("icons/icon_about.png")


# Общие сигналы для нескольких вкладок

QtCore.QObject.connect(ui.info_ppr_input_label, QtCore.SIGNAL("clicked()"),
                      active_ppr_input)
                      
QtCore.QObject.connect(ui.info_ppr_output_label, QtCore.SIGNAL("clicked()"),
                      active_ppr_output)
                      

window.show()
sys.exit(app.exec_())

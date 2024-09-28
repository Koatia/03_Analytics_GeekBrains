Sub Макрос1()
'
' Макрос1 Макрос
' Выделение ячеек с данными в текущем столбце и установка желтой заливки
'

'
    Selection.End(xlUp).Select
    Range(Selection, Selection.End(xlDown)).Select
    With Selection.Interior
        .PatternColorIndex = xlAutomatic
        .Color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
End Sub

Public Function diff_module(a As Integer, b As Integer) As Integer
'
' Задача 2: Создайте пользовательскую функцию, которая принимает два аргумента и возвращает модуль их разницы
' (убирает минус, если он есть, например модуль 2 возвращает 2, модуль -2 возвращает тоже 2)

diff_module = Abs(a - b)

End Function

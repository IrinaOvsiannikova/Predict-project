# Проект по прогнозированию размеров сварного шва при электронно-лучевой сварке тонкостенных конструкций аэрокосмического назначения.

Репозиторий содержит следующие файлы:
* ebw_data.csv - датасет с результатами экспериментальных исследований, проводимых в целях улучшения технологического процесса электронно-лучевой сварки изделия,  сборка которого состоит из элементов, состоящих из разнородного материала;
* Final.ipunb - файл с предобработанными данными и собранной моделью нейронной сети;
* linear_model - сохраненная модель;
* templates - код html страницы;
* app.py - код с приложением для прогнозирования размеров сварного шва.

В проекте реализовано:
1) Изучение и предобработка данных.
2) Создание четырех моделей нейроной сети, учитывающих разные параметры для прогнозирования размеров сварного шва.
3) Выбор и сохранение лучшей модели.
4) Написание кода приложения для прогнозирования размеров сварного шва.

В результате проекта: 
* Реализовано приложение, позволяющее спрогнозировать размеры сварного шва, а именно - глубину и ширину, в зависимости от параметров: величина сварочного тока, тока фокусировки электронного пучка, скорости сварки и расстояния от поверхности образцов до электронно-оптической системы.


Стек – Pandas, numpy, matplotlib.pyplot, tensorflow.

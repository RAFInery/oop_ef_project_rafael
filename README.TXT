//Grundidee des Programms//
Das Programm soll es ermöglichen, alltägliche Ausgaben auf einfache Weise auf einer Liste zusammenzufassen und dem Nutzer praktische Statistiken im Zusammenhang zu festgelegten Budgets pro Bereich (Kleidung, Essen/Verpflegung, Ausgang/Freizeit, Hygiene, Handyabbo) zu geben.

31.08.18
Da ich das Programm schon vor Projektbeginn zu programmieren begonnen habe, läuft das Programm schon. Als erster Schritt wird nun das funktionsfähige Programm in die Struktur des objekt orientierten Programmierens gebracht. Bis jezt wurden 3/4 des Programms in drei Klassen übersetzt: 
Stock: Kümmert sich um die Funktionalität rund um das Budget.
Entry: Kümmert sich um neue Einträge bestehend aus: Summe, Grund/Verwendungszweck und Datum.
Cycle (Entry): Kümmert sich um den Kreislauf, damit mehrere Einträge in einem Programmdurchlauf verarbeitet werden können.
-->Die beiden Klassen Stock und Entry bilden je ein eigenes File und die Cycle-Klasse befindet sich als Erb-klasse in dem File der Entry-Klasse. Alle Klassen werden im Main-File vereint.

Zurzeit wurde nur die Stock-Klasse auf die Funktionalität überprüft, als weitere Schritte werden die beiden weiteren Klassen getestet und der letzte Teil ins oop. umconvertiert.



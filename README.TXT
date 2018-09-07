//Grundidee des Programms//
Das Programm soll es ermöglichen, alltägliche Ausgaben auf einfache Weise auf einer Liste zusammenzufassen und dem Nutzer praktische Statistiken im Zusammenhang zu festgelegten Budgets pro Bereich (Kleidung, Essen/Verpflegung, Ausgang/Freizeit, Hygiene, Handyabbo) zu geben.

/31.08.18
Da ich das Programm schon vor Projektbeginn zu programmieren begonnen habe, läuft das Programm schon. Als erster Schritt wird nun das funktionsfähige Programm in die Struktur des objekt orientierten Programmierens gebracht. Bis jezt wurden 3/4 des Programms in drei Klassen übersetzt: 
Stock: Kümmert sich um die Funktionalität rund um das Budget.
Entry: Kümmert sich um neue Einträge bestehend aus: Summe, Grund/Verwendungszweck und Datum.
Cycle (Entry): Kümmert sich um den Kreislauf, damit mehrere Einträge in einem Programmdurchlauf verarbeitet werden können.
-->Die beiden Klassen Stock und Entry bilden je ein eigenes File und die Cycle-Klasse befindet sich als Erb-klasse in dem File der Entry-Klasse. Alle Klassen werden im Main-File vereint.

Zurzeit wurde nur die Stock-Klasse auf die Funktionalität überprüft, als weitere Schritte werden die beiden weiteren Klassen getestet und der letzte Teil ins oop. umconvertiert.

/07.09.18
Die Klassen Stock, Entry und Cycle wurden auf deren Funktionalität und mögliche Fehler überprüft und angepasst. Weiter entstand eine neue Klasse namens "Calculate", die zurzeit nur über die Funktion verfügt, die Summen der fünf Klassen zu einer Gesammtsumme pro Klasse zusammenzurechnen.

Der Code wurde weiter gekürzt und vereinfacht.

Derzeitiger Ablauf:
Neuer "Eintrag" bestehend aus "Summe", "Grund", "Datum" und "Klassifizierung" wird erstellt.

--->Ein dem Programm unbekannter Grund kann im Falle eines Schreibfehlers angepasst, oder als neuer Grund einer Klasse zugeordnet werden.

Die vier oben genannten Attribute eines "Eintrags" werden in seperaten Listen gespeichert und teilen sich die gleiche Gliednummer.

Mit dem Befehl "done" wird dem Programm vermittelt, dass keine weitere Einträge ausstehen. Bei Eingabe eines anderen Befehls kann und muss ein weiterer Eintrag erstellt werden.

Die Summen der gleichen Klassifizierung werden zusammengerechnet und eine positive oder negative Differenz mit dem "Stock" ermittelt.




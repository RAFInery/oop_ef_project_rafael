//Grundidee des Programms//
Das Programm soll es ermöglichen, alltägliche Ausgaben auf einfache Weise in einer Liste zusammenzufassen und dem Nutzer praktische Statistiken im Zusammenhang zu festgelegten Budgets pro Bereich (Kleidung, Essen/Verpflegung, Ausgang/Freizeit, Hygiene, Handyabbo) zu geben.

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

/17.09.18
Das Programm ist nun in seinen Grundfunktionen fertiggestellt. Die einzelnen Py-Files sins neuerdings als "Module" benannt (z.B. "Entry_Module.py"). Neu hinzu kommt die Funktion, den Eintrag über unbestimmte Zeit hinweg fertigzustellen. Dies wird durch eine "dictionnary" ermögicht, die die Summe, Stock und den Monat umfasst und in einer Pickle-Datei abgespeichert ist. 
Der Ablauf ist wie folgt:

Das Pickel-File wird geladen. Falls kein Monat angegeben ist, fordert das Programm den Benutzer auf, seinen Monat der folgenden Einträge zu spezifizieren.

Im Falle eines neuen Monats, wird das Monatliche Budget zum bestehenden Stock hinzuaddiert. 

Der Benutzer entscheidet über seine Absichten: "new entry" oder "final calculations".

Bei "new entry" kann der Benutzer beliebig viele Einträge bestehend aus Summe, Grund und Datum tätigen.

Anschliessend wird dem Benutzer die Frage gestellt, ob das sein letzter Eintrag war oder ob noch weitere folgen.
Falls noch weitere folgen, werden die Daten in einer python-dictionary als pickel-fle gespeichert. Ansonsten schreitet das Programm zur Stuffe der abschliessenden Abrechnungen, zu welcher der Benutzer auch direkt über die Eingabe "final calculations" anfangs des Programms gelangt. Dies beeinhält die Addition der neuen und gespeicherten Summen und die Bilanz-Ausrechnung des Stocks. Diese Ergebnisse werden in einem einfachen Textfile dargestellt. Danach wird das pckel-fle wieder auf einen neuen Monat zurück gesetzt. Daher: stock = calculated stock, sum = None, month = None.


/31.10.18
Dem Programm wurde eine dynamische Speicherfunktion neuer "keys" hinzugefügt. Das Programm meldet einen unbekannten Grund sofort. Im Falle, das es sich dabe nicht um einen Schreibfehler handelt, ist es dem User möglich einen neuen key permanent hinzuzufügen. Neue keys/Gründe sind dem Programm demnach auch in anschliessenden Monatseinträgen bekannt. Bei einem allgälligen "reset" der Pickle-Datei gehen die hinzugefügten keys jedoch verloren, da die Gründe des "Speicher-Dictionary" angehängt ist. 


Bedienungshinweis (31.10.2018):

Mit dem FiPro können Ausgaben einfach verschriftlicht und eine Bilanz erstellt werden. Grundsätzlich stellt das Programm eine interne Bedienungshilfe bereit. Es folgen wenige wichtige Punkte, die jedoch weiter beachtet werden müssen, damit der Prozess nicht gestört wird.

Projektfile: 
Alle Datein die in Verbindung mit dem Programm stehen, müssen sich im gleichen Ordner befinden. Dies schliesst auch das pickle-file und die erstellen Blätter mit den Ausgabenauflistungen nicht aus.

Download:
Die Datei "FiPro_Rafael_Sollberger_2.0" kann als solche heruntergeladen und das Programm in "main" gestartet werden. Im Falle eines Fehlers, empfehle ich die einen "reset" anhand der "pickle_reset-Datei" durchzuführen.





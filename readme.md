

\## Pre-commit Automatisierung



\### Installation

Führe folgenden Befehl einmalig aus, um die pre-commit Hooks zu aktivieren:



pre-commit install



\### Benutzung



Bei jedem Commit wird der Code automatisch formatiert (mit black):

git add .

git commit -m "Deine Nachricht"



Bei jedem Push werden die Tests automatisch ausgeführt (mit pytest):

git push



Falls du einen Hook umgehen willst:

git commit --no-verify -m "Deine Nachricht"


**Запуск проекта**

Откройте терминал, или командную строку (если вы на Windows) в этой папке (где лежит файл _requirements.txt_ \- это
корень проекта, далее так и будем его называть).

В целях безопасноти создадим виртуальное окружение Python, для этого в консоле выполните: python -m venv venv

Эта команда создаст папочку: venv в котором будет лежать изолированный Python для нашего проекта.

Теперь слеудет активировать нашу новую оболочку, выполните в консоле: `venv\Scripts\activate.bat` (для windows)
и `source venv/bin/activate` (для линукс, или мак).

В корне проекта найти файл: _requirements.txt_ в нём указаны все библиотеки для использования в проекте. Для их
установки выполните:

`pip install -r requirements.txt`

**Убедитесь, что все библиотеки успешно установлены.**

Теперь поднимим back - сервис, для этого в консоле пропишите:

`flask run --debug -h 127.0.0.1 -p 8080`

Для остановки сервисов в каждой консоле зажмите клавиши: **Ctrl+C**

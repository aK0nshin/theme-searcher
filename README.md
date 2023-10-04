# Theme searcher

## Установка
```
git clone git@github.com:aK0nshin/theme-searcher.git
cd theme-searcher
poetry install
```

## Запуск API
```
uvicorn theme_searcher.main:app
```

## Запросы
### Поиск темы по запросу
```
curl --request POST \
  --url http://127.0.0.1:8000/theme/search \
  --header 'Content-Type: application/json' \
  --data '{
	"query": "тайская кухня"
}'
```

### Добавление темы в хранилище
```
curl --request POST \
  --url http://127.0.0.1:8000/theme \
  --header 'Content-Type: application/json' \
  --data '{
	"theme": "новости",
	"phrases": [
		"деревья на Садовом кольце",
		"добрый автобус",
		"выставка IT-технологий"
	]
}'
```
```
curl --request POST \
  --url http://127.0.0.1:8000/theme \
  --header 'Content-Type: application/json' \
  --data '{
	"theme": "кухня",
	"phrases": [
		"рецепт борща",
		"яблочный пирог",
		"тайская кухня"
	]
}'
```
```
curl --request POST \
  --url http://127.0.0.1:8000/theme \
  --header 'Content-Type: application/json' \
  --data '{
	"theme": "товары",
	"phrases": [
		"Дети капитана Гранта",
		"зимние шины",
		"Тайская кухня"
	]
}'
```
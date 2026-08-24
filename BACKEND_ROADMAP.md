# Backend Roadmap → Яндекс-стажировка

> ⚠️ **Это НЕ активный план до сентября.** Активный план — `PREP_PLAN.md` (алгоритмы) +
> `DAILY_PLAN.md` (по дням). Этот файл — **глубокий справочник на поздние секции собеса**
> (язык / архитектура / про опыт / системный дизайн). Разбирать ПОСЛЕ того, как поедут алгоритмы,
> и точечно — под конкретную секцию. 12-недельный объём в текущий график (оффер к концу октября) целиком не влезет.
> Раздел про **Go** релевантен Яндексу, Ozon и Wildberries; для Т-Банк/Авито/МТС (Python) — опционально.
> Список компаний и приоритеты — `docs/companies/shortlist.md`.

Концентрированный план: Python/FastAPI глубоко + Go базово. Привязан к реальному коду в `~/repos/bes` — изучай теорию и сразу смотри как это реализовано в боевом проекте.

> Тренировка — в `~/repos/dojo/`. Каждая тема имеет мини-задачу. Делай в отдельной подпапке (`dojo/learning/<тема>/`), коммить.

---

## 0. Mental model: зачем разделять слои?

В `bes` слои такие (одна и та же иерархия `<type>/<calculation>` повторяется в каждом):

| Слой | Куда кладём | Что делает |
|---|---|---|
| `models/` | SQLAlchemy ORM-классы | Структура таблиц БД. Ничего не знает про HTTP/JSON. |
| `schemas/` | Pydantic-модели | Валидация входа/выхода API. Граница "внешний мир ↔ приложение". |
| `repositories/` | Функции/классы поверх ORM | CRUD-операции. Прячут SQL за вызовами вроде `get_user_by_email()`. |
| `services/` | Бизнес-логика | Оркестрирует repositories, считает, шлёт события. Не знает про FastAPI. |
| `api/` | FastAPI роутеры | HTTP-эндпойнты. Тонкие: валидация → service → response. |
| `core/` | config, DB, security | Инфраструктура, общая для всех модулей. |

**Зачем разделять:**
1. **Тестируемость** — service можно тестировать без HTTP-клиента, repository — без сети.
2. **Замена слоя** — поменять Postgres на Mongo = переписать только `repositories/`.
3. **Тонкие роутеры** — в `api/` нет if-else по бизнес-логике; вся сложность в `services/`.
4. **Pydantic ≠ ORM** — никогда не возвращай ORM-модель в API напрямую: утечки полей (например, `password_hash`).

**Антипаттерн (НЕ делай):** засовывать SQL прямо в роутер, или вызывать `bcrypt` из роутера. Если в `api/` появилась бизнес-логика — выноси в `services/`.

Смотри: `bes/backend/app/api/slab/static.py` → `bes/backend/app/services/slab/static.py` — роутер делает 5 строк, всё мясо в сервисе.

---

## 1. Python core (1-2 недели)

Что важно для Яндекса:
- typing (`TypeVar`, `Protocol`, `Generic`, `Literal`, `TypedDict`) — у них type-hints обязательны.
- async/await: event loop, `asyncio.gather`, `asyncio.create_task`, отмена тасков.
- Контекстные менеджеры (`contextlib.asynccontextmanager`).
- Dataclasses vs Pydantic vs attrs — когда что.
- GIL: что блокирует, что нет (numpy/IO освобождают, чистый python — нет). В `bes` это явно: `run_in_executor` в `api/slab/static.py`.

**Задачка в dojo:** напиши async-функцию, которая параллельно запрашивает 3 URL через `httpx.AsyncClient` и возвращает результат самого быстрого. С таймаутом и отменой остальных.

---

## 2. SQL и базы данных (2 недели — критично)

На собесах Яндекс задаёт SQL глубоко.

**Темы:**
- JOIN'ы (INNER/LEFT/RIGHT/FULL/CROSS) — рисуй диаграммы Венна пока не уляжется.
- Агрегации + `GROUP BY` + `HAVING`.
- Window functions: `ROW_NUMBER`, `RANK`, `LAG/LEAD`, `SUM() OVER (PARTITION BY ...)` — спрашивают часто.
- CTE (`WITH ...`) и рекурсивные CTE.
- Индексы: B-tree, hash, partial, composite. Когда индекс НЕ используется (`LIKE '%foo%'`, функции от колонки).
- `EXPLAIN ANALYZE` — читай планы запросов.
- Транзакции, уровни изоляции (READ COMMITTED / REPEATABLE READ / SERIALIZABLE), что такое phantom read / non-repeatable read.
- Блокировки: `SELECT ... FOR UPDATE`, deadlock'и.
- N+1 проблема и как её ловить (в SQLAlchemy — `selectinload`, `joinedload`).

**ACID** и **CAP** — знать наизусть, объяснять словами.

**Задачка в dojo:** в `dojo/learning/sql/` подними локальный Postgres, создай схему "блог" (users, posts, comments, likes), залей 100k строк через генератор, и реши 20 задач — топ-10 пользователей по числу лайков на пост за последний месяц, окно "пользователи, у которых растёт активность" и т.д. Гоняй `EXPLAIN ANALYZE` на каждую.

Ресурс: pgexercises.com, sql-ex.ru.

---

## 3. SQLAlchemy + Alembic (1 неделя)

В `bes` используется SQLAlchemy 2.x (новый стиль `Mapped[]`).

- Декларативные модели (`bes/backend/app/models/user.py`).
- Relationships: `relationship()`, `back_populates`, lazy strategies (`select`, `selectin`, `joined`).
- Сессии: scoped vs request-scoped. Почему "одна сессия на запрос" — стандарт.
- Alembic: `autogenerate`, ручные миграции, downgrades. Что autogenerate НЕ ловит (переименования колонок, изменения CHECK constraints).

**Задачка в dojo:** склонируй "блог" из задачи 2 в SQLAlchemy-модели, напиши репозитории, потом миграцию которая добавляет soft-delete (`deleted_at`).

---

## 4. FastAPI углублённо (1 неделя)

Прочитай `bes/backend/app/main.py` целиком — там в 50 строк есть: lifespan, CORS, middleware, exception handlers, роуты.

- Dependency Injection (`Depends`) — основа FastAPI. Смотри `bes/backend/app/api/deps.py`.
- Pydantic v2: validators, `model_config`, `Field(..., examples=...)`.
- Background tasks vs очереди (background tasks подходят только для "send email and forget", не для долгих расчётов).
- SSE (Server-Sent Events) — в `bes/backend/app/api/slab/static.py` есть боевой пример с прогресс-стримингом.
- WebSocket — базово.
- Загрузка файлов: `UploadFile`, стриминг больших файлов.

**Задачка в dojo:** на блоге сделай REST + JWT auth (access + refresh токены) с правильным DI.

---

## 5. Auth и безопасность (3-5 дней)

- JWT: что внутри (header.payload.signature), почему НЕ хранить sensitive данные.
- Access vs refresh token, ротация refresh.
- Хеширование паролей: bcrypt/argon2 (не sha256!). В `bes` — bcrypt через `passlib`.
- OWASP Top 10: SQL injection, XSS, CSRF, IDOR, SSRF — что это и как защититься.
- Rate limiting (slowapi для FastAPI).
- CORS — что на самом деле проверяет браузер.

---

## 6. Тесты (1 неделя)

- pytest: фикстуры, параметризация, `conftest.py`, маркеры.
- Изоляция тестов БД: transaction rollback per test vs truncate (в `bes` — truncate, см. `CLAUDE.md`).
- TestClient FastAPI, httpx ASGITransport для async.
- Моки vs стабы vs фейки. Когда мокать БД (почти никогда), когда внешние API (всегда).
- Coverage — стремись к 80%+, но не дрочи на 100%.

**Задачка в dojo:** к блогу напиши 30 тестов: unit (services) + integration (через TestClient + реальный Postgres).

---

## 7. Очереди и кеши (1 неделя)

В Яндексе много очередей.

- Redis: типы данных (string/hash/list/set/zset/stream), TTL, pub/sub.
- Кеш-стратегии: cache-aside, write-through, write-behind. Инвалидация (две главные проблемы программирования: инвалидация кеша и именование).
- Celery / RQ / arq — task queue для Python. Разница между task queue и message broker.
- Идемпотентность задач — must.

**Задачка в dojo:** к блогу прикрути Redis-кеш для топ-10 постов с инвалидацией при новом лайке, и Celery-задачу "отправить дайджест на email".

---

## 8. HTTP, сети, протоколы (3-5 дней)

- HTTP/1.1 vs HTTP/2 vs HTTP/3 — что изменилось, зачем.
- Методы, статус-коды (особенно отличия 401/403, 422, 429).
- REST vs gRPC vs GraphQL — когда что выбирать.
- TLS handshake крупными мазками.
- DNS, как браузер находит сервер.

---

## 9. Архитектура и паттерны (1 неделя)

- SOLID — не зубрить, но уметь объяснять примерами.
- DI как принцип (не библиотека) — почему в `bes/api/deps.py` функции, а не глобальные синглтоны.
- Repository pattern, Service layer, Unit of Work.
- DDD lite: entities, value objects, aggregates — на уровне понимания.
- Чистая архитектура (Hexagonal/Onion) — почему `packages/` в `bes` не знает про FastAPI.
- Микросервисы vs монолит — НЕ ведись на хайп, на собесе говори "depends".

Книги: "Architecture Patterns with Python" (Percival/Gregory) — must read для FastAPI-разработчика.

---

## 10. Docker + деплой (3-5 дней)

- Dockerfile: multi-stage build, минимальные образы, не root user.
- docker-compose для локалки.
- Базовое знание Kubernetes (Pod, Service, Deployment, ConfigMap, Secret) — на уровне "понимаю что это".
- CI/CD: GitHub Actions, runner, secrets.
- Логи и метрики: structured logging (JSON), Prometheus метрики базово.

---

## 11. Go (3-4 недели — параллельно с Python)

Яндекс пишет много бэка на Go. Не нужно стать сениором, нужно уметь читать и писать простой сервис.

**Минимум:**
- Синтаксис, типы, структуры, интерфейсы (как они отличаются от Python ABC — implicit satisfaction).
- Горутины + каналы + `select` — главная фишка.
- Контексты (`context.Context`) — везде.
- `net/http` стандартный, потом `chi` или `fiber`.
- `database/sql` + `sqlx` или `pgx`.
- Тесты (`testing`, `testify`).
- Модули, go.mod, версионирование.

**Задачка в dojo:** перепиши блог-сервис из задач выше на Go (хотя бы CRUD без авторизации). Поймёшь разницу между Python "магией" и Go "явностью".

Ресурсы: "Tour of Go", "Effective Go", книжка "Learning Go" Bodner.

---

## 12. Soft / алгоритмы для собеса

У тебя уже есть `dojo/algorithms/` и `dojo/coderun/` — продолжай. Для Яндекса:
- Массивы / two pointers / sliding window.
- Хеш-таблицы.
- Деревья (BFS/DFS), графы (Dijkstra, топосорт).
- Динамика — хотя бы 20 задач.
- Сложность по времени и памяти — словами, не зазубренно.

Площадки: LeetCode, Codeforces, contest.yandex.ru (там есть тренировочные стажёрские задачи).

---

## 13. Чек-лист "готов к собесу"

- [ ] Могу за 5 минут объяснить разницу schemas/models/repositories/services
- [ ] Напишу SQL с window function без подсказок
- [ ] Объясню что такое N+1 и как лечить в SQLAlchemy
- [ ] Расскажу про уровни изоляции и приведу пример phantom read
- [ ] Покажу как сделать JWT auth с refresh-токенами
- [ ] Объясню почему нельзя возвращать ORM-модель в API
- [ ] Напишу простой HTTP-сервис на Go за 30 минут
- [ ] Решу LeetCode medium за 30-40 минут
- [ ] Объясню что такое event loop и почему `time.sleep` в async-коде — ошибка

---

## Порядок изучения (рекомендация)

```
Неделя 1-2:   Python core + чтение bes построчно
Неделя 3-4:   SQL глубоко (без ORM!)
Неделя 5:     SQLAlchemy + Alembic, переписать "блог"
Неделя 6:     FastAPI углублённо + auth
Неделя 7:     Тесты + Redis + Celery
Неделя 8-10:  Go параллельно с повторением Python
Неделя 11:    Docker, CI/CD, чтение чужих архитектур
Неделя 12+:   Алгоритмы + mock-собесы
```

Не пытайся всё запомнить за раз. Работает связка: прочитал тему → нашёл в `bes` как сделано → сделал свою мини-версию в `dojo/learning/` → объяснил вслух (хоть стене).

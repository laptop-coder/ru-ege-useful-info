[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](https://github.com/laptop-coder/ru-ege-useful-info/blob/main/LICENSE) [![Latest](https://img.shields.io/github/v/release/laptop-coder/ru-ege-useful-info?style=flat-square&label=latest)](https://github.com/laptop-coder/ru-ege-useful-info/releases) [![Release](https://img.shields.io/github/actions/workflow/status/laptop-coder/ru-ege-useful-info/release.yaml?branch=main&style=flat-square&label=release)](https://github.com/laptop-coder/ru-ege-useful-info/actions/workflows/release.yaml)

Ежедневные посты с полезной информацией для подготовки к ЕГЭ по русскому языку

## Источники

| Раздел                                   | Ресурс                                                                                              |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Орфоэпия                                 | [ФИПИ](https://doc.fipi.ru/navigator-podgotovki/navigator-ege/2025/ru-1-fonetika.pdf)               |
| Паронимы и фразеологизмы                 | [ФИПИ](https://doc.fipi.ru/navigator-podgotovki/navigator-ege/2025/ru-2-leksika-i-frazeologija.pdf) |
| Непроверяемые безударные гласные в корне | [ФИПИ](https://doc.fipi.ru/navigator-podgotovki/navigator-ege/2025/ru-5-orfografija.pdf)            |

## Технологии

- **App:** Python (через VK API)
- **Deploy:** Docker, Docker Compose

## Начало работы
```bash
# Клонируйте репозиторий
git clone https://github.com/laptop-coder/ru-ege-useful-info.git
cd ./ru-ege-useful-info
# Настройте переменные окружения
cp .env.example .env
vi .env
# Первый запуск (deploy + CI/CD)
make first-run
```

## Доступные команды для `make`

| Команда     | Описание                                                                |
| ----------- | ----------------------------------------------------------------------- |
| `cron`      | Включить ежедневную публикацию постов и автоматические обновления ночью |
| `deploy`    | Запустить приложение                                                    |
| `first-run` | `deploy` + `cron`                                                       |
| `logs`      | Просмотреть логи                                                        |
| `down`      | Остановить приложение                                                   |
| `dev`       | Запустить приложение в режиме разработки                                |


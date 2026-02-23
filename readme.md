# 🚀 CI/CD Pipeline Demo: FastAPI + GitHub Actions + Railway

> Пет-проект для демонстрации навыков настройки автоматизированных процессов доставки кода (CI/CD).

## 📋 О проекте

Это простое REST API на **FastAPI**, которое демонстрирует полный цикл разработки:
- ✅ Написание кода и тестов
- ✅ Автоматическая проверка качества (CI)
- ✅ Автоматический деплой на продакшн (CD)

### 🔗 Ссылки
- **Live Demo**: [https://web-production-54910.up.railway.app/](https://...)
- **API Docs**: [https://web-production-54910.up.railway.app/docs](https://...)

## 🛠 Технологический стек

| Категория | Инструменты |
|-----------|-------------|
| **Language** | Python 3.11 |
| **Framework** | FastAPI, Uvicorn |
| **Testing** | Pytest, TestClient |
| **CI/CD** | GitHub Actions |
| **Deployment** | Railway (PaaS) |
| **Containerization** | Docker (опционально) |

## ⚙️ Архитектура CI/CD пайплайна

Пайплайн настроен в `.github/workflows/deploy.yml` и состоит из двух стадий:

### 1️⃣ Continuous Integration (CI)
Запускается при каждом `git push`:
```bash
1. Checkout кода
2. Установка зависимостей (pip install)
3. Запуск линтера (flake8/black - опционально)
4. Запуск тестов (pytest)
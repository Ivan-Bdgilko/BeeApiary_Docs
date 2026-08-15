# Документація BeeApiary

Вихідна документація BeeApiary для публікації через MkDocs і GitHub Pages.

## Локальний запуск

```powershell
python -m pip install -r requirements.txt
mkdocs serve
```

Український контент зберігається в `docs/uk/`. Вхідні DOCX є локальними матеріалами міграції та не відстежуються Git.

## Перевірка

```powershell
mkdocs build --strict
```

## GitHub Pages

Перед першим розгортанням відкрийте **Settings → Pages** у GitHub і в секції **Build and deployment** виберіть **Source: GitHub Actions**. Після цього процес `.github/workflows/docs.yml` публікує сайт із `main`.

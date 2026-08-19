# Документація BeeApiary

[User manual](https://ivan-bdgilko.github.io/BeeApiary_Docs/)
[Документація BeeApiary](https://ivan-bdgilko.github.io/BeeApiary_Docs/)

Вихідна документація BeeApiary для публікації через MkDocs і GitHub Pages.

## Локальний запуск

```powershell
python -m pip install -r requirements.txt
mkdocs serve
```

Український контент у `docs/uk/` є основним джерелом істини. Англійські й німецькі сторінки в `docs/en/` та `docs/de/` формуються як переклади відповідних українських сторінок.

Українська версія публікується в корені сайту, англійська — у `/en/`, німецька — у `/de/`. Якщо перекладу сторінки ще немає, відповідна мовна версія тимчасово показує український оригінал із попередженням.

Вхідні DOCX є локальними матеріалами міграції та не відстежуються Git.

## Перевірка

```powershell
mkdocs build --strict
```

## GitHub Pages

Перед першим розгортанням відкрийте **Settings → Pages** у GitHub і в секції **Build and deployment** виберіть **Source: GitHub Actions**. Після цього процес `.github/workflows/docs.yml` публікує сайт із `main`.

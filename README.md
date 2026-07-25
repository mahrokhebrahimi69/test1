# Political Comment Dataset

کالکشن کامل کامنت‌های فارسی سفارش غذا برای تست تشخیص کلاس **سیاسی**.

## دانلود

- **`political_comment_dataset.zip`** — همه فایل‌ها یکجا
- یا مستقیم از پوشه `data/`

## شروع سریع

```bash
# نسخه کامل (با تگ و توضیح)
data/political_comment_dataset.json

# آرایه تخت برای ارزیابی
data/political_comment_dataset.flat.json

# فقط comment برای Runner
data/political_comment_dataset.comments.json
```

بازتولید:

```bash
python3 scripts/build_political_dataset.py
```

## Postman (دیباگ دستی)

- Data File: `data/political_comment_dataset.flat.json`
- Collection: `postman/preferred/Classification_QA.postman_collection.json`
- راهنما: [`postman/HOW_TO_RUN.md`](postman/HOW_TO_RUN.md)

## ترجیح ذخیره سوابق: Newman + JSONL

```bash
npm install
npm run qa:fresh
```

خروجی:
- `results/runs/<runId>/results.jsonl` — هر کیس + confidence
- `results/runs/<runId>/summary.json` — آمار FALSE_ACCEPT / FALSE_REJECT
- `results/runs/index.json` — فهرست runها

چرا این‌طور: [`postman/preferred/WHY_THIS_WAY.md`](postman/preferred/WHY_THIS_WAY.md)

جزئیات خوشه‌ها و اسکیم برچسب: [`data/README.md`](data/README.md)

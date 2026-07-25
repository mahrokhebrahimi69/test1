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

جزئیات خوشه‌ها و اسکیم برچسب: [`data/README.md`](data/README.md)

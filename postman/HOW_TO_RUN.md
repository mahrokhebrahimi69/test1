# اجرای دیتاست در Postman

## ۱) فایل داده درست

در Collection Runner این فایل را انتخاب کن:

```
data/political_comment_dataset.flat.json
```

نه `comments.json` — چون `expected_label` و `expected_reason` ندارد.

## ۲) اسکریپت‌ها

| محل در Request | فایل |
|----------------|------|
| Pre-request Script | `postman/Pre-request_reset_report.js` |
| Tests | `postman/Tests_classification_report.js` |

Body نمونه:

```json
{
  "comment": "{{comment}}"
}
```

## ۳) Run

1. Collection → **Run**
2. Select File → `political_comment_dataset.flat.json`
3. Delay حدود `200ms`
4. Run

## ۴) گرفتن خروجی

بعد از اتمام ران:

`Collection → Variables`

| Variable | محتوا |
|----------|--------|
| `classification_report` | همه کیس‌ها + confidence |
| `classification_failures` | فقط خطاها + confidence |
| `classification_summary` | خلاصه آمار |

یا از Console همان آبجکت summary را کپی کن.

### معنی status

| status | معنی |
|--------|------|
| `PASS` | label و reason درست |
| `FALSE_ACCEPT` | نباید می‌پذیرفت (`disapproval` → `approval`) |
| `FALSE_REJECT` | نباید رد می‌کرد (`approval` → `disapproval`) |
| `LABEL_MISMATCH` | جابه‌جایی دیگر (مثل `unknown`) |
| `REASON_MISMATCH` | label درست، reason غلط (مثلاً سیاسی را نگرفت) |

هر آیتم شامل `confidence` است.

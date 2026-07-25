# ترجیح ذخیره سوابق اجرا

## هدف
- هر کیس با `confidence` ذخیره شود
- `FALSE_ACCEPT` (نباید می‌پذیرفت) و `FALSE_REJECT` (نباید رد می‌کرد) جدا باشد
- تاریخچه اجراها قابل مقایسه بماند

## ترجیح من

| لایه | ابزار | چه چیزی ذخیره شود |
|------|--------|-------------------|
| دیباگ دستی / سریع | Postman GUI | فقط **run جاری** در Collection Variable |
| سابقه واقعی QA | Newman + فایل روی دیسک | **JSONL append** برای هر کیس |

### چرا Collection Variable را برای تاریخچه نمی‌خواهم؟
- سقف حجم دارد
- بین سیستم‌ها/افراد پایدار نیست
- Resume و diff سخت است
- برای ۳۸۶ کیس الان جا می‌شود، برای چند هزار کیس یا چند run متوالی نه

### ساختار پیشنهادی دیسک

```text
results/runs/
  index.json                         # فهرست همه runها
  checkpoint.json                    # برای Resume
  2026-07-25T11-40-00-000Z/
    results.jsonl                    # یک خط = یک کیس + confidence
    summary.json                     # آمار + failures فشرده
    newman-raw.json                  # خروجی خام Newman
    meta.json
```

هر خط `results.jsonl` شبیه:

```json
{
  "id": 1,
  "comment": "...",
  "expected_label": "disapproval",
  "actual_label": "approval",
  "expected_reason": "سياسي",
  "actual_reason": null,
  "confidence": 0.91,
  "status": "FALSE_ACCEPT",
  "mismatch_type": "should_reject_but_approved"
}
```

## اجرای پیشنهادی

```bash
npm install
npm run qa              # ادامه از checkpoint
npm run qa:fresh        # run جدید از صفر
```

خروجی مهم:
- `results/runs/<runId>/results.jsonl`
- `results/runs/<runId>/summary.json`
- `results/runs/index.json`

# Persian Food Comment — Political Classification Dataset

کالکشن کامل کامنت‌های فارسی برای تست/آموزش تشخیص **محتوای سیاسی** در نظرات سفارش غذا.

## فایل‌ها

| فایل | کاربرد |
|------|--------|
| `political_comment_dataset.json` | نسخه کامل با متادیتا، تگ، توضیح |
| `political_comment_dataset.flat.json` | آرایه تخت برای ارزیابی مدل |
| `political_comment_dataset.comments.json` | فقط `comment` برای Newman/Postman Runner |
| `political_comment_dataset.csv` | CSV با BOM برای Excel |

دانلود یکجا: `../political_comment_dataset.zip`

## اسکیم برچسب

- **labels:** `approval` | `disapproval` | `unknown`
- **political reason:** `سياسي` (با ی عربی، مطابق اسکیم سیستم)
- **سایر reasonها برای تفکیک کلاس:**
  - `انتقاد_و_پیشنهاد`
  - `موارد_بهداشتی`
  - `برخورد_نامناسب_پیک`
  - `استفاده_از_کلمات_نامناسب`
  - `null` برای approval/unknown

## اولویت Override

اگر کامنت همزمان تحسین غذا و محتوای سیاسی داشته باشد:

`expected_label = disapproval` و `expected_reason = سياسي`

## خوشه‌ها

| category | هدف |
|----------|-----|
| `political` | سیاسی مستقیم، اقتصادی-سیاسی، شعار، لقب‌دهی |
| `political_mixed` | غذا + سیاسی (تست اولویت Rule) |
| `non_political_negative` | منفی غیرسیاسی برای تفکیک کلاس |
| `approval` | کنترل مثبت |
| `boundary` | نقاط مرزی قیمت/استعاره/false-friend/مبهم |
| `adversarial` | دور زدن مدل: فاصله‌گذاری، پینگلیش، تزریق پرامپت، ایموجی، تمسخر |

## بازتولید

```bash
python3 scripts/build_political_dataset.py
```

# Bug Report Template — قالب ثبت باگ QA

> این صفحه را به‌عنوان **Template** نگه دار.  
> برای هر باگ جدید: `...` روی این صفحه → **Copy** → عنوان باگ را بگذار → جدول را پر کن.

---

## نحوه استفاده در Confluence

1. این صفحه را بساز زیر:
   ```text
   Tapsi Food QA Onboarding Knowledge Base
   └── QA Playbook / Templates
       └── Bug Report Template
   ```
2. در Space Settings (اگر Template رسمی خواستی):  
   Space settings → Templates → Create → همین محتوا را پیست کن و نام بگذار: `QA Bug Report`
3. هر بار باگ جدید: از Template بساز یا این صفحه را Copy کن.

---

## قالب آماده کپی (جدول خالی)

| فیلد | مقدار |
| --- | --- |
| **Title** | `[Squad][Env] خلاصه کوتاه مشکل` |
| **محیط (Environment)** | staging / production / dev |
| **Component** | Front-end / Back-end / App / Both |
| **اسکواد Owner** | AI / CHEF / COMP / DATA / DEL / FIN / MM / OMS405 / PLAT / PROMC / SD / TACH / VEN |
| **سرویس مرتبط** | مثلاً Icarus / OMS / Iris / … |
| **سیستم‌عامل، مرورگر/اپ، دستگاه** | مثلاً macOS + Google Chrome 126 / Android 14 |
| **پیش‌نیازها (Preconditions)** |  |
| **مراحل بازتولید (Steps to Reproduce)** | ۱- … ۲- … ۳- … |
| **نتیجه مورد انتظار (Expected Result)** |  |
| **نتیجه واقعی (Actual Result)** |  |
| **تعداد دفعات وقوع (Reproducibility)** | همیشه / گاهی / یک‌بار / نیاز به شرایط خاص |
| **شدت (Severity)** | Blocker / High / Medium / Low |
| **اولویت (Priority)** | P0 / P1 / P2 / P3 |
| **پیوست‌ها (Attachments)** | اسکرین / ویدیو / لاگ / RequestId / TraceId |
| **Curl خطا (در صورت API)** |  |
| **توضیحات تکمیلی (Additional Notes)** |  |
| **لینک Jira** |  |

---

## نمونه پرشده (برای آموزش)

| فیلد | مقدار |
| --- | --- |
| **Title** | `[FIN][staging] خطای upstream error در Thank You Page بعد از درگاه اوزون` |
| **محیط (Environment)** | staging |
| **Component** | Front-end / Back-end |
| **اسکواد Owner** | FIN (+ بررسی OMS/SD در صورت نیاز) |
| **سرویس مرتبط** | Payment / Checkout |
| **سیستم‌عامل، مرورگر/اپ، دستگاه** | macOS — Google Chrome |
| **پیش‌نیازها (Preconditions)** | کاربر در مسیر `https://accounts.tapsi.ir/` لاگین باشد |
| **مراحل بازتولید (Steps to Reproduce)** | ۱- طی کردن فانل فروش تا صفحه چک‌اوت ۲- انتخاب روش پرداخت اوزون ۳- ورود به درگاه اوزون ۴- مشاهده خطا در Thank You Page |
| **نتیجه مورد انتظار (Expected Result)** | در فرم Thank You Page هیچ خطایی در ریسپانس مشاهده نشود و سفارش/پرداخت وضعیت صحیح نشان دهد |
| **نتیجه واقعی (Actual Result)** | خطای `upstream error` در صفحه Thank You Page نمایش داده می‌شود |
| **تعداد دفعات وقوع (Reproducibility)** | همیشه |
| **شدت (Severity)** | High |
| **اولویت (Priority)** | P1 |
| **پیوست‌ها (Attachments)** | تصاویر/ویدیو در بدنه باگ اتچ شود |
| **Curl خطا (در صورت API)** | - |
| **توضیحات تکمیلی (Additional Notes)** | - |
| **لینک Jira** |  |

---

## چک‌لیست قبل از ثبت باگ

| # | چک | Done؟ |
| --- | --- | --- |
| 1 | محیط دقیق نوشته شده (staging/production) |  |
| 2 | Steps از ۱ شماره‌گذاری شده و قابل بازتولید است |  |
| 3 | Expected و Actual از هم جدا هستند |  |
| 4 | اسکواد/Component مشخص است |  |
| 5 | اسکرین یا ویدیو یا Trace/RequestId پیوست شده |  |
| 6 | اگر API است، Curl یا Response خطا آمده |  |
| 7 | داده تست (یوزر/سفارش/کد تخفیف) ذکر شده |  |

---

## قانون کوتاه نوشتن Title

```text
[کد اسکواد][محیط] خلاصه مشکل در حداکثر یک خط
```

مثال‌ها:
- `[FIN][staging] upstream error در Thank You Page با پرداخت اوزون`
- `[SD][prod] کروسل هوم در شهر مشهد خالی است`
- `[Icarus][staging] OTP منقضی نمی‌شود بعد از TTL`

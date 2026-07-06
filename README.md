# Comment Moderation QA

پکیج کامل تست API مدیریت کامنت (`POST /moderate`) با **Postman Collection Runner** و **Newman**.

**Base URL:** `https://comment.foodstg.com`

---

## ساختار پروژه

```
comment-moderation-qa/
├── collections/
│   └── Comment_Moderation_QA.postman_collection.json
├── data/
│   ├── dataset.json           ← ورودی Runner (فقط comment)
│   ├── dataset.csv            ← همان داده به فرمت CSV
│   └── dataset-catalog.json   ← مرجع QA (خوشه + توضیح)
├── results/
│   └── .gitkeep               ← خروجی‌ها اینجا ساخته می‌شوند
├── scripts/
│   └── newman-runner.js       ← اجرای Production با Resume
├── package.json
├── package-lock.json
└── README.md
```

---

## خوشه‌بندی دیتاست (۳۷ نمونه)

| خوشه | تعداد | هدف |
|------|-------|-----|
| `positive` | ۵ | تحسین فارسی/انگلیسی |
| `complaint` | ۵ | شکایت مشروع (سرد، تاخیر، بسته‌بندی) |
| `toxic` | ۴ | توهین و فحش |
| `spam` | ۵ | نویز، ایموجی، متن بی‌معنا |
| `food_safety` | ۳ | آلودگی و بهداشت |
| `sensitive` | ۲ | حساسیت مذهبی |
| `boundary` | ۶ | کوتاه/بلند/دوزبانه/فاصله/عدد |
| `neutral` | ۲ | گزارش خنثی |
| `policy` | ۲ | رقیب، PII |
| `ambiguous` | ۳ | مبهم و تردید |

جزئیات هر رکورد در `data/dataset-catalog.json`.

---

## ۱. Postman Collection Runner

### Import

فایل `collections/Comment_Moderation_QA.postman_collection.json` را در Postman import کنید.

### ساختار JSON داده

```json
[
  { "comment": "غذا عالی بود" },
  { "comment": "داخل غذا مو بود" }
]
```

### ساختار CSV داده

```csv
comment
"غذا عالی بود"
"داخل غذا مو بود"
```

### Body درخواست

```json
{
  "comment": "{{comment}}"
}
```

### Pre-request Script

فقط در iteration اول مقداردهی اولیه `results` انجام می‌شود. بین Runهای مختلف پاک نمی‌شود.

### Test Script

- خواندن `comment` از Data File
- ذخیره `status` و `response` (JSON یا Text)
- جمع‌آوری در Collection Variable به نام `results`
- در صورت خطای شبکه، اسکریپت crash نمی‌کند

### اجرا

1. Collection → **Run**
2. **Select File:** `data/dataset.json`
3. **Iterations:** Auto
4. **Delay:** 200ms
5. **Run**

### مشاهده خروجی

`Collection → Variables → results` → Copy

---

## ۲. Newman (Production)

### نصب

```bash
npm install
```

### دستورات

```bash
npm run run          # ادامه از checkpoint
npm run run:fresh    # از اول، بدون پاک کردن نتایج قبلی
npm run run:clear    # پاک کردن نتایج + شروع از اول
```

### گزینه‌ها

```bash
node scripts/newman-runner.js --data data/dataset.json --delay 300
node scripts/newman-runner.js --timeout 60000
node scripts/newman-runner.js --help
```

### خروجی

**`results/results.jsonl`** — هر خط یک JSON:

```json
{"runId":"...","index":0,"comment":"غذا خیلی خوشمزه بود","status":200,"response":{...},"error":null,"durationMs":245,"timestamp":"..."}
```

**`results/checkpoint.json`** — وضعیت Resume

### تبدیل JSONL به آرایه

```bash
node -e "const fs=require('fs');const f='results/results.jsonl';if(!fs.existsSync(f))process.exit(1);const arr=fs.readFileSync(f,'utf8').trim().split('\n').filter(Boolean).map(JSON.parse);fs.writeFileSync('results/results-array.json',JSON.stringify(arr,null,2));console.log('saved',arr.length,'records');"
```

---

## ۳. Resume

```
Run 1: رکورد 0-4999 → checkpoint ذخیره
قطع (Ctrl+C)
Run 2: از 5000 ادامه → نتایج قبلی در jsonl باقی است
```

---

## ۴. محدودیت Collection Runner

| مشکل | توضیح |
|------|--------|
| RAM | همه نتایج در حافظه |
| اندازه Variable | ~۵MB عملی |
| Resume | ندارد |
| دیتاست بزرگ | ۵۰k+ مناسب نیست |

**برای ۱۰۰k تا ۱M رکورد از Newman + jsonl استفاده کنید.**

---

## ۵. بهترین محل نگه‌داری نتایج

| محل | کاربرد |
|-----|--------|
| `results/results.jsonl` | خروجی اصلی (append) |
| `results/checkpoint.json` | Resume |
| `results/archive/` | آرشیو روزانه (اختیاری) |

---

## ۶. Authentication

فعلاً API بدون Authentication است. در صورت نیاز در Collection → Authorization تنظیم کنید.

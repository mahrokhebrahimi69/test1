# بکاپ سوابق چت Cloud Agents

تاریخ خروجی: `2026-08-02T05:01:47Z`

- حساب: QA Cursor ACC (`qa-tfood@tapsifood.app`)
- ریپو: `github.com/mahrokhebrahimi69/test1`
- تعداد ایجنت‌ها: **12**

هر پوشه `bc-...` شامل:
- `transcript.json` — متن کامل گفتگو
- `events.json` — رویدادهای داشبورد
- `diff-metadata.json` — وضعیت PR/تغییرات
- `environment-info.json` — اطلاعات محیط

## فهرست چت‌ها

| نام | وضعیت | Archived | مدل | تاریخ ایجاد (UTC) | bcId |
|---|---|---|---|---|---|
| Cursor chat delete guide | IDLE | no | `None` | 2026-08-02T05:00:41 | `bc-6a54a0b6-55af-54ad-baf9-f0f6cd0e8229` |
| بکاپ و حذف سوابق چت | RUNNING | no | `auto-smart` | 2026-08-02T05:00:23 | `bc-c6224a15-ac68-4eeb-8d95-b0ff9a16fc1f` |
| Empty task instruction | IDLE | no | `auto-smart` | 2026-08-01T14:14:49 | `bc-473a31c7-2463-40d7-aa77-2a82e5d05a09` |
| دسترسی کاربر جدید جیرا | IDLE | no | `auto-smart` | 2026-08-01T08:18:53 | `bc-0a09ad1d-563e-4562-b61d-1d3645665c4c` |
| Empty task instruction | IDLE | no | `auto-smart` | 2026-07-28T10:52:12 | `bc-6f6ee186-a47a-4289-b9b3-f9596ea1943f` |
| دیتاست کامنت‌های جامع | IDLE | no | `auto-smart` | 2026-07-25T11:28:56 | `bc-9d9fd971-b3cf-435a-ba5b-b97ef90ec0fd` |
| چک لیست تست فود دلیوری | IDLE | no | `cursor-grok-4.5-high-fast` | 2026-07-14T07:32:57 | `bc-7c1b8bad-1db4-46dc-8fa0-4f5fd503bfef` |
| چک لیست تست فود دلیوری | IDLE | no | `cursor-grok-4.5-high-fast` | 2026-07-14T07:31:37 | `bc-dcd1c07d-c5d3-4880-b04c-8484e78c6bcf` |
| شماره مرجع کال‌بک پرداخت | IDLE | no | `grok-4.5-fast-xhigh` | 2026-07-13T13:15:40 | `bc-1c9606c7-2da2-4432-aef9-bb232a845727` |
| سوالات چالش‌برانگیز رزومه | IDLE | no | `cursor-grok-4.5-high-fast` | 2026-07-13T10:38:59 | `bc-295aef29-caf7-468a-8826-5185ebd82f8b` |
| نقشه راه مهندس نرم‌افزار | IDLE | yes | `composer-2.5` | 2026-07-06T08:28:45 | `bc-8fb1eabf-3f80-494e-99ce-13a494d14029` |
| پیکربندی داده‌محور API | IDLE | no | `composer-2.5` | 2026-07-06T07:00:01 | `bc-3eed5127-4f83-4584-b753-2f97d9fed70a` |

## لینک‌ها

- [Cursor chat delete guide](https://cursor.com/agents/bc-6a54a0b6-55af-54ad-baf9-f0f6cd0e8229)
- [بکاپ و حذف سوابق چت](https://cursor.com/agents/bc-c6224a15-ac68-4eeb-8d95-b0ff9a16fc1f)
- [Empty task instruction](https://cursor.com/agents/bc-473a31c7-2463-40d7-aa77-2a82e5d05a09)
- [دسترسی کاربر جدید جیرا](https://cursor.com/agents/bc-0a09ad1d-563e-4562-b61d-1d3645665c4c)
- [Empty task instruction](https://cursor.com/agents/bc-6f6ee186-a47a-4289-b9b3-f9596ea1943f)
- [دیتاست کامنت‌های جامع](https://cursor.com/agents/bc-9d9fd971-b3cf-435a-ba5b-b97ef90ec0fd)
- [چک لیست تست فود دلیوری](https://cursor.com/agents/bc-7c1b8bad-1db4-46dc-8fa0-4f5fd503bfef)
- [چک لیست تست فود دلیوری](https://cursor.com/agents/bc-dcd1c07d-c5d3-4880-b04c-8484e78c6bcf)
- [شماره مرجع کال‌بک پرداخت](https://cursor.com/agents/bc-1c9606c7-2da2-4432-aef9-bb232a845727)
- [سوالات چالش‌برانگیز رزومه](https://cursor.com/agents/bc-295aef29-caf7-468a-8826-5185ebd82f8b)
- [نقشه راه مهندس نرم‌افزار](https://cursor.com/agents/bc-8fb1eabf-3f80-494e-99ce-13a494d14029)
- [پیکربندی داده‌محور API](https://cursor.com/agents/bc-3eed5127-4f83-4584-b753-2f97d9fed70a)

## حذف سوابق از اکانت Cursor

این بکاپ فقط فایل‌ها را در گیت ذخیره می‌کند. حذف از اکانت را باید خودتان انجام دهید.

### روش ۱ — آرشیو از UI (ساده، برگشت‌پذیر)
1. بروید به [cursor.com/agents](https://cursor.com/agents)
2. روی چت مورد نظر → منوی `...` → **Archive**
3. برای برگرداندن: فیلتر **Archived**

در UI دکمه‌ی حذف دائمی وجود ندارد؛ برای حذف کامل از روش ۲ استفاده کنید.

### روش ۲ — حذف دائمی با API (غیرقابل برگشت)

**قدم ۱ — گرفتن API key**  
از [cursor.com/dashboard/api](https://cursor.com/dashboard/api) یک key بسازید و کپی کنید.

**قدم ۲ — ست کردن key در ترمینال**
```bash
export CURSOR_API_KEY=کلید_واقعی_شما
```

**قدم ۳ — پیدا کردن شناسه‌ی چت**
```bash
./chat-history-backup/delete-agents.sh --list
```
شناسه در آدرس هر چت هم هست: `https://cursor.com/agents/bc-...`

**قدم ۴ — تست بدون حذف واقعی**
```bash
DRY_RUN=1 ./chat-history-backup/delete-agents.sh bc-XXXX
```

**قدم ۵ — حذف**
```bash
# فقط یک چت:
./chat-history-backup/delete-agents.sh bc-XXXX

# چند چت:
./chat-history-backup/delete-agents.sh bc-XXXX bc-YYYY

# همه‌ی چت‌های بکاپ‌شده (به‌جز چت بکاپ):
./chat-history-backup/delete-agents.sh

# واقعاً همه، شامل چت بکاپ:
SKIP_CURRENT=0 ./chat-history-backup/delete-agents.sh
```

خروجی موفق: `OK (200): bc-...`

### بدون اسکریپت (فقط curl)
```bash
curl -X DELETE https://api.cursor.com/v1/agents/bc-XXXX -u "$CURSOR_API_KEY:"
```

> چت فعلی همین بکاپ `bc-c6224a15-ac68-4eeb-8d95-b0ff9a16fc1f` است و به‌صورت پیش‌فرض حذف نمی‌شود تا کار تمام شود.


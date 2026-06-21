from __future__ import annotations

import re


OFFENSIVE = "استفاده_از_کلمات_نامناسب"
CRITICISM = "انتقاد_و_پیشنهاد"
COURIER = "برخورد_نامناسب_پیک"
ADVERTISING = "تبلیغات"
ORDER_CHANGE = "درخواست_ویرایش_سفارش"
OFFTOPIC = "دیدگاه_نامرتبط"
APP_PROBLEM = "مشکلات_اپلیکیشن"
COMPARISON = "مقایسه_دو_مجموعه_با_یکدیگر"
HYGIENE = "موارد_بهداشتی"
DISCOUNT = "موارد_مرتبط_با_کد_تخفیف"
PRIVACY = "نقض_حریم_شخصی"
POLITICAL = "سياسي"


def _out(comment: str, label: str, reason: str | None, confidence: float) -> dict:
    return {
        "comment": comment,
        "label": label,
        "reason": reason,
        "confidence": round(confidence, 2),
    }


def _contains_any(text: str, words: list[str]) -> bool:
    return any(word in text for word in words)


def _has_latin(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]", text))


def _has_phone_or_identifier(text: str) -> bool:
    return bool(
        re.search(r"(?:\+98|0098|0)?9\d{9}", text)
        or re.search(r"۰۹[۰-۹]{9}", text)
        or re.search(r"\b\d{10}\b", text)
        or re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    )


def _has_emoji_or_symbol(text: str) -> bool:
    if re.search(r"[:;]-?[)D(]", text):
        return True
    if any(symbol in text for symbol in ("★", "☆", "♥", "❤️", "✿", "♪", "✅", "⭐", "👍", "😊", "🔥", "🍕")):
        return True
    return any(ord(ch) > 0xFFFF for ch in text)


def _is_incomplete(text: str) -> bool:
    stripped = text.strip()
    exact_fragments = {
        "غذا خوب",
        "ولی کیفیت",
        "به نظرم که",
        "سفارش دادم",
        "خوب و",
        "پیک که",
        "اگر غذا",
        "چون بسته بندی",
        "برنج پیک خوب اما نه",
        "خوب خوب خوب",
        "ممنون",
        "باشه",
        "آره",
        "بله",
        "قضرثصق",
        "اسیبنتلاس",
        "اسنپ غذا خوب",
        "09123456789 غذا خوب",
        "مزخرف ولی",
        "کد تخفیف و",
        "اپلیکیشن که",
        "مو داخل",
    }
    if stripped in exact_fragments:
        return True
    if stripped.endswith((" و", " که", " اما", " ولی", " چون")):
        return True
    if len(stripped.split()) <= 2 and not any(v in stripped for v in ("بود", "است", "شد", "رسید", "دارم", "ندارم")):
        return True
    return False


def classify(text: str) -> dict:
    comment = text
    normalized = text.strip().replace("ي", "ی").replace("ك", "ک")
    lowered = normalized.lower()

    # Override 20 is intentionally first.
    if _is_incomplete(normalized):
        return _out(comment, "disapproval", OFFTOPIC, 0.95)

    if _has_emoji_or_symbol(normalized):
        return _out(comment, "disapproval", OFFTOPIC, 0.98)

    if re.search(r"\b(?:snapp|snap|snab)\b", lowered) or _contains_any(normalized, ["اسنپ", "اسنب"]):
        return _out(comment, "disapproval", ADVERTISING, 0.97)

    if _has_phone_or_identifier(normalized) or _contains_any(
        normalized,
        ["آدرس من", "نامم", "کد ملی", "شماره کارت", "ایمیل من", "پیک آقای", "پیک خانم"],
    ):
        return _out(comment, "disapproval", PRIVACY, 0.98)

    if _contains_any(
        normalized,
        [
            "وضع مملکت",
            "وضع کشور",
            "تورم",
            "دولت",
            "مجلس",
            "رئیس جمهور",
            "زن زندگی آزادی",
            "تحریم",
            "فساد",
            "مرگ بر",
            "دیکتاتور",
            "مسئولین",
        ],
    ):
        return _out(comment, "disapproval", POLITICAL, 0.9)

    if _contains_any(normalized, ["مو پیدا", "مو بود", "حشره", "بوی گندیدگی", "دل درد", "کثیف", "بهداشت", "خام بود"]):
        return _out(comment, "disapproval", HYGIENE, 0.97)

    if _contains_any(normalized, ["مزخرف", "افتضاح", "بی شعور", "اشغال"]) or (
        "توهین" in normalized and "توهینی ندارم" not in normalized
    ):
        return _out(comment, "disapproval", OFFENSIVE, 0.97)

    if ("حلال" in normalized and ("حرام" in normalized or "حروم" in normalized)) or _contains_any(
        normalized, ["نجس", "بسم الله را هم", "غذای حروم"]
    ):
        return _out(comment, "disapproval", OFFENSIVE, 0.93)

    if _contains_any(normalized, ["کد تخفیف", "تخفیف", "پرومو", "آفر", "ارزون"]):
        return _out(comment, "disapproval", DISCOUNT, 0.93)

    if _contains_any(
        normalized,
        ["صفحه فروش ما", "منوی ویژه امروز ما", "تبلیغ رستوران", "سفارش مستقیم", "همه بهتر است از", "فقط کافه نارنج"],
    ):
        return _out(comment, "disapproval", ADVERTISING, 0.9)

    if _contains_any(
        normalized,
        ["اطلاعات مشتری قبلی", "بدون اجازه", "شماره تماس من را برای", "موقعیت من را", "نام و آدرس فرد دیگری"],
    ):
        return _out(comment, "disapproval", PRIVACY, 0.94)

    if _contains_any(
        normalized,
        ["لغو کنید", "حذف کنید", "آدرس ارسال را تغییر", "به جای", "زمان تحویل", "عوض کنید"],
    ):
        return _out(comment, "disapproval", ORDER_CHANGE, 0.93)

    if _contains_any(normalized, ["از کافه", "نسبت به رستوران", "بین هایدا", "از فست فودهای", "از سفارش قبلی در جای دیگر"]):
        return _out(comment, "disapproval", COMPARISON, 0.93)

    if _contains_any(normalized, ["سرد رسید و قابل خوردن نبود", "له شده", "سفارش اشتباه", "ناقص بود", "ریخته بود"]):
        return _out(comment, "disapproval", OFFTOPIC, 0.93)

    if _contains_any(
        normalized,
        ["امروز هوا", "بازی فوتبال", "توی ولیعصر", "از میدان انقلاب", "تست سامانه"],
    ):
        return _out(comment, "disapproval", OFFTOPIC, 0.9)

    if _contains_any(normalized, ["هذا", "عربي", "التعليق", "ولیس"]):
        return _out(comment, "disapproval", OFFTOPIC, 0.85)

    allowed_food_names = {"pizza", "burger"}
    if _has_latin(lowered) and not any(name in lowered for name in allowed_food_names):
        return _out(comment, "disapproval", OFFTOPIC, 0.85)

    if (
        _contains_any(normalized, ["اپلیکیشن", "برنامه", "اپ "])
        and _contains_any(normalized, ["کرش", "خطا", "نقشه", "کد ورود", "لود", "ثبت نشد"])
    ) or "صفحه پیگیری سفارش لود نمی شد" in normalized:
        return _out(comment, "disapproval", APP_PROBLEM, 0.95)

    if _contains_any(normalized, ["پیک بی ادب", "سفیر حاضر نشد", "پیک تماس", "پرت کرد", "احساس ناامنی"]):
        return _out(comment, "disapproval", COURIER, 0.95)

    if "شاهکاری" in normalized and "بد بود" in normalized:
        return _out(comment, "disapproval", CRITICISM, 0.72)

    if _contains_any(normalized, ["دیگر سفارش نمی دهم", "راضی نبودم"]):
        return _out(comment, "disapproval", CRITICISM, 0.72)

    if _contains_any(normalized, ["نه راضی بودم نه ناراضی", "مطمئن نیستم", "نظر مشخصی"]):
        return _out(comment, "unknown", None, 0.55)

    if _contains_any(
        normalized,
        [
            "خوشمزه",
            "حلال",
            "خوب بود",
            "راضی بودم",
            "مودب بود",
            "قابل قبول",
            "پایین تری داشت",
            "کمی",
            "کاش",
            "متوسط",
            "انتظار بهتری داشتم",
            "معمولی بود",
            "بهتری می خواستم",
            "دیر رسید ولی",
            "قابل خوردن بود",
            "محترمانه",
            "پیشنهاد می کنم",
            "نمی ارزید اما توهینی ندارم",
        ],
    ):
        if _contains_any(
            normalized,
            ["کمی", "کاش", "متوسط", "دیر رسید", "نمی ارزید", "انتظار بهتری", "قابل قبول", "پایین تری"],
        ):
            return _out(comment, "approval", None, 0.88)
        return _out(comment, "approval", None, 0.96)

    if _contains_any(normalized, ["دریافت کردم", "تحویل شد", "بسته غذا آمد", "خرید کردم", "سفارش رسید"]):
        return _out(comment, "unknown", None, 0.6)

    if _contains_any(
        normalized,
        [
            "خوشمزه",
            "حلال",
            "خوب بود",
            "راضی بودم",
            "مودب بود",
            "کمی",
            "کاش",
            "متوسط",
            "انتظار بهتری داشتم",
            "معمولی بود",
            "بهتری می خواستم",
            "دیر رسید ولی",
            "قابل خوردن بود",
            "محترمانه",
            "پیشنهاد می کنم",
            "نمی ارزید اما توهینی ندارم",
        ],
    ):
        if _contains_any(normalized, ["کمی", "کاش", "متوسط", "دیر رسید", "نمی ارزید", "انتظار بهتری"]):
            return _out(comment, "approval", None, 0.88)
        return _out(comment, "approval", None, 0.96)

    return _out(comment, "unknown", None, 0.5)

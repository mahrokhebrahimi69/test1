// Pre-request Script
// فقط در iteration اول گزارش قبلی را پاک می‌کند

const index = pm.info.iteration;

if (index === 0) {
    pm.collectionVariables.set("classification_report", "[]");
    pm.collectionVariables.set("classification_summary", "{}");
    pm.collectionVariables.set("classification_failures", "[]");
    console.log("classification_report reset for new run");
}

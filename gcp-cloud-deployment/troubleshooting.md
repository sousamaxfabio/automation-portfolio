# Troubleshooting Record

## 1. Cloud Run port mismatch

**Symptom:** The original Dockerfile listened on fixed port `8001`.

**Risk:** Cloud Run supplies its required port using the `PORT` environment variable. A container listening elsewhere can fail startup.

**Resolution:** Changed the container command to use `${PORT:-8080}` and verified it locally before deployment.

## 2. Private service returned HTTP 403

**Symptom:** An anonymous request to `/health` returned HTTP `403`.

**Finding:** This was expected. Cloud Run IAM rejected the request before FastAPI received it.

**Resolution:** Generated a Google identity token for the authorized test request. The same endpoint then returned HTTP `200`.

## 3. Readiness returned HTTP 503

**Symptom:** `/health` returned `200`, while `/readiness` returned `503`.

**Finding:** The application process was healthy, but PostgreSQL was not yet connected.

**Resolution:** Created the database, attached the Cloud SQL connection, supplied the database settings and secret, and retested. `/readiness` returned HTTP `200`.

This demonstrated why liveness and readiness checks should remain separate.

## 4. Database secret contained an invisible newline

**Symptom:** Cloud SQL was attached correctly, but `/readiness` still returned HTTP `503`.

**Investigation:** The generated password was expected to contain 48 hexadecimal characters. A safe length check returned `49` without displaying the value.

**Root cause:** The secret-generation pipeline stored the newline emitted by `openssl` as part of the secret. Shell command substitution had stripped that newline when the database password was created, so the injected Cloud Run value did not match.

**Resolution:** Created a second secret version using `printf`, verified its length was `48`, and pinned Cloud Run to version `2`.

## 5. API key returned HTTP 401

**Symptom:** An authenticated request with the API-key header returned HTTP `401 Invalid API key`.

**Finding:** The API-key secret had the same trailing-newline issue, and the Cloud Run configuration still referenced `latest`.

**Resolution:** Created corrected version `2` and replaced the Cloud Run secret mappings with explicit versions. The protected endpoint then returned HTTP `200`.

## 6. Cloud SQL update appeared to fail or hang

**Symptom:** Starting Cloud SQL took longer than the local command expected. One command reported that the operation was taking longer than expected; another remained on `working` for more than ten minutes.

**Finding:** The cloud operation continued even after the local waiting command ended or was interrupted.

**Resolution:** Listed Cloud SQL operations, identified the running operation ID, and waited for that exact operation. It finished with `ERROR: -` and `STATUS: DONE`.

**Operational lesson:** Do not submit a duplicate update merely because a local CLI wait times out. Check the server-side operation first.

## 7. Cloud Shell disconnected

**Symptom:** The browser session disconnected and returned to the home directory after reconnection.

**Finding:** Google Cloud resources remained intact. The Cloud Shell home directory also retained the cloned repository.

**Resolution:** Reopened Cloud Shell, verified the active project, and returned to the working directory. Cloud SQL was explicitly stopped during longer breaks because it runs independently of Cloud Shell.

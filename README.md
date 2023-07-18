# Loom Video Grader

## Tech Stack
- Logic: Python
- API Framework: FastAPI
- Database: MongoDB
- LLM: OpenAI: GPT-3.5-turbo


## API Structure
All endpoints must return JSON compatible data.

- API Root `/` Swagger Docs
- API Version `/version` () -> String
  - HTTP Method: GET
- Create User `/validate` (transcript) -> Bool
  - HTTP Method: GET


## App Structure
- `/app/` Application Package
  - `__init__`
  - `api.py` API File
  - `database.py` Database Interface
- `.env` Environment Variables
- `Procfile` Server Run Script
- `requirements.txt` Dependencies
- `run.sh` Local Run Script
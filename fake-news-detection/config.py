from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
INTERIM = ROOT / "data" / "interim"
PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"
REPORTS = ROOT / "reports"

SEED = 42
TEST_SIZE = 0.15
VAL_SIZE = 0.15
MAX_LEN = 256          # longueur max en tokens pour les transformers
LABEL_FAKE, LABEL_TRUE = 1, 0
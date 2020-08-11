CREATE TABLE IF NOT EXISTS config (
  setting         TEXT NOT NULL,
  value           TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS secrets (
  name            TEXT NOT NULL,
  value           TEXT NOT NULL,
  added           TIMESTAMP CURRENT_TIMESTAMP NOT NULL
);

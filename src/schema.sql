CREATE TABLE IF NOT EXISTS config (
  setting         TEXT NOT NULL,
  value           TEXT NOT NULL
);

CREATE UNIQUE INDEX config_setting_uniq ON config (setting);

CREATE TABLE IF NOT EXISTS secrets (
  name            TEXT NOT NULL,
  value           TEXT NOT NULL,
  updated           TIMESTAMP NOT NULL
);

CREATE UNIQUE INDEX secret_name_uniq ON secrets (name);

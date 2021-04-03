CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    birthday TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS deck (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS card (
    id INTEGER PRIMARY KEY,
    deck_id INTEGER NOT NULL,
    word TEXT NOT NULL,
    translation TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(deck_id) REFERENCES deck (id)
);

CREATE UNIQUE INDEX idx_user_email ON user(email);
CREATE INDEX idx_deck_user_id ON deck(user_id);
CREATE INDEX idx_card_deck_id ON card(deck_id);

CREATE TRIGGER tg_deck_updated_at
    AFTER UPDATE ON deck
BEGIN
    UPDATE deck SET updated_at = CURRENT_TIMESTAMP
    WHERE id = old.id;
END;

CREATE TRIGGER tg_card_updated_at
    AFTER UPDATE ON card
BEGIN
    UPDATE card SET updated_at = CURRENT_TIMESTAMP
    WHERE id = old.id;
END;

CREATE TRIGGER  tg_user_updated_at
    AFTER UPDATE ON user
BEGIN
    UPDATE user SET updated_at = CURRENT_TIMESTAMP
    WHERE id = old.id;
END;


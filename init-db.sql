CREATE TABLE conversation
(
    id           SERIAL PRIMARY KEY,
    session_id   UUID      NOT NULL,
    created_at   timestamp NOT NULL,
    question     varchar NOT NULL,
    response     varchar NOT NULL,
    error_message varchar
);

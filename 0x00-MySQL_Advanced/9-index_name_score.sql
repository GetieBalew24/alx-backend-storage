-- sql script to Creates an index idx_name_first_score on the table names,
-- the first letter of name & tscore.
CREATE INDEX idx_name_first_score ON names(name(1), score);
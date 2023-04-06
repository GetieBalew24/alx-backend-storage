-- SQL script that ranks country of origin bands,
-- Ordered by (non-unique) fans.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
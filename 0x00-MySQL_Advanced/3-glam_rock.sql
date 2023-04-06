-- SQL script or statement that lists all bands with Glam rock as style, 
-- ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%' 
    ORDER BY lifespan DESC;
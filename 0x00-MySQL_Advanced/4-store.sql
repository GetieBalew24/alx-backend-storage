-- a SQL script to create a trigger by decreases the quantity of an item 
-- after adding a new order.
DROP TRIGGER IF EXISTS reduce_item_quantity;
CREATE TRIGGER reduce_item_quantity
AFTER INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;
-- create a enum with some possible values
CREATE TYPE orderstatus as ENUM ('ordered', 'preparing', 'shipped', 'delivered', 'cancelled');

-- create a table, that uses this enum as a column
CREATE TABLE orders(id SERIAL PRIMARY KEY, customer VARCHAR(50) NOT NULL, status orderstatus NOT NULL);

-- insert rows with valid status
INSERT INTO orders (customer, status) VALUES
    ('peter', 'ordered'), 
    ('heins', 'ordered'), 
    ('günter', 'preparing'), 
    ('tina', 'shipped'), 
    ('julia', 'delivered'), 
    ('viktor', 'cancelled');

-- insert something, that is not in the enum will fail
INSERT INTO orders (customer, status) VALUES
    ('peter', 'not in list');

-- in camparisions the index is used, not the alphabet
SELECT * FROM orders WHERE status < 'shipped';
-- delivered and cancelled are wbefore shipped in the alphabet, 
-- but are in the enum after shipped, so the result is:

--  id | customer |  status   
-- ----+----------+-----------
--   1 | peter    | ordered
--   2 | heins    | ordered
--   3 | günter   | preparing

-- ofcause you can also check for specific values
SELECT * FROM orders where status IN ('delivered', 'cancelled');

-- to see which enums are available in the database
SELECT typname FROM pg_type WHERE typtype = 'e';

-- with this list you can check agin which values these enums have...e.g.
SELECT enumlabel FROM pg_enum WHERE enumtypid = 'orderstatus'::regtype;
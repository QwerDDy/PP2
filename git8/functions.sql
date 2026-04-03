CREATE OR REPLACE FUNCTION SEARCH_NAME(pattern TEXT)
RETURNS TABLE(name VARCHAR, number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.name AS name, phonebook.number AS number
    FROM phonebook
    WHERE phonebook.name ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION SEARCH_NUMBER(pattern TEXT)
RETURNS TABLE(name VARCHAR, number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.name AS name,
           phonebook.number AS number
    FROM phonebook
    WHERE phonebook.number = pattern;
END;
$$ LANGUAGE plpgsql;

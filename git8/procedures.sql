CREATE PROCEDURE UPSET_USER(u TEXT, p TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phonebook(name, number)
    VALUES (u, p)
    ON CONFLICT (number)
    DO UPDATE SET name = EXCLUDED.name;
END;
$$;

CREATE OR REPLACE PROCEDURE UPDATE_NAME(oldnumber TEXT,oldname TEXT, new_name TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF oldnumber IS NOT NULL THEN
    UPDATE phonebook SET name = new_name WHERE number = oldnumber;
    ELSIF oldname IS NOT NULL AND oldnumber IS NULL THEN
    UPDATE phonebook SET name = new_name WHERE name = oldname;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE DELETE_COL(delname TEXT, delnumber TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF delnumber IS NOT NULL THEN
    DELETE FROM phonebook WHERE number = delnumber;
    ELSIF delname IS NOT NULL AND delnumber IS NULL THEN
    DELETE FROM phonebook WHERE name = delname;
    END IF;
END;
$$;
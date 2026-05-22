# What is DBMS?

DBMS stands for Database Management System. It stores and manages data using defined rules and structures.

## Codd's 12 Rules (brief)

1. Information rule — All information represented logically as values in tables.
2. Guaranteed access rule — Every datum accessible by table name, primary key, and column name.
3. Systematic treatment of nulls — Null values (missing/unknown) are supported and distinct from zero or empty.
4. Dynamic online catalog based on the relational model — Metadata represented as regular tables.
5. Comprehensive data sublanguage rule — A single language for data definition, manipulation, transaction control, and integrity constraints.
6. View updating rule — All theoretically updatable views are updatable through the system.
7. High-level insert, update, delete — Set-at-a-time operations for handling multiple rows.
8. Physical data independence — Application programs unaffected by changes in physical storage.
9. Logical data independence — Application programs unaffected by changes in logical schema.
10. Integrity independence — Integrity constraints definable in the catalog and not in application programs.
11. Distribution independence — Users should not need to know whether data is distributed across locations.
12. Non-subversion rule — Low-level access cannot bypass integrity rules enforced by the high-level language.

Reference: E. F. Codd's relational model rules (summarized).
   
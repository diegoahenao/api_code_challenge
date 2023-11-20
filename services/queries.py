from sqlalchemy import text

class Query():

    def __init__(self, db) -> None:
        self.db = db

    def get_query_one(self):

        query = text("""
            WITH quarters AS (
                SELECT
                    d.department,
                    j.job,
                    CASE
                        WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 1 THEN 'Q1'
                        WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2 THEN 'Q2'
                        WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 3 THEN 'Q3'
                        WHEN EXTRACT(QUARTER FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 4 THEN 'Q4'
                    END AS quarter,
                    COUNT(*) AS hired
                FROM
                    hired_employees AS he
                LEFT JOIN
                    departments AS d
                ON CAST(he.department_id AS VARCHAR) = CAST(d.id_departments AS VARCHAR)
                LEFT JOIN
                    jobs AS j
                ON CAST(he.job_id AS VARCHAR) = CAST(j.id_jobs AS VARCHAR)
                WHERE (SELECT * FROM EXTRACT(YEAR FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"'))) = 2021
                GROUP BY d.department, j.job, quarter),

                    base AS (SELECT DISTINCT department, job
                            FROM quarters)

            SELECT
                b.department,
                b.job,
                COALESCE(q_one.Q1, 0) AS Q1,
                COALESCE(q_two.Q2, 0) AS Q2,
                COALESCE(q_three.Q3, 0) AS Q3,
                COALESCE(q_four.Q4, 0) AS Q4
            FROM base AS b
            LEFT JOIN (SELECT hired AS Q1, department, job FROM quarters WHERE quarter = 'Q1') q_one
            ON b.department = q_one.department AND b.job = q_one.job
            LEFT JOIN (SELECT hired AS Q2, department, job FROM quarters WHERE quarter = 'Q2') q_two
            ON b.department = q_two.department AND b.job = q_two.job
            LEFT JOIN (SELECT hired AS Q3, department, job FROM quarters WHERE quarter = 'Q3') q_three
            ON b.department = q_three.department AND b.job = q_three.job
            LEFT JOIN (SELECT hired AS Q4, department, job FROM quarters WHERE quarter = 'Q4') q_four
            ON b.department = q_four.department AND b.job = q_four.job;
            """)
        
        result = self.db.execute(query).fetchall()
        output = []
        for row in result:
            output.append({
                "department": row[0],
                "job": row[1],
                "q1": row[2],
                "q2": row[3],
                "q3": row[4],
                "q4": row[5],
            })

        return output
    
    def get_query_two(self):

        query = text("""
            WITH group_1 AS (
                SELECT 
                    d.id_departments, 
                    MAX(d.department) AS department, 
                    COUNT(*) AS hired
                FROM 
                    hired_employees AS he
                LEFT JOIN 
                    departments AS d
                ON CAST(he.department_id AS VARCHAR) = CAST(d.id_departments AS VARCHAR)
                WHERE (SELECT * FROM EXTRACT(YEAR FROM TO_TIMESTAMP(he.datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"'))) = 2021
                AND d.id_departments IS NOT NULL
                GROUP BY d.id_departments),

                    group_1_avg AS (
                        SELECT 
                            AVG(hired) 
                        FROM 
                            group_1
                    )

            SELECT 
                d.id_departments, 
                MAX(d.department) AS department, 
                COUNT(*) AS hired
            FROM 
                hired_employees AS he
            LEFT JOIN 
                departments AS d
            ON CAST(he.department_id AS VARCHAR) = CAST(d.id_departments AS VARCHAR)
            GROUP BY d.id_departments
            HAVING COUNT(*) > (SELECT * FROM group_1_avg)
            ORDER BY hired DESC
            """)
        
        result = self.db.execute(query).fetchall()
        output = []
        for row in result:
            output.append({
                "id": row[0],
                "department": row[1],
                "hired": row[2]
            })

        return output
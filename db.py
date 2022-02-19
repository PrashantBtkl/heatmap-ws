import os
import uuid
import psycopg2


PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_DB   = os.getenv("PG_DB")


heatmaps_table = "test_heatmaps"

store_positions_query = """
INSERT into {tbl}
(id, x, y, user_id, page_id)
VALUES
(%s,%s,%s,%s,%s)
""".format(
    tbl=heatmaps_table
)

def get_conn():
    return psycopg2.connect(
        host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB
    )


def store_positions(pos, conn):
	x = int(pos["x"])
	y = int(pos["y"])
	user_id = str(pos["session_id"])
	page_id = str(pos["page_id"])
	try:
		with conn:
			with conn.cursor() as cur:
				cur.execute(
					store_positions_query,
					(str(uuid.uuid4()), x, y, user_id, page_id,),
				)
	except Exception as e:
		print("exception occurred : ", e)
		print("position :",pos," not stored")
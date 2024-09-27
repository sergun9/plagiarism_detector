import psycopg2
from database.config import host, user, password, db_name



def insert_shingles(document_name, shingles):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cur = connection.cursor()


        for shingle in shingles:
            try:
                cur.execute(
                    "INSERT INTO shingles(document_name, shingle) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                    (document_name, shingle)
                )
            except Exception as e:
                print(f"Error inserting shingle: {e}")

        connection.commit()
        cur.close()
            

    except Exception as _ex:
        print("[INFO] error while working with PostgeSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreQSL connection closed")



if __name__ == "__main__":
    doc_name = "test"
    shingles_list = ["example shingle1", "example shingle2"]
    insert_shingles(doc_name, shingles_list)
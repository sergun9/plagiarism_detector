import psycopg2
from database.config import host, user, password, db_name


def find_similar_documents(shingles):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cur = connection.cursor()

        cur.execute(
            "SELECT document_name, COUNT(*) as common_shingles "
            "FROM shingles "
            "WHERE shingle = ANY(%s) "
            "GROUP BY document_name "
            "ORDER BY common_shingles DESC;",
            (shingles,)
        )

        return cur.fetchall()

    except Exception as _ex:
        print("[INFO] error while working with PostgeSQL", _ex)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("[INFO] PostgreQSL connection closed")


if __name__ == "__main__":
    shingles_list = ["example shingle1", "gdfghdfg  sdfgfsdfg dsgdsfgdfg dsfgds"]
    # Пример поиска совпадений
    similar_docs = find_similar_documents(shingles_list)
    print(similar_docs[0][1])
from version_prueba.config import VECTOR_DB

if VECTOR_DB == "milvus":
    from version_prueba.apps.retrieval.vector.dbs.milvus import MilvusClient

    VECTOR_DB_CLIENT = MilvusClient()
else:
    from version_prueba.apps.retrieval.vector.dbs.chroma import ChromaClient

    VECTOR_DB_CLIENT = ChromaClient()

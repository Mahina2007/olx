# from apps.admin.queries import *
#
# def add_kitchen(name, owner_id):
#     query = """
#         SELECT id FROM users
#         WHERE id = %s AND role = 'canteen';
#     """, (owner_id,)
#     execute_query(query=query)
#
#     query = """
#         INSERT INTO kitchens (name, owner_id)
#         VALUES (%s, %s)
#         RETURNING id;
#     """, (name, owner_id)

# # database.py
# import MySQLdb
# import sshtunnel
#
# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0
#
#
# def get_data():
#     with sshtunnel.SSHTunnelForwarder(
#             ('ssh.pythonanywhere.com'),
#             ssh_username='username', ssh_password='hashed',
#             remote_bind_address=('username.mysql.pythonanywhere-services.com', 3306)
#     ) as tunnel:
#         connection = MySQLdb.connect(
#             user='username',
#             passwd='hashed',
#             host='127.0.0.1', port=tunnel.local_bind_port,
#             db='username$dbName',
#         )
#         # Do stuff
#         with connection as con:
#             with con.cursor() as c:
#                 c.execute("SELECT * FROM table;")
#                 res = c.fetchall()
#
#     return res

import mysql.connector

conn = mysql.connector.connect(
  host="HannibalAlex.mysql.pythonanywhere-services.com",
  user="HannibalAlex",
  password="&b]st:Z8%R9d3XCPN<1?@Yt",
  database="HannibalAlex$teatro_lp"
)

mycursor = conn.cursor()

mycursor.execute("SELECT * FROM teatro_arg")

results = mycursor.fetchall()

for rows in results:
  print(rows)
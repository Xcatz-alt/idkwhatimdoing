import mysql.connector
#ganti password sama usernya sesuai user yg ko buat pas pertama kali install
#data basenya ganti sesuai nama file database ko
nama_db = {
    'user' : 'root',
    'password' : 'password',
    'host' : 'localhost',
    'database' : 'aset',
}

connection = mysql.connector.connect(**nama_db)
cursor =  connection.cursor()
cursor.execute(
    """CREATE TABLE aset_data2(
        no char(9),
        kmk char(15),
        nama_mata_kuliah char(30),
        sks char(5),
        kode_kelas char(30),
        ruang char(30),
        hari char(30),
        shift char(30))""")
connection.commit()
print("dah")
connection.close

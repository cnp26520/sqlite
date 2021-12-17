import sqlite3
import random
con = sqlite3.connect('example.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS homelands
    (homeland_id INT AUTO_INCREMENT, 
    home_name VARCHAR(45) NOT NULL,
    alignment VARCHAR(45),
    land_description VARCHAR(30) NOT NULL,
    PRIMARY KEY (homeland_id)
    )''')

cur.execute('''INSERT INTO homelands VALUES
(1, 'Toxus', 'bad', 'A land covered in toxins'),
(2, 'Trunia', 'good', 'A land bathed in light'),
(3, 'Darkuz', 'bad', 'A land smothered in shadow'),
(4, 'Foglight', 'neutral', 'A land hidden in the mist')''')

cur.execute("""CREATE TABLE champions (
champion_id INT AUTO_INCREMENT, 
first_name VARCHAR(30) NOT NULL,
title VARCHAR(25) NOT NULL,
weapon VARCHAR(25) NOT NULL,
homeland_id INT,
PRIMARY KEY (champion_id),
FOREIGN KEY (homeland_id) REFERENCES homelands(homeland_id)
)""")

cur.execute("""INSERT INTO champions VALUES
	(1, 'Baldur' , 'The Rock', "Warhammer", 2),
    (2, 'Shadow Sneak' , 'The Hidden', "Daggers", 4),
    (3, 'Darien' , 'The Great Maul', "Maul", 3),
    (4, 'Ubleck' , 'The Slime', "Acid", 1),
	(5, 'Trish' , 'The Protector', "Sword and Shield", 2),
    (6, 'Dante' , 'The Forgotten', "Pistols", 3),
	(7, 'Thomas' , 'The Champion', "Great Sword", 2),
    (8, 'Akatash' , 'The Silent', "Machete", 4),
    (9, 'Shenji' , 'The Eye of Night', "Bow", 4),
    (10, 'Flumox' , 'The Putrid', "Axe", 1),
    (11, 'Fitzgerald' , 'The Entertainer', "Sword and Shield", 2),
    (12, 'Parthenon' , 'The Killer', "Warhammer", 3);

""")



cur.execute('SELECT * FROM homelands ')
print(cur.fetchone())

cur.execute('SELECT * FROM champions ') 
print(cur.fetchall())

for row in cur.execute("""SELECT(first_name || " of " || home_name)
FROM champions
INNER JOIN homelands
ON champions.homeland_id = homelands.homeland_id"""):
    hero = row[0]
print(hero)
enemies = ['Baldur of Trunia', 'Shadow Sneak of Foglight', 'Darien of Darkuz', 'Ubleck of Toxus', 'Trish of Trunia', 'Dante of Darkuz', 'Thomas of Trunia', 'Akatash of Foglight', 'Shenji of Foglight', 'Flumox of Toxus', 'Fitzgerald of Trunia']
print(enemies)
print(hero, "Enters into battle")
enemy = random.choice(enemies)
print(enemy, "Enters into battle")
damage = [5, 9]
hero_hp = 100
enemy_hp = 100
while hero_hp > 0:
    print(hero_hp, ": Your current health")
    hero_hp = hero_hp - random.choice(damage)
    print(enemy_hp, ": Enemies current health")
    enemy_hp = enemy_hp - random.choice(damage)
    if enemy_hp <= 0:
        print(hero, " Wins")
    elif hero_hp <=0:
        print(enemy, " Wins")

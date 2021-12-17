import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

data = {'name':'Baldur', 'title':'The Rock', 'weapon':'Warhammer', }
data2 = {'name':'Shadow Sneak', 'title':'The Hidden', 'weapon':'Daggers', }
data3 = {'name':'Darien', 'title':'The Great Maul', 'weapon':'Maul', }
data4 = {'name':'Ubleck', 'title':'The Slime', 'weapon':'Acid', }
data5 = {'name':'Trish', 'title':'The Protector', 'weapon':'Sword and Shield', }
data6 = {'name':'Dante', 'title':'The Forgotten', 'weapon':'Pistols', }
data7 = {'name':'Thomas', 'title':'The Champion', 'weapon':'Great Sword', }
data8 = {'name':'Akatash', 'title':'The Silent', 'weapon':'Machete', }
data9 = {'name':'Shenji', 'title':'The Eye of Night', 'weapon':'Bow', }
data10 = {'name':'Flumox', 'title':'The Putrid', 'weapon':'Axe', }
data11 = {'name':'Fitzgerald', 'title':'The Entertainer', 'weapon':'Sword and Shield', }
data12 = {'name':'Parthenon', 'title':'The Killer', 'weapon':'Warhammer', }
db.collection('champions').document('Baldur').set(data)
db.collection('champions').document('Shadow Sneak').set(data2)
db.collection('champions').document('Darien').set(data3)
db.collection('champions').document('Ubleck').set(data4)
db.collection('champions').document('Trish').set(data5)
db.collection('champions').document('Dante').set(data6)
db.collection('champions').document('Thomas').set(data7)
db.collection('champions').document('Akatosh').set(data8)
db.collection('champions').document('Shenji').set(data9)
db.collection('champions').document('Flumox').set(data10)
db.collection('champions').document('Fitzgerald').set(data11)
db.collection('champions').document('Parthenon').set(data12)

parth = db.collection('champions').document('Parthenon')
parth.update({'weapon': 'Spear'})

db.collection("champions").document('Shenji').delete()

parth_info = parth.get()
if parth_info.exists:
    print(f'Document data: {parth_info.to_dict()}')
else:
    print("oof")

people = db.collection('champions')
shields = db.collection('champions').where('weapon', '==', 'Sword and Shield').stream()
for people in shields:
    print(f'{people.id} => {people.to_dict()}')

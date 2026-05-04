from models import Puppy,Owner,Toy,app,db

with app.app_context():

    rufus = Puppy('Rufus')
    fido = Puppy('Fido')

    db.session.add_all([rufus,fido])
    db.session.commit()

    # Check!
    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    karol = Owner('Karol',rufus.id)

    toy1 = Toy('Chew Toy',rufus.id)
    toy2 = Toy('Ball',rufus.id)

    db.session.add_all([karol,toy1,toy2])
    db.session.commit()

    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    print(rufus.report_toys())










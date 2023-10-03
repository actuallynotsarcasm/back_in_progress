from sqlalchemy.orm import Session
from sqlalchemy import insert

from schemas import engine, Cars, Dealers, Moderators


def get_all_cars():
    session = Session(bind=engine)
    query = session.query(Cars.id, Cars.slug, Cars.brand, Cars.model, Cars.complement, Cars.photo_id, Cars.price, Cars.trade_in_profit, Cars.credit_profit).all()
    session.close()
    resp = {row[1]: row._asdict() for row in query}
    return resp


def add_car(car: dict):
    car_slug = car['car_slug']
    session = Session(bind=engine)
    query = session.query(Cars.id, Cars.slug, Cars.brand, Cars.model, Cars.complement, Cars.photo_id, Cars.price, Cars.trade_in_profit, Cars.credit_profit).filter(Cars.slug == car_slug).first()
    session.close()
    if not query:
        conn = engine.connect()
        ins = insert(Cars)
        res = conn.execute(ins, [car])
        conn.commit()
        conn.close()
        return res
    else:
        return None


def get_car_by_slug(car_slug: str):
    session = Session(bind=engine)
    query = session.query(Cars.id, Cars.slug, Cars.brand, Cars.model, Cars.complement, Cars.photo_id, Cars.price, Cars.trade_in_profit, Cars.credit_profit).filter(Cars.slug == car_slug).first()
    session.close()
    if query:
        return query._asdict()
    else:
        return None


def delete_car(car_slug: str):
    session = Session(bind=engine)
    query = session.query(Cars).filter(Cars.slug == car_slug).first()
    if query:
        session.delete(query)
        session.commit()
    session.close()
    return query

##############

def get_all_dealers():
    session = Session(bind=engine)
    query = session.query(Dealers.id, Dealers.slug, Dealers.name, Dealers.address).all()
    session.close()
    resp = {row[1]: row._asdict() for row in query}
    return resp


def add_dealer(dealer: dict):
    dealer_slug = dealer['dealer_slug']
    session = Session(bind=engine)
    query = session.query(Dealers.id, Dealers.slug, Dealers.name, Dealers.address).filter(Dealers.slug == dealer_slug).first()
    session.close()
    if not query:
        conn = engine.connect()
        ins = insert(Dealers)
        res = conn.execute(ins, [dealer])
        conn.commit()
        conn.close()
        return res
    else:
        return None


def get_dealer_by_slug(dealer_slug: str):
    session = Session(bind=engine)
    query = session.query(Dealers.id, Dealers.slug, Dealers.name, Dealers.address).filter(Dealers.slug == dealer_slug).first()
    session.close()
    if query:
        return query._asdict()
    else:
        return None


def delete_dealer(dealer_slug: str):
    session = Session(bind=engine)
    query = session.query(Dealers).filter(Dealers.slug == dealer_slug).first()
    if query:
        session.delete(query)
        session.commit()
    session.close()
    return query

##############

def get_all_moderators():
    session = Session(bind=engine)
    query = session.query(Moderators.id, Moderators.dealer_id, Moderators.name, Moderators.surname).all()
    session.close()
    resp = {row[1]: row._asdict() for row in query}
    return resp


def add_moderator(moderator: dict):
    conn = engine.connect()
    ins = insert(Moderators)
    res = conn.execute(ins, [moderator])
    conn.commit()
    conn.close()
    return res


def get_moderator_by_id(id: int):
    session = Session(bind=engine)
    query = session.query(Moderators.id, Moderators.dealer_id, Moderators.name, Moderators.surname).filter(Moderators.id == id).first()
    session.close()
    if query:
        return query._asdict()
    else:
        return None


def delete_moderator(id: int):
    session = Session(bind=engine)
    query = session.query(Moderators).filter(Moderators.id == id).first()
    if query:
        session.delete(query)
        session.commit()
    session.close()
    return query
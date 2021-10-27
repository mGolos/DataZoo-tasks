import streamlit as st
from db import Weather, opendb
from sqlalchemy.orm import load_only


def main():
    st.title('Task 2: History')
    db = opendb()
    
    # Asks for all dates and ids only
    results = db.query(Weather)\
        .options(load_only('id','date'))\
        .order_by(Weather.date.asc())\
        .all()
    results_dict = [{'id': row.id, 'date': row.date} for row in results]

    if len(results_dict):
        # Choosing one from the dates
        if len(results_dict) > 1:
            rad = st.select_slider('Select a date:', results_dict, format_func=lambda r: r['date'].date())
            chosen = db.query(Weather).filter(Weather.id == rad['id']).first()

        # Or selecting the only one entry
        else:
            chosen = db.query(Weather).first()
            st.info(f"Only one record ({chosen.date.isoformat(' ', 'seconds')})")
            
        # Display
        st.info(f"At {chosen.date.time().strftime('%X')}")
        st.json(chosen.json)
        st.caption(f"JSON data from {chosen.date.isoformat(' ', 'seconds')}")
    else:
        st.warning('No record yet.')
        
    db.close()


if __name__ == "__main__":
    main()
import streamlit as st
from src.recommender import search_movie, recommend
from src.tmdb_api import fetch_movie_details

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -------------------- Title --------------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies similar to your favourite movie using NLP and Cosine Similarity."
)

# -------------------- Search --------------------

movie_name = st.text_input("🔍 Search Movie")

if movie_name:

    results = search_movie(movie_name)

    if len(results) == 0:

        st.error("Movie not found.")

    else:

        selected_movie = st.selectbox(
            "Select a Movie",
            results["title"].values
        )

        if st.button("🎯 Recommend"):

            # ==========================
            # Selected Movie
            # ==========================

            selected_movie_id = results[
                results["title"] == selected_movie
            ].iloc[0]["movie_id"]

            selected_details = fetch_movie_details(selected_movie_id)

            st.subheader("🎬 Selected Movie")

            col1, col2 = st.columns([1, 2])

            with col1:

                poster_path = selected_details.get("poster_path")

                if poster_path:

                    poster_url = (
                        "https://image.tmdb.org/t/p/w500"
                        + poster_path
                    )

                    st.image(
                        poster_url,
                        use_container_width=True
                    )

                else:

                    st.write("No Poster Available")

            with col2:

                st.markdown(f"## {selected_movie}")

                st.write(
                    f"⭐ Rating : {selected_details.get('vote_average', 'N/A')}"
                )

                st.write(
                    f"📅 Release : {selected_details.get('release_date', 'N/A')}"
                )

                overview = selected_details.get("overview")

                if overview:

                    st.write(overview)

            st.divider()

            # ==========================
            # Recommended Movies
            # ==========================

            st.subheader("🎯 Recommended Movies")

            recommendations = recommend(selected_movie)

            # 4 Movies Per Row
            for i in range(0, len(recommendations), 4):

                cols = st.columns(4)

                for col, movie in zip(cols, recommendations[i:i+4]):

                    details = fetch_movie_details(movie["movie_id"])

                    with col:

                        poster_path = details.get("poster_path")

                        if poster_path:

                            poster_url = (
                                "https://image.tmdb.org/t/p/w500"
                                + poster_path
                            )

                            st.image(
                                poster_url,
                                use_container_width=True
                            )

                        else:

                            st.write("No Poster Available")

                        st.markdown(
                            f"**{movie['title']}**"
                        )

                        st.write(
                            f"⭐ {details.get('vote_average', 'N/A')}"
                        )

                        st.write(
                            f"📅 {details.get('release_date', 'N/A')}"
                        )

                st.write("")
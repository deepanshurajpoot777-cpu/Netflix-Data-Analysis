# import the libraries
import pandas as pd
import matplotlib.pyplot as plt
# load data
df=pd.read_csv("netflix_titles.csv")

#clean data
df=df.dropna(subset=["type","release_year","rating","country","duration"])

type_counts=df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=["skyblue","orange"])
plt.title("Number of movies vs tv shows on netflix")
plt.xlabel("type")
plt.ylabel("count")
plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()

rating_counts=df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct="%1.1f%%",startangle=90)
plt.title("percentage of content rating")
plt.tight_layout()
plt.savefig("content rating.png")
plt.show()

movies_df=df[df["type"]=="Movie"].copy()
movies_df["duration_int"]=movies_df["duration"].str.replace("min","").astype(int)

plt.figure(figsize=(8,6))
plt.hist(movies_df["duration_int"],bins=30,color="purple",edgecolor="black")
plt.title("Distribution of movie duration")
plt.xlabel("Duration minutes")
plt.ylabel("Number of movies")
plt.tight_layout()
plt.savefig("movie_duration_histogram.png")
plt.show()

release_counts=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_counts.index,release_counts.values,color="red")
plt.title("relese_year vs movies")
plt.xlabel("Realese year")
plt.ylabel("Number of shoes")
plt.tight_layout()
plt.savefig("release_yeasr scatter.png")
plt.show()

country_counts=df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color="teal")
plt.title("Top 10 country by no of shows")
plt.xlabel("no of shows")
plt.ylabel("country")
plt.tight_layout()
plt.savefig("top_10_ountry.png")
plt.show()

content_by_year=df.groupby(["release_year","type"]).size().unstack().fillna(0)

flg,ax=plt.subplots(1,2,figsize=(12,6))

#first supplot movies

ax[0].plot(content_by_year.index,content_by_year["Movie"],color="blue")
ax[0].set_title("movies relesed per year")
ax[0].set_xlabel("year")
ax[0].set_ylabel("numbers of movies")

# second subplot:Tv shows

ax[1].plot(content_by_year.index,content_by_year["TV Show"],color="orange")
ax[1].set_title("Tv shows relesed per year")
ax[1].set_xlabel("year")
ax[1].set_ylabel("numbers of Tv shows")

plt.suptitle("comparison of movies and tv shows realesed over year")

plt.tight_layout()
plt.savefig("movies_tvshows_comparision.png")

plt.show()
import turtle

st = turtle.Turtle()

# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)
# st.forward(180)
# st.left(140)



# using for loop

# for i in range(25):
#     st.forward(180)
#     st.left(140)


# coloring it

st.color("red", "yellow")

st.begin_fill()
for i in range(18):
    st.forward(180)
    st.left(140)

st.end_fill()

turtle.done()
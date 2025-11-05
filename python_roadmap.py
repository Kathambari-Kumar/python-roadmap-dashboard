import streamlit as st
from streamlit_js_eval import streamlit_js_eval

screen_width = streamlit_js_eval(js_expressions="screen.width", key="width")
# Theme selector

# Create horizontal layout
hide_streamlit_style = """
    <style>
     #MainMenu {visibility: hidden;}
     header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background-color: #fdf6e3;
}
.stApp {
    background-color: #fff8dc;
    color: #333333;
}
div[data-testid="stHeader"] {
    background-color: #C2B280;
    border-bottom: 2px solid #ff7f50;
}
h1, h2, h3 {
    color: #6a1b9a;
}
section[data-testid="stSidebar"] {
    background-color: #fff8dc;
    border-right: 2px solid #C2B280;
}
.sidebar-title {
    color:#6a1b9a;
    font-size : 20px;
    font-weight:bold;
}

/* Hide mobile menu on screens wider than 768px */
@media (max-width: 768px) {
    .avatar {
        display:none;   
    }
    .mobile-menu {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="My Python Learning Journey",
    page_icon = ":streamlit",
    layout="wide",  # Options: "centered" or "wide"
    initial_sidebar_state="expanded",  # or "collapsed"
)
st.markdown("""
<div style='display: flex; align-items: center; gap: 10px'>
    <img src="https://cdn-icons-png.flaticon.com/512/1822/1822920.png" width="60">
    <h1 style='margin: 0'>Python Learning Roadmap</h1>
</div>
""", unsafe_allow_html=True)

st.caption("Curated by Kathambari — blending backend clarity with creative storytelling")

# Sidebar navigation
st.sidebar.markdown('<div class="sidebar-title">📚 Explore Roadmap</div>', unsafe_allow_html=True)
st.sidebar.divider()
sidebar_choice = st.sidebar.radio("", [
    "Welcome",
    "About Me",
    "Foundations",
    "Advanced Concepts",
    "OOP",
    "Practical Python",
    "Automation & Pipelines",
    "NumPy Fundamentals",
    "Testing Modules",
    "Currently Exploring"
])


# Section content

if screen_width and screen_width < 768:
    st.markdown("""
        <div style='text-align: center; font-size: 14px; color: #6A5ACD; margin-bottom: 10px;'>
        📱 Tap below to explore the roadmap
        </div>
        """, unsafe_allow_html=True)
    menu_choice = st.selectbox(
        "",
        ["Welcome", "About Me", "Foundations", "Advanced Concepts", "OOP", "Practical Python",
         "Automation & Pipelines", "NumPy Fundamentals", "Testing Modules", "Currently Exploring"]
    )
    active_section = menu_choice
else:
    menu_choice = None
    active_section = sidebar_choice

if active_section == "Welcome":
    st.markdown("""
    <div style="text-align:center; padding:30px; background-color:#fff8dc; border-radius:10px; border:2px solid #C2B280">
        <h1 style="color:#6a1b9a">Welcome to My Python Learning Roadmap</h1>
        <p style="font-size:18px; color:#333333">Crafted with clarity, creativity, and care.</p>
        <img src="https://cdn-icons-png.flaticon.com/512/1822/1822920.png" width="100">
    </div>
    """, unsafe_allow_html=True)

elif sidebar_choice == "About Me" or menu_choice=="About Me":
    st.subheader("About me")
    col1, col2 = st.columns([2, 1])  # col1 takes twice the width of col2
    st.markdown("""
       <div style="display:flex; border: 2px solid #C2B280; padding: 10px; border-radius: 8px; background-color:white; gap:20px"> 
       <div style="flex:7; padding: 10px">
            <p style="font-size:20px">With a storyteller’s eye for detail and a developer’s drive for structure, 
            I craft seamless digital journeys—from elegant front-end interfaces to robust back-end architecture. 
            I build software with the same care I bring to storytelling: clear, thoughtful, and deeply user-focused. 
            I thrive where creativity meets code, transforming technology from mere function into feeling. 
            To me, great software should be like poetry—elegant, intuitive, and profoundly human.</p>
        </div>
        <div  class ="avatar" style="flex:3; text-align:center; padding-top:35px">
        <img src = "https://t3.ftcdn.net/jpg/07/28/48/98/360_F_728489827_qtQHjlMEeD53QhTdUEtdOvNPQw21pYjh.jpg" style="width:140px;height:140px">
        <p style="color:#C2B280; font-size:20px">Developer | Designer | Author</p>
        </div>
    """, unsafe_allow_html=True)

elif active_section == "Foundations":
    st.header("🔰 Python Foundations")
    with st.expander("🐣 Basic Syntax & Variables"):
        st.markdown("- Python syntax, indentation\n- Variable assignment\n- Naming conventions\n- User Input\n- Type Casting")
        st.code("""
            # Global variable example
            food = "Pizza"
            def order():
                print("Ordered:", food)
            order()
            print(food)  # This works — 'food' is global
            """, language="python")

        st.code(""" 
        # Enclosing Variable Scope (Closure)
        def cart():
            discount = 1.0
            def checkout():
                print("Discount is:", discount)
            checkout()
        cart()
        """, language="python")

        st.code("""
        # Built-in Variable
        print(__file__)  # Shows the filename of the current script 
        """, language="python")

        st.code(""" 
        # Global Variable Scope
        User_id = 'U_123456'
        def homepage():
            print("Welcome", User_id)
        
        def profile():
            print(f"Welcome to the profile page {User_id}!")
        homepage()
        profile()

        """, language="python")

        st.code("""
        #User Input ( Interactive)
        a = input("Enter a number: ")
        b = input("Enter another number: ")
        print(int(a) + int(b))
        """, language="python")

        st.code("""
        #TypeCasting
        x = "10"
        print(type(x))        #Output <class 'str'>
        print(int(x))         #Output 10
        print(type(int(x)))   #Output <class 'int'>

        """, language="python")

    with st.expander("🧵 String Manipulation Techniques"):
        st.markdown("""
            > Every string tells a story — and Python helps us shape, search, and style it with ease.

            - Explore basic string operations like case conversion, slicing, and formatting.
            - Learn how to split, join, search, and replace text.
            - Use regular expressions for advanced replacements.
            - Count words, reverse strings, and extract initials.
            """)
        with st.expander("🔤 Case Conversion"):
            st.markdown("- Convert strings to uppercase, lowercase, and title case.")
            st.code("""
        text = "good morning"
        print(text.upper())    # GOOD MORNING
        print(text.lower())    # good morning
        print(text.title())    # Good Morning
        """, language="python")

        with st.expander("🔗 Splitting & Joining"):
            st.markdown("- Split strings into lists and join them back with custom separators.")
            st.code("""
        sentence = "Data Science is fun"
        words = sentence.split()  # ['Data', 'Science', 'is', 'fun']
        joined = "_".join(words)  # Data_Science_is_fun
        print(joined)
        """, language="python")

        with st.expander("🔍 Searching & Replacing"):
            st.markdown("- Find substrings and replace them with new values.")
            st.code("""
        text = "Welcome to Python programming"
        print(text.find("Python"))  # 11
        print(text.replace("Python", "JavaScript"))  # Welcome to JavaScript programming
        """, language="python")

        with st.expander("🧼 Trimming Whitespace"):
            st.markdown("- Remove leading and trailing spaces.")
            st.code("""
        text = "  Hello Sweden  "
        trimmed = text.strip()
        print(f"'{trimmed}'")  # 'Hello Sweden'
        """, language="python")

        with st.expander("🔢 Word Count & Initials"):
            st.markdown("- Count words and extract first letters of each word.")
            st.code("""
        text = "Python powers poetic dashboards"
        word_count = len(text.split())  # 4
        initials = ''.join([word[0] for word in text.split()])
        print(f"Word count: {word_count}")  # 4
        print(f"Initials: {initials}")      # Pppd
        """, language="python")

        with st.expander("📏 Length & Slicing"):
            st.markdown("- Measure string length and extract parts using slicing.")
            st.code("""
        text = "Finspång"
        print(len(text))      # 8
        print(text[2:6])      # nspå
        print(text[::-1])     # gnåpsniF
        """, language="python")

    with st.expander("📚 Collections"):
        st.markdown("- Lists, Tuples, Sets, Dictionaries")
        with st.expander("List – Ordered, Mutable, Allows Duplicates"):
            st.markdown("""
            - Lists maintain order and allow duplicates.
            - You can add, insert, remove, reverse, and pop items.
            """)
            with st.expander("Managing List Items"):
                st.code("""
                # List – Ordered, Mutable, Allows Duplicates
                books = ["Atomic Habits", "The Power of Now", "Mindset"]
                books.append("Atomic Habits")  # Adds a duplicate
                print(books)
                # ['Atomic Habits', 'The Power of Now', 'Mindset', 'Atomic Habits']
                
                books.insert(2, "Flow")  # Insert at index 2
                print(books)
                # ['Atomic Habits', 'The Power of Now', 'Flow', 'Mindset', 'Atomic Habits']
                
                books.remove("Atomic Habits")  # Removes first occurrence
                print(books)
                # ['The Power of Now', 'Flow', 'Mindset', 'Atomic Habits']
                
                print(books.index("Atomic Habits"))  #Output 3
                
                books.reverse()
                print(books)
                # ['Atomic Habits', 'Mindset', 'Flow', 'The Power of Now']
        
                books.pop()  # Removes last item
                print(books)
                # ['Atomic Habits', 'Mindset', 'Flow']    
                """, language="python")

            with st.expander("Working with Lists"):
               st.write("🔪 List Slicing, 🔁 List Iteration, 🔃 List Sorting")
               st.code("""
                books = ["Atomic Habits", "Mindset", "Flow", "Deep Work"]
                print(books[1:3])  # ['Mindset', 'Flow']
                """, language="python")

               st.code("""
               books = ["Atomic Habits", "Mindset", "Flow", "Deep Work"]
                for book in books:
                    print("Reading:", book)
                """, language="python")

               st.code("""
               books = ["Atomic Habits", "Mindset", "The Power of Now", "Flow"]
                books.sort()
                print(books)  # Alphabetical order
                books.sort(reverse=True) #descending order
                print(books)
                # ['The Power of Now', 'Mindset', 'Flow', 'Atomic Habits']
                              """, language="python")

        with st.expander("🧳 Tuple – Travel Itinerary"):
            st.markdown("- Tuples are ordered and immutable.\n- They allow duplicates and support indexing.")
            st.code("""
               itinerary = ("Paris", "Tokyo", "Berlin", "Tokyo", "Stockholm")
               print(itinerary.count("Tokyo"))  # 2
               print(itinerary.index("Berlin"))  # 2
               """, language="python")

        with st.expander("🍽️ Set – Recipes & Categories"):
            st.markdown("""
            - Sets remove duplicates and support union, intersection, and difference.
            - Useful for comparing recipe categories like desserts, beverages, brunch, and lunch.
            """)
            st.code("""
            brunch_items = {"pancakes", "avocado toast", "smoothie", "pancakes"}
            print(brunch_items)
            # {'smoothie', 'avocado toast', 'pancakes'} - duplicates removed
            
            brunch_items.add("omelette")
            print(brunch_items)
            # {'smoothie', 'avocado toast', 'pancakes', 'omelette'}
            
            brunch_items.remove("omelette")
            print(brunch_items)
            # {'smoothie', 'avocado toast', 'pancakes'}
            brunch_items.discard("waffles") # no error if item not found
    
            desserts = {"brownie", "ice cream", "pancakes"}
            beverages = {"smoothie", "coffee", "ice cream"}
    
            # Union – combine all unique items
            combined = desserts.union(beverages)
            print(combined)
            # {'brownie', 'coffee', 'ice cream', 'smoothie', 'pancakes'}
            
            combined = desserts | beverages
            print(combined)
            # {'brownie', 'coffee', 'ice cream', 'smoothie', 'pancakes'}
            
            # Intersection – common items
            common = desserts.intersection(beverages)
            print(common)
            # {'ice cream'}
            
            common = desserts & beverages
            print(common)
            # {'ice cream'}
            
            # Difference – items in desserts not in beverages
            difference = desserts.difference(beverages)
            print(difference)
            # {'brownie', 'pancakes'}
        """, language="python")
        with st.expander("🗂️ Dictionary – Person Profile"):
            st.markdown("""
           - Dictionaries store key-value pairs with no duplicate keys.
           - You can update, access, remove, and iterate through them.
           """)
            st.code("""
               recipe = {
                    "dish": "Masala Dosa",
                    "prep_time": "30 mins",
                    "ingredients": ["rice", "lentils", "potato", "spices"],
                    "vegetarian": True
                }
                
                print(recipe["dish"])  # 'Masala Dosa'
                
                recipe["prep_time"] = "35 mins"  # Update value
                print(recipe["prep_time"])  # '35 mins'
                
                recipe.update({"prep_time": "40 mins"})  # Upsert: updates if key exists
                print(recipe)
                # {'dish': 'Masala Dosa', 'prep_time': '40 mins', 'ingredients': [...], 'vegetarian': True}
                
                print(recipe.get("ingredients"))  
                # ['rice', 'lentils', 'potato', 'spices']
                
                print(recipe.keys())    
                # dict_keys(['dish', 'prep_time', 'ingredients', 'vegetarian'])
                
                print(recipe.values())  
                # dict_values(['Masala Dosa', '40 mins', [...], True])
                
                print(recipe.items())   
                # dict_items([('dish', 'Masala Dosa'), ('prep_time', '40 mins'), ...])
                
                print(recipe.pop("vegetarian"))  # True
                
                print(recipe)  
                # {'dish': 'Masala Dosa', 'prep_time': '40 mins', 'ingredients': [...]}
                
                print(recipe.popitem())  
                # ('ingredients', ['rice', 'lentils', 'potato', 'spices'])
                
                print(recipe)  # {'dish': 'Masala Dosa', 'prep_time': '40 mins'}
                
                recipe.update({"vegetarian": True})  # Re-add key
                print(recipe)  
                # {'dish': 'Masala Dosa', 'prep_time': '40 mins', 'vegetarian': True}
                """, language="python")

            st.markdown("""
               > Every journey has its details — and nested dictionaries help us track them all.
               - Each flight ID maps to a dictionary of passenger details.
               - You can access nested values using two keys: outer ID and inner field.
               """)
            st.code("""
                   flights = {
                   "FL001": {
                       "passenger": "Anika",
                       "origin": "Stockholm",
                       "destination": "London",
                       "fare": 8200.00,
                       "status": "confirmed"
                   },
                   "FL002": {
                       "passenger": "Ravi",
                       "origin": "Chennai",
                       "destination": "Delhi",
                       "fare": 5600.00,
                       "status": "cancelled"
                       }
                }
                
                print(flights["FL001"]["destination"])  # London
                print(flights["FL002"]["fare"])         # 5600.0
        """, language="python")

    with st.expander("🧠 Control Flow "):
        st.markdown(
            """ > Control flow is the storyteller — deciding which chapter to read, when to repeat a scene, and how to skip the boring bits.            
            - Use `if-elif-else` to guide decisions. 
            - Use `for` and `while` loops to repeat actions. 
            - Handle errors gracefully with `try-except-finally`. """)
        st.code("""
            temperature = 12
            if temperature < 0:
                print("Freezing weather ❄️")
            elif temperature < 20:
                print("Cool day 🌥️")
            else:
                print("Warm and sunny ☀️")
            
            fruits = ["mango", "banana", "apple"]
            for fruit in fruits:
                print(f"I love {fruit}")
            print(fruits.count("apple"))
            
            countdown = 3
            while countdown > 0:
                print(f"Launching in {countdown}...")
                countdown -= 1
                
            for num in range(6):
                if num == 5:
                    break
                if num % 2 == 0:
                    continue
                print(f"Odd number: {num}")
                
            try:
                result = 10 / 0
            except ZeroDivisionError:
                print("Cannot divide by zero!")
            else:
                print("Division successful")
            finally:
                print("Cleanup complete")
    
            """, language = "python")

    with st.expander("🧪 Python Foundations Quiz"):
        st.markdown("> Choose your answers and click Submit to see your score!")

        q1 = st.radio("1. What does `text[::-1]` do?",
                      ["Uppercase", "Whitespace", "Split", "Reverse"], key="q1")
        q2 = st.radio("2. Which type removes duplicates?",
                      ["Tuple", "List", "Set", "Dictionary"], key="q2")
        q3 = st.radio("3. What is `if age < 18:`?",
                      ["Condition", "Function", "Exception", "Loop"], key="q3")

        if st.button("Submit"):
            score = 0
            if q1 == "Reverse":
                score += 1
                st.success("🏆 Q1 Correct!")
            else:
                st.warning("Q1 Incorrect. Correct Answer : Reverse")

            if q2 == "Set":
                score += 1
                st.success("🏆 Q2 Correct!")
            else:
                st.warning("Q2 Incorrect. Correct Answer : Set")

            if q3 == "Condition":
                score += 1
                st.success("🏆 Q3 Correct!")
            else:
                st.warning("Q3 Incorrect. Correct Answer : Condition")

            st.markdown(f"### 🎯 Final Score: **{score}/3**")
            if score == 3:
                st.balloons()

    with st.expander("🎨 Interactive String Playground"):
        st.markdown("""
            > Type a word, a phrase, or a poetic line — and let Python reveal its shape, size, and rhythm.

            - See your input reversed, counted, and stylized.
            - A gentle way to explore string methods with your own creativity.
            """)

        user_input = st.text_input("Enter your text here:")

        if user_input:
            st.write(f"🔁 Reversed: `{user_input[::-1]}`")
            st.write(f"🔢 Length: `{len(user_input)}`")
            st.write(f"🔤 Uppercase: `{user_input.upper()}`")
            st.write(f"🔡 Lowercase: `{user_input.lower()}`")
            st.write(f"🧼 Trimmed: `{user_input.strip()}`")
            st.write(f"🅰️ Initials: `{''.join([word[0] for word in user_input.split() if word])}`")

elif active_section == "Advanced Concepts":
    st.header("🚀 Functional & Advanced Python")
    with st.expander(" ⚡ Functional Programming in Python"):
        st.markdown("""
        > Functional programming emphasizes pure functions, immutability, and elegant composition.
        - Lambda expressions    
        - Higher-order functions
        - Map, filter, reduce  
        - Closures, partials, composition, recursion
        """)
        with st.expander("Lambda, Higher-order functions, Map, filter, reduce"):
            st.markdown("> Lambda Expressions – Tiny Anonymous Functions")
            st.code("""
            square = lambda x: x * x
            print(square(4))  # 16
    
            add = lambda a, b: a + b
            print(add(3, 5))  # 8
            """, language="python")

            st.markdown("> Higher-Order Functions – Functions That Accept Functions")
            st.code("""
            def shout(text):
                return text.upper()
    
            def whisper(text):
                return text.lower()
    
            def greet(style, name):
                return style(f"Hello {name}")
    
            print(greet(shout, "Katham"))   # HELLO KATHAM
            print(greet(whisper, "Katham")) # hello katham
            """, language="python")

            st.markdown("> Map, Filter, Reduce – Functional Tools for Collections")
            st.code("""
            from functools import reduce
    
            numbers = [1, 2, 3, 4, 5]
            squares = list(map(lambda x: x * x, numbers))
            print(squares)  # [1, 4, 9, 16, 25]
    
            evens = list(filter(lambda x: x % 2 == 0, numbers))
            print(evens)  # [2, 4]
    
            total = reduce(lambda x, y: x + y, numbers)
            print(total)  # 15
            """, language="python")

        with st.expander("Closures, partials, composition, recursion"):
            st.markdown(""" > Compose  
                - Function composition combines multiple functions into one 
                - passing output from one as input to the next.
                - Use case: Clean chaining of transformations, especially in data pipelines or functional chains
                 """)
            st.code("""
            def strip_whitespace(text):
                return text.strip()
    
            def capitalize_words(text):
                return text.title()
    
            def compose(f, g):
                return lambda x: f(g(x))
    
            # Compose: first strip, then capitalize
            format_name = compose(capitalize_words, strip_whitespace)
    
            raw_input = "   Hello World   "
            print(format_name(raw_input))  # Hello World
            """, language="python")

            st.markdown(""" > Closure 
                - Function that remembers variables from its enclosing scope even after that scope has finished.
                """)

            st.code("""
            def outer(msg):
                def inner():
                    return f"Message is : {msg}"
                return inner
    
            greet = outer("Good Morning")
            print(greet())  # Message is : Good Morning
            """, language="python")

            st.markdown(""" > Partial Functions
                - Fix some arguments of a function using `functools.partial`.
                """)
            st.code("""
               from functools import partial
               def calculate_shipping(weight, rate_per_kg):
                    return weight * rate_per_kg
                
                # Fix the rate for express shipping
                express_shipping = partial(calculate_shipping, rate_per_kg=50)  
                print(express_shipping(2))  # 100
                """, language="python")

            st.markdown("""  > Callback Functions
                - Pass a function as an argument to be executed later.
                """)
            st.code("""
                def on_button_click(callback):
                    print("Button was clicked")
                    callback()
    
                def show_message():
                    print("Hello World")
    
                on_button_click(show_message)
        """)
            st.markdown("""  > Recursive Functions
                - A function that calls itself to solve smaller versions of a problem.
            """)
            st.code("""
                def factorial(n):
                    if n == 1:
                        return 1
                    return n * factorial(n - 1)
    
                print(factorial(5))  # 120
                """, language="python")


    with st.expander("🔄 Iterators & 🌱 Generators – Lazy Elegance"):
        st.markdown("""
        > Loops repeat. Iterators remember. Generators whisper one value at a time.

        Python provides powerful tools for working with sequences:
        - **Iterators**: Objects that remember their state and return items one at a time using `next()`.
        - **Generators**: Special functions that yield values lazily, perfect for large or infinite sequences.
        """)
        st.markdown("Manual Iterator with `iter()` and `next()`")
        st.code("""
            numbers = [10, 20, 30]
            iterator = iter(numbers)
        
            print(next(iterator))  # 10
            print(next(iterator))  # 20
            print(next(iterator))  # 30
            # next(iterator) now would raise StopIteration
            """, language="python")

        st.markdown("Custom Iterator Class")
        st.code("""
            class Countdown:
                def __init__(self, start):
                    self.current = start
        
                def __iter__(self):
                    return self
        
                def __next__(self):
                    if self.current == 0:
                        raise StopIteration
                    self.current -= 1
                    return self.current + 1
        
            for num in Countdown(5):
                print(num)  # 5 4 3 2 1
            """, language="python")

        st.markdown("Generator Function – Yielding One by One")
        st.code("""
            # Regular function: returns all values at once
            def get_numbers(n):
                return [i for i in range(n)]
        
            print(get_numbers(5))  # [0, 1, 2, 3, 4]
        
            # Generator function: yields values one at a time
            def get_numbers(n):
                for i in range(n):
                    yield i

            print(get_numbers(5))  # <generator object ...>

            for number in get_numbers(5):
                print(number)  # 0 1 2 3 4
        """, language="python")
        st.success("🎉 Iterators and Generators section complete!")
    with st.expander("🧪 Quiz: Functional Programming & Lazy Iteration"):
        st.markdown(
            "> This short quiz explores concepts like lambdas, higher-order functions, iterators, and generators.")

        q1 = st.radio("1. What does a lambda function return?",
                      ["A loop", "An anonymous function", "A list", "A generator"], key="fp_q1")
        q2 = st.radio("2. Which tool yields values one at a time?",
                      ["List", "Tuple", "Generator", "Set"], key="fp_q2")
        q3 = st.radio("3. What does `next()` do with an iterator?",
                      ["Creates a loop", "Returns the last item", "Returns the next item", "Stops the iteration"],
                      key="fp_q3")

        if st.button("Submit Functional Quiz"):
            score = 0
            if q1 == "An anonymous function":
                score += 1
                st.success("✅ Q1 Correct!")
            else:
                st.warning("❌ Q1 Incorrect. Correct Answer: An anonymous function")

            if q2 == "Generator":
                score += 1
                st.success("✅ Q2 Correct!")
            else:
                st.warning("❌ Q2 Incorrect. Correct Answer: Generator")

            if q3 == "Returns the next item":
                score += 1
                st.success("✅ Q3 Correct!")
            else:
                st.warning("❌ Q3 Incorrect. Correct Answer: Returns the next item")

            st.markdown(f"###  Score: **{score}/3**")
            if score == 3:
                st.balloons()

elif active_section == "OOP":
    st.header("🧱 Object-Oriented Programming")

    with st.expander("📦 Classes & Objects"):
        st.markdown("""
        > Classes are blueprints. Objects are the buildings.

        - Define reusable structures with attributes and behaviors.
        - Create multiple instances with unique data.
        """)
        st.code("""
            class Person:
                def __init__(self, name):
                    self.name = name
        
                def greet(self):
                    return f"Hello, I am {self.name}"
        
            p1 = Person("Kathambari")
            print(p1.greet())  # Hello, I am Kathambari
    """, language="python")

    with st.expander("🔐 Encapsulation"):
        st.markdown("""
            > Hide internal details. Expose only what’s needed.
    
            - Use underscores to signal private attributes.
            - Protect data from unintended access.
        """)
        st.code("""
            class BankAccount:
                def __init__(self, balance):
                    self._balance = balance  # protected
        
                def deposit(self, amount):
                    self._balance += amount
        
                def get_balance(self):
                    return self._balance
        
            acc = BankAccount(1000)
            acc.deposit(500)
            print(acc.get_balance())  # 1500
    """, language="python")

    with st.expander("🧬 Inheritance & Method Overriding"):
        st.markdown("""
            > Inherit traits. Override behavior.
    
            - Reuse code from a parent class.
            - Customize methods in child classes.
        """)
        st.code("""
            class Animal:
                def speak(self):
                    return "Some sound"
        
            class Dog(Animal):
                def speak(self):
                    return "Woof!"
        
            pet = Dog()
            print(pet.speak())  # Woof!
    """, language="python")

    with st.expander("🧪 Abstract Classes"):
        st.markdown("""
            > Define a contract. Let subclasses implement it.
    
            - Use `abc` module and `@abstractmethod`.
            - Prevent direct instantiation.
        """)
        st.code("""
            from abc import ABC, abstractmethod
        
            class Shape(ABC):
                @abstractmethod
                def area(self):
                    pass
        
            class Circle(Shape):
                def __init__(self, radius):
                    self.radius = radius
        
                def area(self):
                    return 3.14 * self.radius * self.radius
        
            c = Circle(5)
            print(c.area())  # 78.5
    """, language="python")

    with st.expander("🔑 Access Modifiers"):
        st.markdown("""
            > Control visibility with naming conventions.
    
            - `public`: no underscore  
            - `_protected`: single underscore  
            - `__private`: double underscore
            """)
        st.code("""
            class Demo:
                def __init__(self):
                    self.name = "Public"
                    self._age = 30
                    self.__secret = "Hidden"
        
            obj = Demo()
            print(obj.name)       # Public
            print(obj._age)       # 30
        # print(obj.__secret) # Error: not accessible
    """, language="python")

    # Poetic summary
    with st.expander("🌟 Poetic Summary"):
        st.markdown("""
            > In Object-Oriented Programming, every class is a character,  
            > every method a voice, and every object a story waiting to unfold.  
            > You shape behavior, protect secrets, and pass down traits —  
            > like crafting a lineage of logic with elegance and intent.
            """)

elif active_section == "Practical Python":
    st.header("🗂️ System & Data Utilities")
    with st.expander("🔧 File Handling & Logging"):
        st.markdown("""
            > Files hold memory. Logs tell stories.

             File Modes
            - `r` : Read (file must exist)  
            - `w` : Write (creates or overwrites)  
            - `a` : Append (adds to end)  
            - `r+`, `w+`, `a+` : Read + Write variants  
            - `rb`, `wb`, `ab` : Binary modes
            """)

        st.markdown("✍️ Writing & Reading a Text File")
        st.code("""
            #
            Write to a file
            with open("journal.txt", "w") as file:
                file.write("Dear Kathambari\n")
                file.write("Today we explored file handling in Python.")

            #Read the file
            with open("journal.txt", "r") as file:
                content = file.read()
                print(content)
        """, language="python")

        st.markdown("➕ Appending & Line-by-Line Reading")
        st.code("""
                    #
                    Append a new entry
        with open("journal.txt", "a") as file:
            file.write("Adding one more thought...\n")

        # Read line by line
        with open("journal.txt", "r") as file:
            for line in file:
                print(line.strip())
                    """, language="python")

        st.markdown(" 🔍 Searching for Keywords")
        st.code("""
                with open("journal.txt", "r") as file:
                    for line in file:
                    if "thought" in line:
                    print("Found keyword:"
                   , line.strip())
            """, language="python")

    with st.expander("📑 CSV File Input & Handling"):
            st.markdown("""
            > CSV files are simple tables — rows of data separated by commas.

            📥 Writing a Sample CSV File
            Let's first create a sample CSV file to work with.
            """)
            st.code("""
        import csv

        # Create a sample CSV file
        with open("people.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "city"])
            writer.writerow(["Geetha", "28", "London"])
            writer.writerow(["David", "30", "Venice"])
            writer.writerow(["Elin", "25", "Mumbai"])
        """, language="python")

            st.markdown("📖 Reading CSV with `DictReader`")
            st.code("""
        import csv

        with open("people.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["name"], "-", row["age"])
        """, language="python")

            st.markdown("🔍 Reading Specific Columns (Skipping Header)")
            st.code("""
            with open("people.csv", "r") as file:
                lines = file.readlines()
                for line in lines[1:]: # Skip header
                columns = line.strip().split(",")
                print(columns[2]) # Print city
                    """, language="python")

    with st.expander("📜 Logging"):
            st.markdown("Logging – Tracking Events Gracefully")
            st.code("""
        import logging

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='activity.log',
            filemode='w'
        )

        def greet_user(name):
            logging.info(f"Greeting user: {name}")
            if name:
                message = f"Hello, {name}!"
                logging.debug(f"Greeting message: {message}")
                return message
            else:
                logging.warning("No name provided.")
                return "Hello, guest!"

        print(greet_user("Kathambari"))
        print(greet_user(""))
        """, language="python")

            st.success(
                "🎉 File handling and logging section complete — Unlocked the power of persistence and traceability!")

    with st.expander("🧮 Databases"):
        st.markdown("""           
            Example – Student Marks Management
            > Connect, insert, calculate, and export — a full cycle of data management using PyMySQL.

            This example:
            - Connects to a MySQL database
            - Creates a `students` table
            - Inserts multiple rows of marks
            - Calculates average marks per student
            - Writes the results to a text file
            """)

        st.code("""
        import pymysql.cursors

        # Step 1: Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='school_db',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                # Step 2: Create a table
                create_query = '''
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    subject VARCHAR(100),
                    marks INT
                );
                '''
                cursor.execute(create_query)

                # Step 3: Insert data
                insert_query = "INSERT INTO students (name, subject, marks) VALUES (%s, %s, %s)"
                values = [
                    ("Anjali", "Math", 85),
                    ("Ravi", "Science", 78),
                    ("Meera", "English", 92),
                    ("Ravi", "Math", 88),
                    ("Anjali", "Science", 90)
                ]
                cursor.executemany(insert_query, values)

                # Step 4: Fetch and process data
                select_query = "SELECT name, AVG(marks) as average_marks FROM students GROUP BY name"
                cursor.execute(select_query)
                result = cursor.fetchall()

                # Step 5: Write to file
                with open("student_averages.txt", "w") as file:
                    for row in result:
                        file.write(f"{row['name']} - Average Marks: {row['average_marks']:.2f}\\n")

        except Exception as e:
            print("Error occurred:", e)
        finally:
            connection.commit()
        """, language="python")
        st.success("🎉 MySQL example complete — you've created, calculated, and captured student insights!")

elif active_section == "Automation & Pipelines":
    st.header("⏱️ Automation & ETL Concepts")
    with st.expander("Time-Based Trigger – `while True` + `cron`"):
        st.markdown("""
        This example:
        - Runs a task every 15 seconds using `while True` and `time.sleep()`
        - Logs system uptime to a file
        - Can be scheduled using `crontab -e` for long-running background automation

        > A great way to simulate polling, monitoring, or periodic logging.
        """)

        st.code("""
    # uptime_logger.py

    import time
    import os

    def task():
        uptime = os.popen("uptime").read().strip()
        with open("/home/kathambari/airflow/uptime_log.txt", "a") as f:
            f.write(f"Uptime: {uptime}\\n")
        print("Logged uptime:", uptime)

    while True:
        task()
        time.sleep(15)  # Run every 15 seconds
    """, language="python")

        st.markdown("### Schedule with Cron (Ubuntu)")
        st.code("""
    # Open crontab
    crontab -e

    # Add this line to run the script at reboot
    @reboot /usr/bin/python3 /home/kathambari/airflow/uptime_logger.py
    """, language="bash")

        st.markdown("""
        - `@reboot` runs the script once when the system starts  
        - You can also use `* * * * *` format for timed execution  
        - Make sure the script is executable and paths are correct
        """)

        st.warning("⚠️ This script runs infinitely — use Ctrl+C to stop it manually if needed.")

    with st.expander("ETL Basics"):
        st.markdown("- Extract, Transform, Load\n- Data cleaning & pipeline design\n- Workflow automation with Airflow")

        with st.expander("`transform_quotes.py` – Extract & Transform Logic"):
            st.markdown("""
            - Extracts quotes from an API  
            - Transforms them by adding `length` and `mood`  
            - Saves both raw and transformed CSVs
            """)
            st.code("""
    import pandas as pd
    import requests

    def extract_quotes():
        response = requests.get("https://api.quotable.io/quotes?limit=10", verify=False)
        data = response.json()
        quotes = pd.DataFrame(data['results'])
        quotes.to_csv('/home/kathambari/airflow/quotes_raw.csv', index=False)

    def transform_quotes():
        df = pd.read_csv('/home/kathambari/airflow/quotes_raw.csv')
        df['length'] = df['content'].apply(len)

        def tag_mood(text):
            length = len(text)
            if length < 80:
                return 'short & punchy'
            elif length < 160:
                return 'reflective'
            else:
                return 'deep & poetic'

        df['mood'] = df['content'].apply(tag_mood)
        df.to_csv('/home/kathambari/airflow/quotes_transformed.csv', index=False)
        print("Quotes transformed and saved.")

    if __name__ == "__main__":
        extract_quotes()
        transform_quotes()
    """, language="python")

        with st.expander("`quotes_wrapper.sh` – Manual Trigger Script"):
            st.markdown("Runs both the DAG and transformation script manually.")
            st.code("""
    #!/bin/bash
    python3 /home/kathambari/airflow/dags/extract_quotes_dag.py
    python3 /home/kathambari/transform_quotes.py
    """, language="bash")

        with st.expander(" `extract_quotes_dag.py` – Airflow DAG Definition"):
            st.markdown("""
            - Defines the DAG and task dependencies  
            - Uses `PythonOperator` to run extract and transform functions  
            - Scheduled to run every 5 minutes
            """)
            st.code("""
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime, timedelta
    import sys
    sys.path.append('/home/kathambari')
    from transform_quotes import extract_quotes, transform_quotes

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }

    dag = DAG(
        dag_id="extract_quotes_dag",
        default_args=default_args,
        start_date=datetime(2025, 10, 1),
        schedule_interval=timedelta(minutes=5),
        catchup=False
    )

    extract_task = PythonOperator(
        task_id='extract_quotes',
        python_callable=extract_quotes,
        dag=dag,
    )

    transform_task = PythonOperator(
        task_id='transform_quotes',
        python_callable=transform_quotes,
        dag=dag,
    )

    extract_task >> transform_task
    """, language="python")

elif active_section == "NumPy Fundamentals":
    with st.expander("🧮 NumPy Fundamentals"):
        st.markdown("""
        This module covers:
        - One-dimensional and multi-dimensional arrays
        - Built-in NumPy methods (`rand`, `randint`, `arange`, `eye`, `ones`, `zeros`)
        - Mathematical operations (`sqrt`, `exp`, `sum`, `broadcasting`)
        - Array slicing, indexing, and conditional selection
    
        > NumPy blends C-level speed with Pythonic syntax — ideal for data science, ML, and numerical computing.
        """)

        st.code("""
    import numpy as np
    
    # Array creation
    list_1 = [50, 60, 80, 100, 200, 300, 500, 600]
    my_array_items = np.array(list_1)
    my_matrix = np.array([[2,3,4], [5,6,7]])
    
    # Random generation
    np.random.rand(10)
    np.random.randint(1, 50, 5)
    np.ones((2,2))
    np.zeros(3)
    
    # Math operations
    x = np.arange(1, 10)
    y = np.arange(1, 10)
    sum = x + y
    squared = x ** 2
    sqrt = np.sqrt(squared)
    exp = np.exp(x)
    
    # Slicing and indexing
    my_random_array = np.random.randint(1, 10, 15)
    my_random_array[0:5] = 7
    my_2d_array = np.random.randint(1,10, (4,4))
    
    # Conditional selection
    matrix[matrix < 0] = 0
    matrix[matrix % 2 == 1] = -2
    """, language="python")
        st.markdown("Try replacing `input()` with `st.number_input()` if you want to make this interactive in Streamlit.")
elif  active_section == "Testing Modules":
    with st.expander("🧪 Python Testing Basics"):
        st.markdown("""
            Testing is the process of verifying that your code behaves as expected — reliably, safely, and correctly.
            In Python, testing can be as simple as using `assert` statements to check logic, or as advanced as using frameworks like `pytest`, `unittest`, or `doctest`.

            This section includes:
            - ✅ Basic assertion tests (e.g., string reversal, even number check)
            - 🚨 Exception handling tests (e.g., divide-by-zero)
            - 🔍 Edge case validation (e.g., empty strings, negative numbers)
            - 🧩 Core logic testing (custom functions like `multiply`, `is_palindrome`, etc.)
            """)
        with st.expander("String Reversal Test"):
            st.markdown("""
            - Tests a function that reverses a string  
            - Uses `assert` to validate expected output  
            - Great for understanding string slicing and basic testing
            """)
            st.code("""
        # string_logic.py
        def reverse_string(s):
            return s[::-1]

        # test_string_logic.py
        from string_logic import reverse_string

        def test_reverse_string():
            assert reverse_string("hello") == "olleh"

        test_reverse_string()
        """, language="python")

        with st.expander("Even Number Test"):
            st.markdown("""
            - Checks if a number is even  
            - Introduces modulus operator `%`  
            - Simple logic with clear pass/fail behavior
            """)
            st.code("""
        # number_logic.py
        def is_even(n):
            return n % 2 == 0

        # test_number_logic.py
        from number_logic import is_even

        def test_is_even():
            assert is_even(4) == True
            assert is_even(7) == False

        test_is_even()
        """, language="python")
        with st.expander("Palindrome Checker Test"):
            st.markdown("""
            - A palindrome is a word or phrase that reads the same backward as forward  
            - This test checks if the function correctly identifies palindromes  
            - Great for practicing string logic and conditionals
            """)

            st.code("""
        # palindrome_logic.py
        def is_palindrome(s):
            return s == s[::-1]
        """, language="python")

            st.code("""
        # test_palindrome_logic.py
        from palindrome_logic import is_palindrome

        def test_is_palindrome():
            assert is_palindrome("madam") == True
            assert is_palindrome("hello") == False

        test_is_palindrome()
        """, language="python")
        with st.expander("Test for exception handling"):
            st.markdown("""
            **Purpose:**  
            To verify that accessing a non-existent key in a dictionary raises a `KeyError`, and that the error is properly handled using `try-except`.
            """)
            st.code("""
            #test for exception handling
            def test_key_error():
                try:
                    profile = {"name": "Kathambari"}
                    print(profile["age"])  # Key doesn't exist
                    assert False  # Should not reach this line
                except KeyError:
                    assert True
            """, language="python")

elif active_section == "Currently Exploring":
    with st.expander("🚧 Currently Exploring"):
        st.markdown("""
        - Flask – building routes, handling requests, and serving dynamic content
        - PyTorch – exploring tensors, gradients, and model training for data science workflows   
         """)
        st.code("""
        # app.py

        from flask import Flask
        
        app = Flask(__name__)
        
        @app.route('/')
        def home():
            return "Flask Web App Loaded Successfully!"
        
        if __name__ == '__main__':
            app.run(debug=True)

        """, language="python")
        st.code("""
            # pytorch_intro.py

            import torch

            # Create a tensor
            x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)

            # Perform operations
            y = x * 2 + 1
            z = y.mean()

            # Backpropagate
            z.backward()

            # Print gradients
            print(x.grad)
            """, language="python")

# Footer
st.markdown("---")
st.caption("✨ Built with Streamlit | Inspired by real-world backend workflows")




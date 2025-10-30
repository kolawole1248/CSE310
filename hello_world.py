"""
Hello World Program
A simple demonstration of basic Python programming concepts
"""

import datetime

def greet_user():
    """Greet the user with a personalized message"""
    print("=" * 50)
    print("🌟 Welcome to the Enhanced Hello World Program! 🌟")
    print("=" * 50)
    
    # Get user input
    name = input("What's your name? ").strip()
    
    if not name:
        name = "World"
    
    # Get current time
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    # Determine appropriate greeting based on time of day
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    elif 17 <= hour < 21:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    
    # Display personalized greeting
    print(f"\n{greeting}, {name}!")
    print(f"📅 Today is {current_time.strftime('%A, %B %d, %Y')}")
    print(f"⏰ Current time: {current_time.strftime('%I:%M %p')}")  # FIXED: Removed extra parenthesis
    
    return name

def display_ascii_art():
    """Display some ASCII art for visual appeal"""
    print("\n" + "✨" * 25)
    print("""
    ╔══════════════════════════════╗
    ║                              ║
    ║        HELLO WORLD!          ║
    ║                              ║
    ║    From a future software    ║
    ║          engineer!           ║
    ║                              ║
    ╚══════════════════════════════╝
    """)
    print("✨" * 25)

def count_characters(text):
    """Count characters in the given text"""
    return len(text)

def main():
    """Main function to run the Hello World program"""
    try:
        # Greet the user and get their name
        user_name = greet_user()
        
        # Display ASCII art
        display_ascii_art()
        
        # Demonstrate basic programming concepts
        print(f"\n📊 Let me analyze your name '{user_name}':")
        print(f"   • Your name has {count_characters(user_name)} characters")
        print(f"   • In uppercase: {user_name.upper()}")
        print(f"   • In lowercase: {user_name.lower()}")
        
        # Create a list and demonstrate looping
        languages = ["Python", "JavaScript", "Java", "C++", "Rust"]
        print(f"\n💻 Programming languages I'm interested in learning:")
        for i, language in enumerate(languages, 1):
            print(f"   {i}. {language}")
        
        # Simple calculation
        a, b = 7, 3
        print(f"\n🧮 Quick math demonstration:")
        print(f"   {a} + {b} = {a + b}")
        print(f"   {a} * {b} = {a * b}")
        
        # Farewell message
        print(f"\n🎉 Thank you for trying my Hello World program, {user_name}!")
        print("🚀 This is just the beginning of my programming journey!")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print(f"\n\n👋 Thanks for stopping by! Have a great day!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

# Check if this file is being run directly
if __name__ == "__main__":
    main()  # FIXED: Removed extra parenthesis
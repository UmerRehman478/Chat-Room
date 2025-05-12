# 🐼 Panda-Chat – A Fun Themed Chatroom

This project is a panda-themed real-time chatroom built using Python's socket programming. Users can chat, send fun commands, and receive random panda facts, all while interacting in a cute and creative environment.

---

## 💬 What It Does

- Lets multiple users join the same chatroom at once.
- Broadcasts everyone's messages to all participants with fun panda decorations like emojis and puns.
- Includes special commands:
  - `@bamboo`: Get a random panda fact.
  - `@grove`: See who else is in the chat.
  - `@leaves`: Exit the chatroom peacefully.

---

## 🐼 Key Features

### Server
- Accepts connections from multiple clients at the same time (multithreaded).
- Broadcasts every message to all connected users.
- Adds random panda emojis, puns, or decorations to messages.
- Recognizes and handles the three special commands mentioned above.
- Logs interactions (can be extended to generate a server log file).

### Client
- Connects to the chatroom server using TCP.
- Lets each user pick a panda-themed name.
- Allows sending and receiving messages in real time.
- Supports fun commands (`@bamboo`, `@grove`, `@leaves`).
- Gracefully disconnects when the user exits.

---

## 🛠 How to Run

1. **Install Python 3**

   Make sure you have Python 3 installed. You can get it from https://www.python.org

2. **Open Two Terminals**

   In one terminal, run the server:
   ```bash
   python server.py
   ```

   In another terminal, run the client:
   ```bash
   python client.py
   ```

   You can open more terminals and run more `client.py` instances to simulate multiple users.

3. **Choose Your Panda Name**

   Each client will be asked to pick a name when connecting. This name will be shown in the chat.

4. **Start Chatting!**

   Type messages and see them broadcasted with panda-themed style.
   You can also type these commands:
   - `@bamboo`: Get a cool panda fact!
   - `@grove`: See who else is connected.
   - `@leaves`: Leave the chat politely.

---

## 🐾 Example Panda Features

Here are some fun panda facts you might get with `@bamboo`:

```
- Pandas spend around 14 hours a day eating bamboo!
- Baby pandas are born pink and weigh only about 100 grams!
- A group of pandas is called an embarrassment!
- Pandas can swim and are excellent tree climbers!
- There are only about 1,800 giant pandas left in the wild.
```

And here are some emojis used:
```
🐼 🎋 🍃 🐾 🌿
```

---

## 🧪 Example Interaction

```
[PandaLover] 🐼: Hello everyone!
[BambooFan] 🎋: @bamboo
Server: 🐾 Did you know? Pandas spend around 14 hours a day eating bamboo!
[PandaLover] 🐼: @grove
Server: Connected pandas: PandaLover, BambooFan
[BambooFan] 🎋: @leaves
Server: Goodbye BambooFan 🐼! See you next time!
```

---

## 📁 File Structure

```
project-folder/
├── server.py         # Server-side chatroom code
├── client.py         # Client-side chatroom code
├── README.md         # This file
```

---

## 🔧 Notes

- Use threading on the server to handle multiple users.
- Use lists to manage connected users and store panda facts.
- Handle client disconnections without crashing the server.
- Add more panda facts or decorations for extra fun (ASCII art, colors, sounds, etc.).
- This runs on the command line (no GUI required).

---

## 🧠 Fun Tips (Optional Add-Ons)

- Add ASCII panda art when someone joins or leaves.
- Let users vote on favorite panda fact.
- Track how many times a fact was requested.
- Show time stamps in chat messages.

---

Let’s make chatting as adorable as a panda munching on bamboo! 🐼🎋

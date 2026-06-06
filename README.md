# 🧪 Ursina Chemistry Lab Simulator

A 3D Chemistry Laboratory simulation built using the **Ursina Game Engine** and **MySQL authentication**. This project allows users to sign up, log in, and explore an interactive virtual chemistry laboratory with realistic lighting, sound effects, and laboratory equipment.

---

## 📌 Features

- 🔐 User Authentication System
  - Sign Up
  - Login
  - MySQL Database Integration

- 🎮 First-Person Exploration
  - Smooth FPS controls using Ursina's `FirstPersonController`

- 🧪 Laboratory Environment
  - Laboratory tables
  - Bunsen burners
  - Test tube stands
  - Chemical containers
  - Shelves and equipment

- 💡 Dynamic Lighting
  - Ambient lighting
  - Directional lighting
  - Emergency power mode

- 🔊 Audio Effects
  - Background ambience
  - Siren system
  - Button click sounds
  - Power activation sounds

- 🚪 Interactive Login & Signup Portals


---

## 🛠 Requirements

### Python Packages

Install the required dependencies:

```bash
pip install ursina
pip install mysql-connector-python
```

---

## 🗄 MySQL Setup

Make sure MySQL Server is installed and running.

Update the database credentials inside the script:

```python
db = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password'
}
```

The game automatically creates:

```sql
DATABASE ursina
```

and

```sql
TABLE auth (
    username VARCHAR(60) PRIMARY KEY,
    password VARCHAR(50)
)
```

---

## 📂 Assets Folder Structure

```text
project/
│
├── main.py
├── assets/
│   ├── rift.glb
│   ├── table.glb
│   ├── bunsen_burner.glb
│   ├── testubes.glb
│   ├── hologram.glb
│   ├── bottles.glb
│   ├── canister.glb
│   ├── o2.glb
│   ├── gas.glb
│   ├── wall.jpeg
│   ├── auth.jpg
│   ├── click.wav
│   ├── abg.mp3
│   ├── main_v.mp3
│   ├── main_a.mp3
│   ├── charge.mp3
│   └── mbg.mp3
│
└── README.md
```

---

## 🎮 Controls

| Key | Action |
|------|---------|
| W A S D | Move |
| Mouse | Look Around |
| Space | Jump |
| E | Interact |
| B | Change Light Color |
| ESC | Exit Game |

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/your-username/ursina-chemistry-lab.git
```

Navigate to the project folder:

```bash
cd ursina-chemistry-lab
```

Run the game:

```bash
python main.py
```

---

## 🎯 Gameplay Flow

1. Launch the game.
2. Enter the credential room.
3. Choose:
   - Login
   - Sign Up
4. Create an account or log in.
5. Enter the chemistry laboratory.
6. Activate the power system.
7. Explore the lab and interact with objects.

---

## ⚠️ Important Notes

- Ensure MySQL Server is running before launching the game.
- All required asset files must be present in the `assets` directory.
- The default database password in the source code should be changed before deployment.
- Passwords are currently stored in plain text. For production use, implement password hashing.

---

## 🔒 Future Improvements

- Password encryption using bcrypt
- Save user progress
- Chemistry experiments and reactions
- Multiplayer support
- Inventory system
- Quest and learning modules
- Improved UI/UX

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed using Python, Ursina Engine, and MySQL.

If you found this project useful, consider giving it a ⭐ on GitHub.

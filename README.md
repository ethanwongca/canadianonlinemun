# Canadian Online Model United Nations (COMUN)

![COMUN LinkedIn](https://github.com/user-attachments/assets/2b8feb6f-9209-4d28-beac-db9e26513156)

Welcome to the technical repository for the **Canadian Online Model United Nations** (COMUN). COMUN is one of the first virtual and free Model United Nations, recognized with **2 x Special Mentions** from the **United Nations High Commissioner for Refugees (UNHCR)** MUN Refugee Challenge. We have successfully hosted over **300 delegates** from **37 countries** worldwide.

📂 **Awards**: UNHCR awards can be found in the [**awards folder**](./Awards).  
📂 **Letters**: COMUN-related letters are available in the COMUN letters folder.

---

## 🌐 Connect with Us
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/canadianonlinemun)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/canadianonlinemun/?hl=en)

---

## 📋 Table of Contents

- [Languages and Libraries](#-languages-and-libraries)
- [Discord Bots](#-discord-bots)
- [Website](#-website)
- [Usage](#-usage)

---

## 🛠 Languages and Libraries

### **Bots:**

- **[Python 3](https://www.python.org/doc/)**: The primary programming language used for developing the bots due to its simplicity and extensive libraries.
- **[Discord.py (v1.7.3)](https://discordpy.readthedocs.io/en/stable/)**: A Python library used for interacting with the Discord API. It provides an easy way to create bots that can communicate with users on Discord servers.
- **[Asyncio](https://docs.python.org/3/library/asyncio.html)**: Used for writing concurrent code with the async/await syntax. It is essential for handling multiple tasks, such as processing user commands and responding to them in real-time.
- **[Nest_asyncio](https://github.com/erdewit/nest_asyncio)**: A small Python library that allows asyncio to be used in environments that have an already running asyncio event loop (like Jupyter notebooks).
- **[Time](https://docs.python.org/3/library/time.html)**: A standard Python library for manipulating time-related tasks like setting timers, measuring execution time, and delaying actions.

### **Website:**

- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)**: Used for adding interactivity to the website, including button transitions and dynamic content updates.
- **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Used for styling the website to create a visually appealing and responsive design.
- **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)**: The backbone of the website, used for structuring the content and elements.

---

## 🤖 Discord Bots

The bot code can be found in the [**bots folder**](./bots). Below are examples of each bot in action:

### **Welcome Bot**
Greets delegates when they enter the COMUN server.

![COMUN Welcome Bot](https://user-images.githubusercontent.com/87055387/236654482-14f38c98-14b6-496a-925d-cd4b0cf6d69a.png)

### **Poll Bot**
Creates a poll for voting between three options: abstain, for, and against, and counts up the poll results.

![Poll Bot Command](https://user-images.githubusercontent.com/87055387/236654479-a42ebbc4-5390-4898-9892-2de130e4e388.png)

### **Roll Call Bot**
Asks delegates their status (present or present and voting) and stores the delegate's choice.

![Roll Call Bot](https://user-images.githubusercontent.com/87055387/236654469-a2fcb6ca-d936-48cb-b302-2f82caa570e9.png)

### **Timer Bot**
Creates a countdown timer with the `/time 60` command.

![Timer Bot](https://user-images.githubusercontent.com/87055387/236659709-80cca300-af8e-4453-8de1-9072b8e9854a.png)

### **Role Bot**
Assigns roles (committees delegates are in) via emojis after a specific command.

![Role Bot Command](https://user-images.githubusercontent.com/87055387/236660798-ec0a5467-956e-435f-b10b-bfba2af5a7a4.png)
![Role Bot Emojis](https://user-images.githubusercontent.com/87055387/236660826-0876c060-7501-4141-9232-2d73a3dbb72f.png)

---

## 🌐 Website

The website was designed with simplicity in mind using **JavaScript**, **HTML**, and **CSS**. It features interactive elements like button transitions and anchored social media buttons. The website's source code is located in the [**docs folder**](./docs).

![COMUN Website Screenshot](https://github.com/user-attachments/assets/768296e1-a431-4ba7-95b8-bad411e994db)

---

## 💻 Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ethanwongca/canadianonlinemun.git
   cd canadianonlinemun


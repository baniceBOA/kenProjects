

Projectile Motion Calculator
An Android  built with Python, Kivy, and Kivymd that calculates the physical properties of a projectile's motion  based on user input.
1. About the Project
This application provides a simple interface to calculate three key metrics of projectile motion:

* Maximum Height: The highest vertical point reached by the projectile.
* Horizontal Distance (Range): The total horizontal distance traveled before hitting the ground.
* The time taken to reach the maximum height.

How it Works
The app uses standard kinematic equations to process user input (Launch Velocity and Launch Angle).

* Assumptions: It assumes a constant gravitational acceleration of $9.8 m/s^2$ and zero air resistance 
* Logic: The mathematical logic is separated into func.py, while main.py and main.kv handle the reactive UI 
* Calculations: The app updates results in real-time as the user types into the input fields .

------------------------------
2. Project SetupLocal Development (Desktop)

   1. Clone the repository:
   
   git clone https://github.com
   cd kenProjects
   
   2. Create a virtual environment:
   
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   3. Install dependencies:
   
   pip install -r requirements.txt
   
   (Note: Ensure your Python version matches the project requirement of 3.11) .
   4. Run the application:
   
   python main.py
   
   
Android Build (CI/CD)
The project includes a GitHub Actions workflow (apkBuild.yaml) that automatically builds an APK whenever you push to the main branch. It uses Buildozer inside an Ubuntu environment to compile the Python code into an Android-ready package .
------------------------------
3. Dependencies & ReferencesApplication Dependencies
These are required to run the application, as specified in buildozer.spec :

* Python (3.11.9): The core programming language.
* Kivy (2.3.1): The framework used for the application's cross-platform lifecycle.
* Kivymd (1.2.0): A collection of Material Design compliant widgets for Kivy.
* Filetype: Used for file handling/identification.

Workflow Dependencies (GitHub Actions)

The .github/workflows/apkBuild.yaml file utilizes the following tools to automate the build 

* actions/checkout@v4: To pull the source code into the runner.
* digreatbrian/buildozer-action@v2: The primary action used to run the Buildozer command in a containerized environment.
* actions/upload-artifact@v4: To store the resulting .apk file for download.
* System Libraries: Specifically libtinfo5, libtool, pkg-config, autoconf, and automake are manually installed on the runner to ensure compatibility with Android's build toolchain 

------------------------------



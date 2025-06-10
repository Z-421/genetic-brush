# genetic-brush

**GeneticBrush** is an artistic-algorithmic project that reconstructs colorful images using genetic algorithms and simple shapes like circles.  
The project can take any image as input and gradually optimize an approximate artistic version of it. The main goal is to blend artificial intelligence and digital art to create unique artworks.

## Features
- Reconstructs color images using genetic algorithms  
- Accepts any image as input  
- Simple and extensible implementation in Python  
- Uses popular libraries such as PyGAD, PIL, and NumPy  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/genetic-brush.git
   cd genetic-brush
   ```
2.	(Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
3.	Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
1.	Prepare your target image (preferably resized to 64x64 or 128x128 pixels for performance).
2.	Run the main script to start the genetic algorithm process:
     ```bash
     python main.py --input your_image.jpg
     ```
  3.	The program will evolve and save intermediate and final images to monitor progress.

## Development
•	Feel free to fork the repo and submit pull requests.  
•	You can extend the project by adding new shapes, improving the fitness function, or enhancing the UI.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

# Lobete NFT Generator

This repository contains the script **NFT art generator** used to create the Lobete NFT collection.

The combination of hand-drawn layers creates a set of punk-styled wolf-rat characters with customizable traits. The NFTs generated here are the basic ones, a base where holders will be able to add traits later on when meeting certain requirements.

This script produces both the **image files** and the correspondant **metadata JSON files** for minting ERC721 NFTs.  
It is designed to be flexible so you can experiment with your ownhand-drawn traits, rarities and layers.


## Repository Structure

lobete-nft-generator/

│

├── lobeteNFTGenerator.py # Main Python code to generate the basic NFTs

├── lobeteNFTGenerator.ipynb # Jupiter notebook version for divided execution control

│

├── /metadata/ # Generated NFT metadata (empty by default)

│ └── all-traits.json # Generated traits for 100 NFTs used in tests

│

├── /lobetesIMG/

│ ├── /N-Trait/ # Several folders, one for each trait type, in order of layers. 

│ └── Z-FINAL/ # Generated NFT images (empty by default)

│

└── README.md


## Demo NFT Set (100 Lobetes NFTs)

A demo batch of **100 Lobetes NFT** has been generated in order to showcase the usage of the generator.  
These are hosted on **IPFS** to keep the repository lightweight and the images and metadata distributed and not centralized:  

- [IPFS link to demo images (100)](ipfs://<CID>/images/)  
- [IPFS link to demo metadata (100)](ipfs://<CID>/json/)  

*TODO (Replace `<CID>` with the uploaded folder CID once available.)*

## How to Run

1. Clone the repository:  
   ```bash
    git clone https://github.com/mazh-lycan/lobete-nft-generator
    cd lobete-nft-generator
2. Install dependencies
    pip install -r requirements.txt
3. Add the layers (PNG) for each trait type
4. Run the generator:
    python3 generator.py
5. Find your results in:
    - /lobetesIMG/Z-FINAL/ → generated NFT images (PNG)
    - /metadata/ → metadata files (JSON)

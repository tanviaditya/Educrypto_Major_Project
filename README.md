# Educrypto_Major_Project

# EduCrypto: Transforming Education using Blockchain

The proposed system is an Ethereum blockchain and IPFS based system for storing, retrieving, and authenticating educational documents as well as streamlining the entire process of examination and result generation. The proposed system comprises three main modules: Admission; Examination and Results; Third-Party Module. The authenticity of any document is guaranteed since it is shared within a secured environment. Existing research on similar solutions suffers from poor testing, lack of evaluation, and inefficient storage models. The proposed system overcomes these drawbacks. The proposed system was also evaluated for uploading and fetching latency. The average results show that the system has a mean execution time of 10176 milliseconds for uploading a 1.45MB document and a mean execution time of 110.7 milliseconds for fetching 6 documents each of size 214 kB. Thus, the system is found to be efficient in addition to being safe and secure.

# Prerequites
Below are things you need in order to run our system:

1. Ethereum: Ethereum is a decentralized blockchain platform that establishes a peer-to-peer network that securely executes and verifies application code, called smart contracts. It is a blockchain-based computing platform that enables developers to build and deploy decentralized applications. Ethereum has proven to be highly robust against attack while providing high security and stability.

2. Clique: Clique is a proof-of-authority consensus protocol. It shadows the design of Ethereum mainnet, so it can be added to any client with minimal effort.

3. Ganache framework: Ganache is a personalized blockchain for Ethereum development. It can be used to run tests, execute commands, and inspect states while controlling how the chain operates. Ganache is used for setting up a personal Ethereum Blockchain for testing your Solidity contracts.

4. Metamask extension: MetaMask is a software cryptocurrency wallet used to interact with the Ethereum blockchain. It allows users to access their Ethereum wallet through a browser extension or mobile app, which can then be used to interact with decentralized applications.

5. Web3. JS: Web3.js is a collection of libraries that allow you to interact with a local or remote ethereum node using HTTP, IPC or WebSocket. The web3 JavaScript library interacts with the Ethereum blockchain. It can retrieve user accounts, send transactions, interact with smart contracts, and more.

6. Chai assertion library: Chai is a BDD / TDD assertion library for node and the browser that can be delightfully paired with any javascript testing framework. 

7. Mocha test framework: Mocha is a feature-rich JavaScript test framework running on Node. js and in the browser, making asynchronous testing simple and fun.

8. Truffle Suite: Truffle is a world-class development environment, testing framework and asset pipeline for blockchains using the Ethereum Virtual Machine (EVM).

9. Django REST Framework: Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs. It is a toolkit built on top of the Django web framework that reduces the amount of code you need to write to create REST interfaces.

10. HTML CSS: HTML (Hypertext Markup Language) is used to create the actual content of the page, such as written text, and CSS (Cascade Styling Sheets) is responsible for the design or style of the website, including the layout, visual effects and background color.

11. Bootstrap: Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.

12. Javascript: JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions. It is used to develop interactive web applications.

13. JQuery: JQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. 

14. IPFS: The InterPlanetary File System is a protocol and peer-to-peer network for storing and sharing data in a distributed file system. IPFS uses content-addressing to uniquely identify each file in a global namespace connecting all computing devices. It can be leveraged to more efficiently store and share large files. It relies on cryptographic hashes that can easily be stored on a blockchain.


## Installation

Create and set up an account on Ganache and Metamask. Once you're done with it, enable the Metamask plugin and keep the Ganache framework open.




"Educrypto-Backend" is the folder where you will find all the backend code.

To run the backend code:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


"Educrypto-Frontend" is the folder where you will find all the frontend code.

To run the frontend code:
```bash
npm install
npm run dev
```

## Authors

1. Tanvi Aditya (https://github.com/tanviaditya)
2. Sagar Badlani (https://github.com/sagarbadlani)
3. Sarthak Maniar (https://github.com/sarthakmaniar27)


import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Utility functions =================================================

// Sample data of products
const products = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        initialQuantity: 4,
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        initialQuantity: 10,
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        initialQuantity: 2,
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        initialQuantity: 5,
    },
];

// Function to retrieve product by ID
function getProductById(id) {
    return products.find(product => product.id === id);
}

// Redis connection =================================================

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
    console.log(`Error with Redis connection: ${error.message}`);
});

client.on('connect', () => {
    console.log('Connected to Redis server');
});

// Functions for managing stock in Redis =============================

function reserveStockById(productId, quantity) {
    client.set(`product.${productId}.stock`, quantity);
}

async function getCurrentReservedStockById(productId) {
    const stock = await getAsync(`product.${productId}.stock`);
    return stock;
}

// Express setup ======================================================

const app = express();
const port = 1245;

const notFoundResponse = { status: 'Product not found' };

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

// Routes =============================================================

// Endpoint to list all products
app.get('/products', (req, res) => {
    res.json(products);
});

// Endpoint to get details of a specific product by ID
app.get('/products/:id', async (req, res) => {
    const productId = Number(req.params.id);
    const product = getProductById(productId);

    if (!product) {
        res.json(notFoundResponse);
        return;
    }

    const currentStock = await getCurrentReservedStockById(productId);

    if (!currentStock) {
        await reserveStockById(productId, product.initialQuantity);
        product.currentQuantity = product.initialQuantity;
    } else {
        product.currentQuantity = currentStock;
    }

    res.json(product);
});

// Endpoint to reserve a product by ID
app.get('/products/:id/reserve', async (req, res) => {
    const productId = Number(req.params.id);
    const product = getProductById(productId);
    const noStockResponse = { status: 'Not enough stock available', productId };
    const reservationConfirmedResponse = { status: 'Reservation confirmed', productId };

    if (!product) {
        res.json(notFoundResponse);
        return;
    }

    let currentStock = await getCurrentReservedStockById(productId);

    if (currentStock === null) {
        currentStock = product.initialQuantity;
    }

    if (currentStock <= 0) {
        res.json(noStockResponse);
        return;
    }

    reserveStockById(productId, Number(currentStock) - 1);
    res.json(reservationConfirmedResponse);
});


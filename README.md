
# Receipt Processor

## Overview
This project implements a web service for processing receipts and calculating points based on various rules. It uses FastAPI for the web framework and Pydantic for data validation.

## Project Structure
```
receipt_processor/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Installation

### Using Docker

1. **Build the Docker image**:
   ```sh
   docker build -t receipt-processor .
   ```

2. **Run the Docker container**:
   ```sh
   docker run -p 8000:8000 receipt-processor
   ```

Note: use `sudo` before the commands if there is a permission error

### Without Docker

1. **Clone the repository**:
   ```sh
   git clone https://github.com/AbdelrahmanZeidan5/receipt-processor.git
   cd receipt-processor
   ```

2. **Create a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Process Receipts
- **Endpoint**: `/receipts/process`
- **Method**: `POST`
- **Request Body**: JSON receipt
- **Response**: JSON containing an ID for the receipt

Example request:
```json
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"}
  ],
  "total": "9.00"
}
```

Example response:
```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```

### Get Points
- **Endpoint**: `/receipts/{receipt_id}/points`
- **Method**: `GET`
- **Response**: JSON object containing the number of points awarded

Example request:
```http
GET /receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points
```

Example response:
```json
{
  "points": 32
}
```

## Running Tests
You can test the endpoints using tools like Postman or cURL. Here's an example using cURL:

### Process Receipts
```sh
curl -X POST "http://127.0.0.1:8000/receipts/process" -H "Content-Type: application/json" -d '{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"},
    {"shortDescription": "Gatorade", "price": "2.25"}
  ],
  "total": "9.00"
}'
```

### Get Points
```sh
curl -X GET "http://127.0.0.1:8000/receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points"
```


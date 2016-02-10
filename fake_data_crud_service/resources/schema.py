schema = {
    "$schema": "http://json-schema.org/draft-04/hyper-schema#",
    "type": "object",
    "title": "Fake Data CRUD Service",
    "description": "Simple Flask web app to provide CRUD functionalities for fake data.",
    "definitions": {
        "book": {
            "type": "object",
            "title": "Book",
            "description": "Representation of a book.",
            "properties": {
                "ISBN": {
                    "type": "string",
                    "title": "ISBN",
                    "description": "International Standard Book Number",
                    "maxLength": 10
                },
                "authors": {
                    "type": "array",
                    "title": "Authors",
                    "description": "List of authors.",
                    "items": {
                        "type": "string",
                        "title": "Author",
                        "description": "Author of the book."
                    }
                },
                "title": {
                    "type": "string",
                    "title": "Title",
                    "description": "Title of the book."
                },
                "pages": {
                    "type": "integer",
                    "title": "Pages",
                    "description": "Number of pages."
                },
                "genre": {
                    "type": "string",
                    "title": "Genre",
                    "description": "Literary genre.",
                    "enum": [
                        "fiction",
                        "non-fiction"
                    ]
                }
            }
        }
    },
    "links": [
        {
            "href": "books/production/",
            "method": "GET",
            "rel": "books",
            "title": "Books",
            "description": "List of available books.",
            "targetSchema": {
                "properties": {
                    "type": "array",
                    "title": "Books",
                    "description": "List of available books.",
                    "items": {
                        "$ref": "#/definitions/book"
                    }
                }
            }
        },
        {
            "href": "books/production/:id",
            "method": "GET",
            "rel": "book",
            "title": "Book",
            "description": "Single book.",
            "schema": {
                "properties": {
                    "id": {
                        "type": "string",
                        "title": "Book ID",
                        "description": "ID of the selected book."
                    }
                }
            },
            "targetSchema": {
                "properties": {
                    "$ref": "#/definitions/book"
                }
            }
        }
    ],
    "properties": {
        "book": {
            "$ref": "#/definitions/book"
        }
    }
}

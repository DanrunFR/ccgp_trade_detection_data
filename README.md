# CCGP trade detection dataset

This dataset is designed for trade detection from titles of procurement document. 

## Description
Procurement documents in the dataset are originally published on www.ccgp.gov.cn. Title and trade are provided by buyers when uploading the documents, and are directly available on the listing page. Note that trade information is not always given.

All documents are written in simplified Chinese, and are in csv format with tabulation `\t` as delimiter.

There are 15994 entries in total, 8477 with trade information and 7517 without.

Each entry has 6 columns:
- `ref`: Reference code of the document on CCGP.
- `object_original`: Original title of the document.
- `object`: Cleaned title of the document. Agency name, project id and document types are removed with regex.
- `trade_original`: Original trade information of the document, chosen by the buyer.
- `trade`: Cleaned trade information. Only first-level trade information (supplies, works or services) is preserved. 
- `url`: URL of the original document.

## Inventory
```
├── data
│   ├── trade.csv : all entries
│   ├── trade_annotated.csv :  entries with trade information
│   ├── trade_non_annotated.csv :  entries without trade information
├── src
│   ├── utils.py : cleaning regex and functions
└── README.md
```

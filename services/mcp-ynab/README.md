# MCP YNAB Service

**GitHub Repository**: [https://github.com/ntdef/ynab-mcp](https://github.com/ntdef/ynab-mcp)

This is a Model Context Protocol server for interacting with YNAB (You Need A Budget) via their API. It enables LLMs to manage budgets, accounts, categories, and transactions through YNAB's comprehensive budgeting platform.

## Available Tools

### Budget Management
- `get_budgets` - Retrieve all budgets for the authenticated user
- `get_budget_summary` - Get a summary of the budget, optionally for a specific month

### Account Management  
- `get_accounts` - Retrieve all accounts for a specific budget

### Category Management
- `get_categories` - Retrieve all categories for a specific budget
- `create_category` - Create a new category in the specified budget group
- `update_category_budgeted` - Update the budgeted amount for a category in a specific month

### Transaction Management
- `get_transactions` - Retrieve transactions for a specific budget, optionally filtered by date, account, or category
- `create_transaction` - Create a new transaction in the specified budget
- `update_transaction` - Update one or more fields of a specific transaction

## Requirements

- YNAB account with API token (get from [YNAB Developer Settings](https://app.ynab.com/settings/developer))
- Environment variable:
  - `YNAB_API_TOKEN` - Your YNAB API token
- Python 3.13+ (if not using Docker)

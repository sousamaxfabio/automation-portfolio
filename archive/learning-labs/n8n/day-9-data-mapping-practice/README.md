\# Day 9 – n8n Data Mapping Practice



\## Overview



A beginner n8n workflow demonstrating structured data, expressions, data mapping, conditional routing, and execution history.



\## Workflow



Manual Trigger → Create Sample Data → Build Confirmation → Check Service



\## What It Does



1\. Starts manually.

2\. Creates sample customer-service data.

3\. Maps incoming JSON values into new fields.

4\. Builds a confirmation message using expressions.

5\. Uses an If node to route the item according to the requested service.



\## Sample Data



```json

{

&#x20; "customer\_name": "Fabio",

&#x20; "service": "invoice automation",

&#x20; "urgency": "high"

}

```



\## Example Output



```json

{

&#x20; "customer\_name": "Fabio",

&#x20; "service": "invoice automation",

&#x20; "urgency": "high",

&#x20; "copied\_name": "Fabio",

&#x20; "confirmation\_message": "Hello Fabio, your request for invoice automation has been received."

}

```



\## Skills Practised



\- Manual Trigger

\- Edit Fields

\- JSON data

\- Data mapping

\- n8n expressions

\- Preserving incoming fields

\- If conditions

\- True and False branches

\- Execution-history debugging



\## Files



\- `workflow.json` — exported n8n workflow

\- `screenshots/workflow-execution.png` — successful workflow execution



\## Security



This practice workflow contains no credentials, passwords, or API keys.


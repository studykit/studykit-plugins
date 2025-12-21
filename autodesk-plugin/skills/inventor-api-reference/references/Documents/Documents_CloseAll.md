# Documents.CloseAll Method

Parent Object: [Documents](../Documents/Documents.md)

## Description

Method that closes all the documents in the current Inventor session. Changes are not saved to any of the documents. In other words, if there are dirty documents in the collection, changes made to them will be lost.

## Syntax

Documents.**CloseAll**( [***UnreferencedOnly***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UnreferencedOnly | Boolean | Optional input Boolean that indicates whether to close only the unreferenced documents. If not specified, a value of False is assumed and all documents are closed. Examples of unreferenced documents: \* Create a new assembly, place an instance of a part "block.ipt", (provided block.ipt is not open in it's own window) and then delete the instance in the assembly. At this point, block.ipt is an unreferenced document. \* Set the Suppressed property of a ComponentOccurrence to True within an API Transaction (or a ChangeProcessor). Assuming that the document that this occurrence was referencing is not referenced elsewhere, it becomes an "unreferenced" document. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
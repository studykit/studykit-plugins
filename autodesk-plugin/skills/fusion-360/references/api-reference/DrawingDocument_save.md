# DrawingDocument.save Method

Parent Object: [DrawingDocument](DrawingDocument.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/DrawingDocument.h>

## Description

Saves a version of the current document. You must use the SaveAs method the first time a document is saved. You can determine if a document has been saved by checking the value of the isSaved property.

## Remarks

Saving a document is not supported within any of the Command related events. When a command is running, a transaction is open, and saving a document cannot be transacted and, as a result, cannot be contained within a command transaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawingDocument\_var" is a variable referencing a [DrawingDocument](DrawingDocument.htm) object.```` ``` returnValue = drawingDocument_var.save(description) ``` ```` |

"drawingDocument\_var" is a variable referencing a [DrawingDocument](DrawingDocument.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if saving the document was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| description | string | The version description for this document |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
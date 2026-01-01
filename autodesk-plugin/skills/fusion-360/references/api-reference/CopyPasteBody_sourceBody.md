# CopyPasteBody.sourceBody Property

Parent Object: [CopyPasteBody](CopyPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBody.h>

## Description

Returns the bodies that were copied to create the result bodies of this feature. An ObjectCollection is returned that will contain the original bodies. It's possible that the collection can be empty or contain less than the number of bodies originally copied. This happens in the case where a body has been deleted or consumed by some other operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object.  ```` ``` # Get the value of the property. propertyValue = copyPasteBody_var.sourceBody ``` ```` |

"copyPasteBody\_var" is a variable referencing a CopyPasteBody object. ```` ``` #include <Fusion/Features/CopyPasteBody.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = copyPasteBody_var->sourceBody(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copy Paste Bodies API Sample](CopyPasteBodiesSample_Sample.htm) | Demonstrates how to use Copy Paste Bodies related API. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
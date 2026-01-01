# CutPasteBody.sourceBody Property

Parent Object: [CutPasteBody](CutPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBody.h>

## Description

Returns the bodies that were cut to create the result bodies of this feature. An ObjectCollection is returned that will contain the original bodies. It's possible that the collection can be empty or contain less than the number of bodies originally copied. This happens in the case where a body has been deleted or consumed by some other operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBody\_var" is a variable referencing a CutPasteBody object.  ```` ``` # Get the value of the property. propertyValue = cutPasteBody_var.sourceBody ``` ```` |

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. ```` ``` #include <Fusion/Features/CutPasteBody.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = cutPasteBody_var->sourceBody(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
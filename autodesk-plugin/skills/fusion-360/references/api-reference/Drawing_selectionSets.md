# Drawing.selectionSets Property

Parent Object: [Drawing](Drawing.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/Drawing.h>

## Description

Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawing\_var" is a variable referencing a Drawing object. |

"drawing\_var" is a variable referencing a Drawing object. ```` ``` #include <Drawing/Drawing/Drawing.h>  // Get the value of the property. Ptr<SelectionSets> propertyValue = drawing_var->selectionSets(); ``` ```` |

## Property Value

This is a read only property whose value is a [SelectionSets](SelectionSets.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
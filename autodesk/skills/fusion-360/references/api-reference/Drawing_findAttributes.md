# Drawing.findAttributes Method

Parent Object: [Drawing](Drawing.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/Drawing.h>

## Description

Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"drawing\_var" is a variable referencing a [Drawing](Drawing.htm) object.```` ``` returnValue = drawing_var.findAttributes(groupName, attributeName) ``` ```` |

"drawing\_var" is a variable referencing a [Drawing](Drawing.htm) object.  ```` ``` #include <Drawing/Drawing/Drawing.h>  returnValue = drawing_var->findAttributes(groupName, attributeName); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Attribute](Attribute.htm)[] | An array of Attribute objects that were found. An empty array is returned if no attributes were found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| groupName | string | The search string for the group name. See above for more details. |
| attributeName | string | The search string for the attribute name. See above for more details. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
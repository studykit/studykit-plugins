# FlatPatternProduct.findAttributes Method

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.```` ``` returnValue = flatPatternProduct_var.findAttributes(groupName, attributeName) ``` ```` |

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.  ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  returnValue = flatPatternProduct_var->findAttributes(groupName, attributeName); ``` ```` |

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

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
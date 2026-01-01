# CAM.findAttributes Method

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.```` ``` returnValue = cAM_var.findAttributes(groupName, attributeName) ``` ```` |

"cAM\_var" is a variable referencing a [CAM](CAM.htm) object.  ```` ``` #include <Cam/CAM/CAM.h>  returnValue = cAM_var->findAttributes(groupName, attributeName); ``` ```` |

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

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
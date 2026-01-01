# RemoveFeature.itemToRemove Property

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

Gets and sets the body or component occurrence to remove.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a RemoveFeature object.  ```` ``` # Get the value of the property. propertyValue = removeFeature_var.itemToRemove ``` ```` |

"removeFeature\_var" is a variable referencing a RemoveFeature object. ```` ``` #include <Fusion/Features/RemoveFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = removeFeature_var->itemToRemove(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
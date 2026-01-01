# CustomGraphicsEntity.parent Property

Parent Object: [CustomGraphicsEntity](CustomGraphicsEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsEntity.h>

## Description

Returns the parent Component for a top-level group or the CustomGraphicsGroup object for graphics entities and child groups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsEntity\_var" is a variable referencing a CustomGraphicsEntity object. |

"customGraphicsEntity\_var" is a variable referencing a CustomGraphicsEntity object. ```` ``` #include <Fusion/Graphics/CustomGraphicsEntity.h>  // Get the value of the property. Ptr<Base> propertyValue = customGraphicsEntity_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
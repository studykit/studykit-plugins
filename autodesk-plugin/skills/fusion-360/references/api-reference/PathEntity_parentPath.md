# PathEntity.parentPath Property

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

Property that returns the parent Path of the entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a PathEntity object. |

"pathEntity\_var" is a variable referencing a PathEntity object. ```` ``` #include <Fusion/Features/PathEntity.h>  // Get the value of the property. Ptr<Path> propertyValue = pathEntity_var->parentPath(); ``` ```` |

## Property Value

This is a read only property whose value is a [Path](Path.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
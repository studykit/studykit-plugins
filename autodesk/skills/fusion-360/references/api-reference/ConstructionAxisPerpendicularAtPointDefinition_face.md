# ConstructionAxisPerpendicularAtPointDefinition.face Property

Parent Object: [ConstructionAxisPerpendicularAtPointDefinition](ConstructionAxisPerpendicularAtPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisPerpendicularAtPointDefinition.h>

## Description

Returns the face the construction axis is perpendicular to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisPerpendicularAtPointDefinition\_var" is a variable referencing a ConstructionAxisPerpendicularAtPointDefinition object. |

"constructionAxisPerpendicularAtPointDefinition\_var" is a variable referencing a ConstructionAxisPerpendicularAtPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisPerpendicularAtPointDefinition.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = constructionAxisPerpendicularAtPointDefinition_var->face(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
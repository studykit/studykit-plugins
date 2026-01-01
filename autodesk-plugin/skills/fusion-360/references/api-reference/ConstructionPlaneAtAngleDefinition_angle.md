# ConstructionPlaneAtAngleDefinition.angle Property

Parent Object: [ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>

## Description

Returns a Parameter object that controls the value of the angle. You can use properties of the returned Parameter object to modify the angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a ConstructionPlaneAtAngleDefinition object. |

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a ConstructionPlaneAtAngleDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>  // Get the value of the property. Ptr<Parameter> propertyValue = constructionPlaneAtAngleDefinition_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [Parameter](Parameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
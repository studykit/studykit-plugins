# ConstructionPlaneAtAngleDefinition.planarEntity Property

Parent Object: [ConstructionPlaneAtAngleDefinition](ConstructionPlaneAtAngleDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>

## Description

Gets the planar face or construction plane the angle for this construction plane is measured from and is parametrically dependent on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a ConstructionPlaneAtAngleDefinition object.  ```` ``` # Get the value of the property. propertyValue = constructionPlaneAtAngleDefinition_var.planarEntity ``` ```` |

"constructionPlaneAtAngleDefinition\_var" is a variable referencing a ConstructionPlaneAtAngleDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneAtAngleDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = constructionPlaneAtAngleDefinition_var->planarEntity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
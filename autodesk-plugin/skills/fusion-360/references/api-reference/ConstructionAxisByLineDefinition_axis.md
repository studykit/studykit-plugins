# ConstructionAxisByLineDefinition.axis Property

Parent Object: [ConstructionAxisByLineDefinition](ConstructionAxisByLineDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisByLineDefinition.h>

## Description

Gets and sets the infinite line that defines the position and direction of the axis

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisByLineDefinition\_var" is a variable referencing a ConstructionAxisByLineDefinition object. |

"constructionAxisByLineDefinition\_var" is a variable referencing a ConstructionAxisByLineDefinition object. ```` ``` #include <Fusion/Construction/ConstructionAxisByLineDefinition.h>  // Get the value of the property. Ptr<InfiniteLine3D> propertyValue = constructionAxisByLineDefinition_var->axis();  // Set the value of the property, where value_var is an InfiniteLine3D. bool returnValue = constructionAxisByLineDefinition_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [InfiniteLine3D](InfiniteLine3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
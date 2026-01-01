# ConstructionPlaneOffsetDefinition.offset Property

Parent Object: [ConstructionPlaneOffsetDefinition](ConstructionPlaneOffsetDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneOffsetDefinition.h>

## Description

Returns a Parameter object that controls the value of the offset. You can use properties of the returned Parameter object to modify the offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneOffsetDefinition\_var" is a variable referencing a ConstructionPlaneOffsetDefinition object. |

"constructionPlaneOffsetDefinition\_var" is a variable referencing a ConstructionPlaneOffsetDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneOffsetDefinition.h>  // Get the value of the property. Ptr<Parameter> propertyValue = constructionPlaneOffsetDefinition_var->offset(); ``` ```` |

## Property Value

This is a read only property whose value is a [Parameter](Parameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
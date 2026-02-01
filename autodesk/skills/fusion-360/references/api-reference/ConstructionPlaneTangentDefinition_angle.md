# ConstructionPlaneTangentDefinition.angle Property

Parent Object: [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentDefinition.h>

## Description

Returns a Value object that for a transient definition provides the current assigned value. For a definition associated with a construction plane, it provides access to the associated parameter controlling the angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneTangentDefinition\_var" is a variable referencing a ConstructionPlaneTangentDefinition object. |

"constructionPlaneTangentDefinition\_var" is a variable referencing a ConstructionPlaneTangentDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPlaneTangentDefinition.h>  // Get the value of the property. Ptr<Parameter> propertyValue = constructionPlaneTangentDefinition_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [Parameter](Parameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
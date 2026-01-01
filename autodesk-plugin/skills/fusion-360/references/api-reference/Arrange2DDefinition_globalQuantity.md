# Arrange2DDefinition.globalQuantity Property

Parent Object: [Arrange2DDefinition](Arrange2DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DDefinition.h>

## Description

Returns the parameter that controls the global quantity. You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. |

"arrange2DDefinition\_var" is a variable referencing an Arrange2DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange2DDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrange2DDefinition_var->globalQuantity(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
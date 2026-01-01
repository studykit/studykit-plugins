# Arrange3DDefinition.isCreateCopies Property

Parent Object: [Arrange3DDefinition](Arrange3DDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DDefinition.h>

## Description

Gets if the original components were moved to create the arrangement or copied were created. This value can only be set when creating a new arrangement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DDefinition\_var" is a variable referencing an Arrange3DDefinition object. |

"arrange3DDefinition\_var" is a variable referencing an Arrange3DDefinition object. ```` ``` #include <Fusion/Arrange/Arrange3DDefinition.h>  // Get the value of the property. boolean propertyValue = arrange3DDefinition_var->isCreateCopies(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
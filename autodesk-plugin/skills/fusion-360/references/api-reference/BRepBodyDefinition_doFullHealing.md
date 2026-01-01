# BRepBodyDefinition.doFullHealing Property

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

Specifies if full healing is done when creating the body. This defaults to true and it's highly recommended that you do full healing because it can find and correct problems with the input. If you're sure that the B-Rep definition that you've constructed is correct then you can set this to false to skip the full healing process.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. |

"bRepBodyDefinition\_var" is a variable referencing a BRepBodyDefinition object. ```` ``` #include <Fusion/BRep/BRepBodyDefinition.h>  // Get the value of the property. boolean propertyValue = bRepBodyDefinition_var->doFullHealing();  // Set the value of the property, where value_var is a boolean. bool returnValue = bRepBodyDefinition_var->doFullHealing(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
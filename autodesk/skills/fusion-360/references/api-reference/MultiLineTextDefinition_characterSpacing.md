# MultiLineTextDefinition.characterSpacing Property

Parent Object: [MultiLineTextDefinition](MultiLineTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

Gets and sets the spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. |

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. ```` ``` #include <Fusion/Sketch/MultiLineTextDefinition.h>  // Get the value of the property. double propertyValue = multiLineTextDefinition_var->characterSpacing();  // Set the value of the property, where value_var is a double. bool returnValue = multiLineTextDefinition_var->characterSpacing(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
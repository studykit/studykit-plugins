# MultiLineTextDefinition.horizontalAlignment Property

Parent Object: [MultiLineTextDefinition](MultiLineTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MultiLineTextDefinition.h>

## Description

Gets and sets the horizontal alignment of the text with respect to the text rectangle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. |

"multiLineTextDefinition\_var" is a variable referencing a MultiLineTextDefinition object. ```` ``` #include <Fusion/Sketch/MultiLineTextDefinition.h>  // Get the value of the property. HorizontalAlignments propertyValue = multiLineTextDefinition_var->horizontalAlignment();  // Set the value of the property, where value_var is a HorizontalAlignments. bool returnValue = multiLineTextDefinition_var->horizontalAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [HorizontalAlignments](HorizontalAlignments.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
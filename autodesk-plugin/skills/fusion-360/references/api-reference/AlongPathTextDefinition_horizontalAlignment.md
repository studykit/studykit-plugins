# AlongPathTextDefinition.horizontalAlignment Property

Parent Object: [AlongPathTextDefinition](AlongPathTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/AlongPathTextDefinition.h>

## Description

Gets and sets the horizontal alignment of the text with respect to the path curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. |

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. ```` ``` #include <Fusion/Sketch/AlongPathTextDefinition.h>  // Get the value of the property. HorizontalAlignments propertyValue = alongPathTextDefinition_var->horizontalAlignment();  // Set the value of the property, where value_var is a HorizontalAlignments. bool returnValue = alongPathTextDefinition_var->horizontalAlignment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [HorizontalAlignments](HorizontalAlignments.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
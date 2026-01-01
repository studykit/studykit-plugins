# AlongPathTextDefinition.isAbovePath Property

Parent Object: [AlongPathTextDefinition](AlongPathTextDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/AlongPathTextDefinition.h>

## Description

Gets and sets if the text should be positioned above or below the path entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. |

"alongPathTextDefinition\_var" is a variable referencing an AlongPathTextDefinition object. ```` ``` #include <Fusion/Sketch/AlongPathTextDefinition.h>  // Get the value of the property. boolean propertyValue = alongPathTextDefinition_var->isAbovePath();  // Set the value of the property, where value_var is a boolean. bool returnValue = alongPathTextDefinition_var->isAbovePath(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
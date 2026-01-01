# BoxFeature.name Property

Parent Object: [BoxFeature](BoxFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeature.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"boxFeature\_var" is a variable referencing a BoxFeature object. |

"boxFeature\_var" is a variable referencing a BoxFeature object. ```` ``` #include <Fusion/Features/BoxFeature.h>  // Get the value of the property. string propertyValue = boxFeature_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = boxFeature_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
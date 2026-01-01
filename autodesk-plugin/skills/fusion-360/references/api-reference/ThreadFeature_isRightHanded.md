# ThreadFeature.isRightHanded Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object.  ```` ``` # Get the value of the property. propertyValue = threadFeature_var.isRightHanded  # Set the value of the property. threadFeature_var.isRightHanded = propertyValue ``` ```` |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. boolean propertyValue = threadFeature_var->isRightHanded();  // Set the value of the property, where value_var is a boolean. bool returnValue = threadFeature_var->isRightHanded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
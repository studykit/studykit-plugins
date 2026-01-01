# ThreadFeature.isFullLength Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Gets and sets if this thread is the full length of the cylinder. It only can be set to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object.  ```` ``` # Get the value of the property. propertyValue = threadFeature_var.isFullLength  # Set the value of the property. threadFeature_var.isFullLength = propertyValue ``` ```` |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. boolean propertyValue = threadFeature_var->isFullLength();  // Set the value of the property, where value_var is a boolean. bool returnValue = threadFeature_var->isFullLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
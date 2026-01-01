# ThreadFeature.threadInfo Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Gets and sets the thread data. Also can edit the thread through the properties and methods on the ThreadInfo object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object.  ```` ``` # Get the value of the property. propertyValue = threadFeature_var.threadInfo  # Set the value of the property. threadFeature_var.threadInfo = propertyValue ``` ```` |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. Ptr<ThreadInfo> propertyValue = threadFeature_var->threadInfo();  // Set the value of the property, where value_var is a ThreadInfo. bool returnValue = threadFeature_var->threadInfo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThreadInfo](ThreadInfo.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
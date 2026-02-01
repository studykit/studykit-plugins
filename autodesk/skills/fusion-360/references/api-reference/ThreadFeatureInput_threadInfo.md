# ThreadFeatureInput.threadInfo Property

Parent Object: [ThreadFeatureInput](ThreadFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatureInput.h>

## Description

Gets and sets the information that defines the thread.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. |

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. ```` ``` #include <Fusion/Features/ThreadFeatureInput.h>  // Get the value of the property. Ptr<ThreadInfo> propertyValue = threadFeatureInput_var->threadInfo();  // Set the value of the property, where value_var is a ThreadInfo. bool returnValue = threadFeatureInput_var->threadInfo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThreadInfo](ThreadInfo.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
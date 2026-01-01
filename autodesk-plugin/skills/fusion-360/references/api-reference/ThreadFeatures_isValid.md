# ThreadFeatures.isValid Property

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a ThreadFeatures object. |

"threadFeatures\_var" is a variable referencing a ThreadFeatures object. ```` ``` #include <Fusion/Features/ThreadFeatures.h>  // Get the value of the property. boolean propertyValue = threadFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
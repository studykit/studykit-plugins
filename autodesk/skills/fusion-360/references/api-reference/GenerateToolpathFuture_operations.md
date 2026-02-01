# GenerateToolpathFuture.operations Property

Parent Object: [GenerateToolpathFuture](GenerateToolpathFuture.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/GenerateToolpathFuture.h>

## Description

Returns a collection of all operations that need to be generated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generateToolpathFuture\_var" is a variable referencing a GenerateToolpathFuture object. |

"generateToolpathFuture\_var" is a variable referencing a GenerateToolpathFuture object. ```` ``` #include <Cam/CAM/GenerateToolpathFuture.h>  // Get the value of the property. Ptr<Operations> propertyValue = generateToolpathFuture_var->operations(); ``` ```` |

## Property Value

This is a read only property whose value is an [Operations](Operations.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
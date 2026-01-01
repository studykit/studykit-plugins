# CAMPattern.parent Property

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Returns the parent Setup, Folder or Pattern for this Folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a CAMPattern object. |

"cAMPattern\_var" is a variable referencing a CAMPattern object. ```` ``` #include <Cam/CAM/CAMPattern.h>  // Get the value of the property. Ptr<Base> propertyValue = cAMPattern_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
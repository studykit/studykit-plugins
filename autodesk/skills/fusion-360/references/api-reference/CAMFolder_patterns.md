# CAMFolder.patterns Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Returns the Patterns collection that provides access to existing patterns in this folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. Ptr<CAMPatterns> propertyValue = cAMFolder_var->patterns(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMPatterns](CAMPatterns.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
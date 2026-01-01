# CAMLibrary.assetTypeName Property

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

Get the name of the asset type which can be accessed by the library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a CAMLibrary object. |

"cAMLibrary\_var" is a variable referencing a CAMLibrary object. ```` ``` #include <Cam/Global/CAMLibrary.h>  // Get the value of the property. string propertyValue = cAMLibrary_var->assetTypeName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
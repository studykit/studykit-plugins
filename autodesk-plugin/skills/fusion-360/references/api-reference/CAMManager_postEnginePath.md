# CAMManager.postEnginePath Property

Parent Object: [CAMManager](CAMManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMManager.h>

## Description

Gets the absolute path to the post engine (post.exe) installed with Fusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMManager\_var" is a variable referencing a CAMManager object. |

"cAMManager\_var" is a variable referencing a CAMManager object. ```` ``` #include <Cam/Global/CAMManager.h>  // Get the value of the property. string propertyValue = cAMManager_var->postEnginePath(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
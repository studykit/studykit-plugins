# CAMParameter.title Property

Parent Object: [CAMParameter](CAMParameter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameter.h>

## Description

Returns the title of this parameter as seen in the user interface. This title is localized and can change based on the current language

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameter\_var" is a variable referencing a CAMParameter object. |

"cAMParameter\_var" is a variable referencing a CAMParameter object. ```` ``` #include <Cam/Operations/CAMParameter.h>  // Get the value of the property. string propertyValue = cAMParameter_var->title(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
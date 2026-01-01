# Profiles.count Property

Parent Object: [Profiles](Profiles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profiles.h>

## Description

Returns the number of closed profiles in the sketch. Open and text based profiles are not included.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profiles\_var" is a variable referencing a Profiles object. |

"profiles\_var" is a variable referencing a Profiles object. ```` ``` #include <Fusion/Sketch/Profiles.h>  // Get the value of the property. uinteger propertyValue = profiles_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
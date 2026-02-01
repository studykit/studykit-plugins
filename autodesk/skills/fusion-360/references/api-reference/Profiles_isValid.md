# Profiles.isValid Property

Parent Object: [Profiles](Profiles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profiles.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profiles\_var" is a variable referencing a Profiles object. |

"profiles\_var" is a variable referencing a Profiles object. ```` ``` #include <Fusion/Sketch/Profiles.h>  // Get the value of the property. boolean propertyValue = profiles_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
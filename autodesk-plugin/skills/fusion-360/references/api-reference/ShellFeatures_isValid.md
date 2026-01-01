# ShellFeatures.isValid Property

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a ShellFeatures object. |

"shellFeatures\_var" is a variable referencing a ShellFeatures object. ```` ``` #include <Fusion/Features/ShellFeatures.h>  // Get the value of the property. boolean propertyValue = shellFeatures_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
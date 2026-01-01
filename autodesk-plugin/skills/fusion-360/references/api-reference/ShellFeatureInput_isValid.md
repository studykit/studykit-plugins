# ShellFeatureInput.isValid Property

Parent Object: [ShellFeatureInput](ShellFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatureInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. |

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. ```` ``` #include <Fusion/Features/ShellFeatureInput.h>  // Get the value of the property. boolean propertyValue = shellFeatureInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
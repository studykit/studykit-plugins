# NamedView.isBuiltIn Property

Parent Object: [NamedView](NamedView.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedView.h>

## Description

Indicates if this named view is one of the four standard named views ("TOP", "FRONT", "RIGHT", and "HOME"). There is limited functionality with the four standard named views.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedView\_var" is a variable referencing a NamedView object. |

"namedView\_var" is a variable referencing a NamedView object. ```` ``` #include <Core/Application/NamedView.h>  // Get the value of the property. boolean propertyValue = namedView_var->isBuiltIn(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
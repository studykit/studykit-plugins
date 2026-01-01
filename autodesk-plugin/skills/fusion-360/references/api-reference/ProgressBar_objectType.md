# ProgressBar.objectType Property

Parent Object: [ProgressBar](ProgressBar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressBar.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressBar\_var" is a variable referencing a ProgressBar object.  ```` ``` # Get the value of the property. propertyValue = progressBar_var.objectType ``` ```` |

"progressBar\_var" is a variable referencing a ProgressBar object. ```` ``` #include <Core/UserInterface/ProgressBar.h>  // Get the value of the property. string propertyValue = progressBar_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
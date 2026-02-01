# Analysis.name Property

Parent Object: [Analysis](Analysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analysis.h>

## Description

A property that gets and sets the name of the analysis. If you use a name that is not unique, Fusion will automatically append a number to the name to make it unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analysis\_var" is a variable referencing an Analysis object. |

"analysis\_var" is a variable referencing an Analysis object. ```` ``` #include <Fusion/Fusion/Analysis.h>  // Get the value of the property. string propertyValue = analysis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = analysis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |
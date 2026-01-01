# ShellFeature.shellType Property

Parent Object: [ShellFeature](ShellFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeature.h>

## Description

The shell type used when creating a shell. The default value is SharpOffsetShellType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeature\_var" is a variable referencing a ShellFeature object.  ```` ``` # Get the value of the property. propertyValue = shellFeature_var.shellType  # Set the value of the property. shellFeature_var.shellType = propertyValue ``` ```` |

"shellFeature\_var" is a variable referencing a ShellFeature object. ```` ``` #include <Fusion/Features/ShellFeature.h>  // Get the value of the property. ShellTypes propertyValue = shellFeature_var->shellType();  // Set the value of the property, where value_var is a ShellTypes. bool returnValue = shellFeature_var->shellType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ShellTypes](ShellTypes.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
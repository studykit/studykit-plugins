# ShellFeatureInput.shellType Property

Parent Object: [ShellFeatureInput](ShellFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatureInput.h>

## Description

The shell type used when creating a shell. The default value is SharpOffsetShellType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. |

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. ```` ``` #include <Fusion/Features/ShellFeatureInput.h>  // Get the value of the property. ShellTypes propertyValue = shellFeatureInput_var->shellType();  // Set the value of the property, where value_var is a ShellTypes. bool returnValue = shellFeatureInput_var->shellType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ShellTypes](ShellTypes.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
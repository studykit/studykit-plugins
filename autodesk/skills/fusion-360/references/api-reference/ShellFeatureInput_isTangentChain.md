# ShellFeatureInput.isTangentChain Property

Parent Object: [ShellFeatureInput](ShellFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatureInput.h>

## Description

Gets and sets if any faces that are tangentially connected to any of the input faces will also be included in setting InputEntities. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. |

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. ```` ``` #include <Fusion/Features/ShellFeatureInput.h>  // Get the value of the property. boolean propertyValue = shellFeatureInput_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = shellFeatureInput_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Parameter.dependencyParameters Property

Parent Object: [Parameter](Parameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

Returns a list of parameters that this parameter is dependent on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameter\_var" is a variable referencing a Parameter object. |

"parameter\_var" is a variable referencing a Parameter object. ```` ``` #include <Fusion/Fusion/Parameter.h>  // Get the value of the property. Ptr<ParameterList> propertyValue = parameter_var->dependencyParameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [ParameterList](ParameterList.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
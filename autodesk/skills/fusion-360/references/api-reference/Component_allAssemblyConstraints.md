# Component.allAssemblyConstraints Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns all assembly constraints in this component and any sub components. The assembly constraints returned are all in the context of this component so any joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joints, when manipulating an assembly.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. std::vector<Ptr<AssemblyConstraint>> propertyValue = component_var->allAssemblyConstraints(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [AssemblyConstraint](AssemblyConstraint.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
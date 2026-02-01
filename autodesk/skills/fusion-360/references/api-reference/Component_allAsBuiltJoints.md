# Component.allAsBuiltJoints Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns all joint origins in this component and any sub components. The joint origins returned are all in the context of this component so any joint origins in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joint origins, when manipulating an assembly.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. std::vector<Ptr<AsBuiltJoint>> propertyValue = component_var->allAsBuiltJoints(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [AsBuiltJoint](AsBuiltJoint.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
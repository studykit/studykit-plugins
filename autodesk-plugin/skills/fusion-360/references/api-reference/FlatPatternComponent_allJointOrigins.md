# FlatPatternComponent.allJointOrigins Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns all as-built joints in this component and any sub components. The as-built joints returned are all in the context of this component so any as-built joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including as-built joints, when manipulating an assembly.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. std::vector<Ptr<JointOrigin>> propertyValue = flatPatternComponent_var->allJointOrigins(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [JointOrigin](JointOrigin.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
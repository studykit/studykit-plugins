# AsBuiltJoint.name Property

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

The name of the as-built joint as it is displayed in the timeline and the browser. The name can be changed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. |

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Get the value of the property. string propertyValue = asBuiltJoint_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = asBuiltJoint_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |